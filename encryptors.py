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
