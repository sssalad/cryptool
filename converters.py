from base64 import b64encode, b64decode

########################
##### Binary to... #####
########################
def binaryToText(binaryString):
    dec = int(binaryString, 2)
    text = dec.to_bytes((dec.bit_length() + 7) // 8, 'big').decode()
    return text

def binaryToHex(binaryString):
    dec = int(binaryString, 2)
    hexidecimal = hex(dec)
    return hexidecimal[2:]

def binaryToB64(binaryString):
    hexidecimal = binaryToHex(binaryString)
    b64 = b64encode(bytes.fromhex(hexidecimal)).decode()
    return b64

#############################
##### Hexidecimal to... #####
#############################
def hexToBinary(hexString):
    binaryString = bin(int(hexString, 16)).zfill(8)
    return binaryString

def hexToText(hexString):
    text = bytes.fromhex(hexString).decode('utf-8')
    return text

def hexToB64(hexString):
    b64 = b64encode(bytes.fromhex(hexString)).decode()
    return b64

######################
##### Text to... #####
######################
def textToBinary(text):
    binaryString = ' '.join(format(ord(x), 'b') for x in text)
    return binaryString

def textToHex(text):
    hexidecimal = text.encode("utf-8").hex()
    return hexidecimal

def textToB64(text):
    b64 = b64encode(text.encode('ascii'))
    return b64

########################
##### Base64 to... #####
########################
def base64ToBinary(b64String):
    hexidecimal = b64decode(b64String.encode()).hex()
    binaryString = hexToBinary(hexidecimal)
    return binaryString

def base64ToHex(b64String):
    hexidecimal = b64decode(b64String.encode()).hex()
    return hexidecimal

def base64ToText(b64String):
    text = b64decode(b64String).decode('utf-8')
    return text

#testing = "01110100011001010111001101110100011010010110111001100111"
testing = 'cafebabe'
print(binaryToB64(testing))