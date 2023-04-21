from converters import *

def convertMain(convertFrom, convertTo, input):
    result = ''
    if convertFrom == 'Binary':
        if convertTo == 'Binary':
            result = input
        elif convertTo == 'Decimal':
            result = binaryToDecimal(input)
        elif convertTo == 'Hexidecimal':
            result = binaryToHex(input)
        elif convertTo == 'Base64':
            result = binaryToB64(input)
        elif convertTo == 'Text':
            result = binaryToText(input)
    elif convertFrom == 'Decimal':
        if convertTo == 'Binary':
            result = decimalToBinary(input)
        elif convertTo == 'Decimal':
            result = input
        elif convertTo == 'Hexidecimal':
            result = decimalToHexidecimal(input)
        elif convertTo == 'Base64':
            result = decimalToBase64(input)
        elif convertTo == 'Text':
            result = decimalToText(input)
    elif convertFrom == 'Hexidecimal':
        if convertTo == 'Binary':
            result = hexToBinary(input)
        elif convertTo == 'Decimal':
            result = hexToDecimal(input)
        elif convertTo == 'Hexidecimal':
            result = input
        elif convertTo == 'Base64':
            result = hexToB64(input)
        elif convertTo == 'Text':
            result = hexToText(input)
    elif convertFrom == 'Base64':
        if convertTo == 'Binary':
            result = base64ToBinary(input)
        elif convertTo == 'Decimal':
            result = base64ToDecimal(input)
        elif convertTo == 'Hexidecimal':
            result = base64ToHex(input)
        elif convertTo == 'Base64':
            result = input
        elif convertTo == 'Text':
            result = base64ToText(input)
    elif convertFrom == 'Text':
        if convertTo == 'Binary':
            result = textToBinary(input)
        elif convertTo == 'Decimal':
            result = textToDecimal(input)
        elif convertTo == 'Hexidecimal':
            result = textToHex(input)
        elif convertTo == 'Base64':
            result = textToB64(input)
        elif convertTo == 'Text':
            result = input
    return result