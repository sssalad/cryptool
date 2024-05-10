import string
from converters import *

# this only works assuming everything is lowercase right now
# also assumes alphabet is ONLY alphabetical characters
    # issues with cases. Find letter in alphabet when ignoring case, vs. caring about case
# default alphabet = testAlphabet = string.ascii_lowercase
def caesarCipherMain(input, alphabet, shift, maintainCase, maintainForeignChar, shiftNumbers):
    alphabet = list(alphabet)
    output = ''
    
    for inputChar in input:
        #Check if number and shift accordingly
        if inputChar.isnumeric():
            if shiftNumbers:
                output += str((int(inputChar) + shift) % 10)
            else:
                output += inputChar
        elif inputChar.isalpha():
            if maintainCase:
                isUpper = inputChar.isupper()
                inputChar = inputChar.lower()
                alphabetIndex = alphabet.index(inputChar)
                shuffledIndex = (alphabetIndex + shift) % len(alphabet)
                if isUpper:
                    output += alphabet[shuffledIndex].upper()
                else:
                    output += alphabet[shuffledIndex]
            else:
                inputChar = inputChar.lower()
                alphabetIndex = alphabet.index(inputChar)
                shuffledIndex = (alphabetIndex + shift) % len(alphabet)
                output += alphabet[shuffledIndex]
        # if not number or letter...
        else:
            if maintainForeignChar:
                output += inputChar
    return output

def XORMain(input, inputType, outputType, key, keyType):
    #convert everything to binary
    inputBinary = ''
    keyBinary = ''
    outputBinary = ''
    output = ''

    if inputType == 'Binary':
        inputBinary = input 
    elif inputType == 'Decimal':
        inputBinary = decimalToBinary(input)
    elif inputType == 'Hexidecimal':
        inputBinary = hexToBinary(input)
    elif inputType == 'Base64':
        inputBinary = base64ToBinary(input)
    elif inputType == 'Text':
        inputBinary = textToBinary(input)

    if keyType == 'Binary':
        keyBinary = key 
    elif keyType == 'Decimal':
        keyBinary = decimalToBinary(key)
    elif keyType == 'Hexidecimal':
        keyBinary = hexToBinary(key)
    elif keyType == 'Base64':
        keyBinary = base64ToBinary(key)
    elif keyType == 'Text':
        keyBinary = textToBinary(key)
    
    #do xor
    for i in range(len(inputBinary)):
        if (inputBinary[i] != keyBinary[i % len(keyBinary)]):
            outputBinary += '1'
        else:
            outputBinary += '0'

    #convert output to proper format
    if outputType == 'Binary':
        output = outputBinary 
    elif outputType == 'Decimal':
        output = binaryToDecimal(outputBinary)
    elif outputType == 'Hexidecimal':
        output = binaryToHex(outputBinary)
    elif outputType == 'Base64':
        output = binaryToB64(outputBinary)
    elif outputType == 'Text':
        output = binaryToText(outputBinary)

    return output