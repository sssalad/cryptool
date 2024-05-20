from base64 import b64encode, b64decode

########################
##### Binary to... #####
########################
def binaryToText(binaryString):
    result = ''
    for i in range(0, len(binaryString), 8):
        asciiCode = binaryToDecimal(binaryString[i:(i+8)])
        result += chr(int(asciiCode))
    return result


def binaryToHex(binaryString):
    dec = int(binaryString, 2)
    hexidecimal = hex(dec)
    hexidecimal = hexidecimal[2:]
    return str(hexidecimal)

# https://pythontic.com/containers/bytes/fromhex
def binaryToB64(binaryString):
    hexidecimal = binaryToHex(binaryString)
    if (len(hexidecimal) % 2 == 1):
        hexidecimal = hexidecimal.zfill(len(hexidecimal) + 1)
    b64 = b64encode(bytes.fromhex(hexidecimal)).decode()
    return str(b64)

def binaryToDecimal(binaryString):
    return str(int(binaryString, 2))

#############################
##### Hexidecimal to... #####
#############################
def hexToBinary(hexString):
    binaryString = bin(int(hexString, 16))
    binaryString = binaryString[2:]
    binaryString = binaryString.zfill(len(hexString) * 4)
    return str(binaryString)

def hexToText(hexString):
    result = ''
    for i in range(0, len(hexString), 2):
        asciiCode = hexToDecimal(hexString[i:(i+2)])
        result += chr(int(asciiCode))
    return result
    

def hexToB64(hexString):
    hexidecimal = hexString
    if (len(hexidecimal) % 2 == 1):
        hexidecimal = hexidecimal.zfill(len(hexidecimal) + 1)
    b64 = b64encode(bytes.fromhex(hexidecimal)).decode()
    return str(b64)

def hexToDecimal(hexString):
    return str(int(hexString, 16))

######################
##### Text to... #####
######################
def textToBinary(text):
    binaryString = ' '.join(format(ord(x), 'b') for x in text)
    byteList = binaryString.split()
    finalString = ''
    for byte in byteList:
        finalString += byte.zfill(8) 
    return finalString

def textToHex(text):
    hexidecimal = text.encode("utf-8").hex()
    return hexidecimal

def textToB64(text):
    b64 = b64encode(text.encode("utf-8"))
    return b64.decode("utf-8")

def textToDecimal(text):
    dec = ''
    for character in text:
        dec += str(ord(character))
        dec += ' '
    return dec
    

########################
##### Base64 to... #####
########################
def base64ToBinary(b64String): # one long string, not split by byte
    hexidecimal = b64decode(b64String.encode()).hex()
    binaryString = hexToBinary(hexidecimal)

    if (len(binaryString) % 8 == 0):
        return binaryString 
    else:
        return binaryString.zfill((len(binaryString) + (8 - (len(binaryString) % 8))))

def base64ToHex(b64String):  # one long string, not split by byte
    hexidecimal = b64decode(b64String.encode()).hex()
    return hexidecimal

def base64ToText(b64String):
    text = b64decode(b64String).decode('utf-8')
    return text

def base64ToDecimal(b64String): # does not work
    hexString = base64ToHex(b64String)
    dec = hexToDecimal(hexString)
    return dec

#########################
##### Decimal to... #####
#########################
def decimalToBinary(decimal):
    return bin(int(decimal)).replace("b", "")

def decimalToHexidecimal(decimal):
    return hex(int(decimal)).replace("0x", "")

def decimalToBase64(decimal):
    binary = decimalToBinary(decimal)
    result = binaryToB64(binary)
    return result

def decimalToText(decimal):
    binary = decimalToBinary(decimal)
    result = binaryToText(binary)
    return result