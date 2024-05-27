import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import owiener
from encoders.converters import textToBinary, binaryToDecimal, decimalToText


def getNumbersFromPEMRSAKey(rsaKey):
    try:
        if "-----BEGIN PUBLIC KEY-----" in rsaKey:
            publicKey = serialization.load_pem_public_key(bytes(rsaKey, 'utf-8'))
            numbers = publicKey.public_numbers()
            return {'n': numbers.n, 'e': numbers.e}
        elif "-----BEGIN RSA PRIVATE KEY-----" in rsaKey:
            privateKey = serialization.load_pem_private_key(bytes(rsaKey, 'utf-8'), password=None)
            privateNumbers = privateKey.private_numbers()
            publicNumbers = privateNumbers.public_numbers

            return {'n': publicNumbers.n, 'e': publicNumbers.e, 'd': privateNumbers.d}
    except:
        return 'error'
    
# Encrypt or decrypt
def rsaDencrypt(rsaKey, message):
    if "-----BEGIN PUBLIC KEY-----" in rsaKey:
        publicKey = serialization.load_pem_public_key(bytes(rsaKey, 'utf-8'))
        ciphertext = publicKey.encrypt(
            bytes(message, 'utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(ciphertext).decode('ascii')
    
    elif "-----BEGIN RSA PRIVATE KEY-----" in rsaKey:
        privateKey = serialization.load_pem_private_key(bytes(rsaKey, 'utf-8'), password=None)
        plaintext = privateKey.decrypt(
            base64.b64decode(message),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode('utf-8')
    
def simpleRSAEncrypt(inputText, n, e):
    inputBinary = textToBinary(inputText)
    inputDecimal = binaryToDecimal(inputBinary)
    cipherDecimal = pow(int(inputDecimal), e, n)
    return cipherDecimal

def simpleRSADecrypt(cipherDecimal, n, d):
    clearDecimal = pow(cipherDecimal, d, n)
    clearText = decimalToText(clearDecimal)
    return clearText
    
def WienerAttack(n, e):
    d = owiener.attack(e, n)

    if d is None:
        return -1
    else:
        return d