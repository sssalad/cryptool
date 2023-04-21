from base64 import b64encode, b64decode

########################
##### Binary to... #####
########################
def binaryToText(binaryString):
    dec = int(binaryString, 2)
    text = dec.to_bytes((dec.bit_length() + 7) // 8, 'big').decode()
    return text

def binaryToHex(binaryString): #this does not retain leading 0s
    dec = int(binaryString, 2)
    hexidecimal = hex(dec)
    return hexidecimal[2:]

def binaryToB64(binaryString):
    hexidecimal = binaryToHex(binaryString)
    b64 = b64encode(bytes.fromhex(hexidecimal)).decode() #from hex must have 2 hex bytes per thing, so multiple of 8 binary bits
    #https://pythontic.com/containers/bytes/fromhex
    return b64

def binaryToDecimal(binaryString):
    return int(binaryString, 2)

#############################
##### Hexidecimal to... #####
#############################
def hexToBinary(hexString):
    binaryString = bin(int(hexString, 16))
    return binaryString[2:]

def hexToText(hexString):
    text = bytes.fromhex(hexString).decode('utf-8')
    return text

def hexToB64(hexString):
    b64 = b64encode(bytes.fromhex(hexString)).decode()
    return b64

def hexToDecimal(hexString):
    return int(hexString, 16)

######################
##### Text to... #####
######################
def textToBinary(text):
    binaryString = ' '.join(format(ord(x), 'b') for x in text)
    byteList = binaryString.split()
    finalString = ''
    for byte in byteList:
        finalString += byte.zfill(8) 
        finalString += ' '
    return finalString

def textToHex(text):
    hexidecimal = text.encode("utf-8").hex()
    return hexidecimal

def textToB64(text):
    b64 = b64encode(text.encode('ascii'))
    return b64[2:]

def textToDecimal(text): # this does not work
    num = 0
    for ch in text:
        num = num << 8 + ord(ch)
    return num
    

########################
##### Base64 to... #####
########################
def base64ToBinary(b64String): # one long string, not split by byte
    hexidecimal = b64decode(b64String.encode()).hex()
    binaryString = hexToBinary(hexidecimal)
    
    return binaryString.zfill((len(binaryString) + (8 - (len(binaryString) % 8))))

def base64ToHex(b64String):  # one long string, not split by byte
    hexidecimal = b64decode(b64String.encode()).hex()
    return hexidecimal

def base64ToText(b64String):
    text = b64decode(b64String).decode('utf-8')
    return text

def base64ToDecimal(b64String): # does not work
    return int(b64String, 64)

#########################
##### Decimal to... #####
#########################
def decimalToBinary(decimal):
    return '{0:08b}'.format(decimal)

def decimalToHexidecimal(decimal):
    return hex(decimal)

def decimalToBase64(decimal):
    return b64encode(bytes(str(decimal), 'ascii'))

def decimalToText(decimal):
    return ord(decimal)