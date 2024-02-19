from base64 import b64encode, b64decode

########################
##### Binary to... #####
########################
def binaryToText(binaryString):
    dec = int(binaryString, 2)
    try:
        text = dec.to_bytes((dec.bit_length() + 7) // 8, 'big').decode()
        return str(text).toUtf8()
    except:
        return "[Non-ASCII Result :(]"

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
    text = bytes.fromhex(hexString).decode('utf-8')
    return str(text)

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
    b64 = b64encode(text.encode('ascii'))
    #b64 = str(b64)
    #return b64[2:(len(b64) - 1)]
    return b64.decode('ascii')

def textToDecimal(text):
    dec = ''
    for character in text:
        dec += ord(character)
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
    return '{0:08b}'.format(decimal)

def decimalToHexidecimal(decimal):
    return hex(int(decimal))

def decimalToBase64(decimal):
    return b64encode(bytes(str(decimal), 'ascii'))

# Assuming there is a string of decimal numbers separated by spaces
def decimalToText(decimal):
    result = ''
    decList = decimal.split()
    for number in decList:
        result += ord(int(number))
    return result