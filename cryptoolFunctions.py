from converters import *


def getByteSize(convertFrom):
    if convertFrom == 'Binary':
        return 8
    elif convertFrom == 'Decimal':
        return -1 #should throw some kind of error
    elif convertFrom == 'Hexidecimal':
        return 2
    elif convertFrom == 'Base64':
        return -1 #should throw some kind of error
    elif convertFrom == 'Text':
        return 1

def addPadding(input, convertFrom):
    paddedInput = ''
    if convertFrom == 'Binary':
        if (len(input) % 8) == 0:
            paddedInput = input
        else:
            paddedInput = ('0' * (8 - (len(input) % 8))) + input
    elif convertFrom == 'Decimal':
        paddedInput = paddedInput #should throw some kind of error
    elif convertFrom == 'Hexidecimal':
        if (len(input) % 2) == 0:
            paddedInput = input
        else:
            paddedInput = ('0' * (2 - (len(input) % 2))) + input
    elif convertFrom == 'Base64':
        paddedInput = paddedInput #should throw some kind of error
    elif convertFrom == 'Text':
        paddedInput = paddedInput #should throw some kind of error
    
    return paddedInput

# Expects input is already padded
def splitByBytes(paddedInput, convertFrom):
    result = []
    byteSize = getByteSize(convertFrom)

    if len(paddedInput) == byteSize:
        result.append(paddedInput)
    else:
        for i in range(0, len(paddedInput), byteSize):
            result.append(paddedInput[i:i+byteSize])

    return result



def convertMain(convertFrom, convertTo, input, byBytes):
    result = []
    input = input.strip()
    input = addPadding(input, convertFrom)
    if byBytes:
        input = splitByBytes(input, convertFrom)
    else:
        input = [input] 

    if convertFrom == 'Binary':
        if convertTo == 'Binary':
            result = input
        elif convertTo == 'Decimal':
            for item in input:
                result.append(binaryToDecimal(item))
        elif convertTo == 'Hexidecimal':
            for item in input:
                result.append(binaryToHex(item))
        elif convertTo == 'Base64':
            for item in input:
                result.append(binaryToB64(item))
        elif convertTo == 'Text':
            for item in input:
                result.append(binaryToText(item))
    elif convertFrom == 'Decimal':
        if convertTo == 'Binary':
            for item in input:
                result.append(decimalToBinary(item))
        elif convertTo == 'Decimal':
            result = input
        elif convertTo == 'Hexidecimal':
            for item in input:
                result.append(decimalToHexidecimal(item))
        elif convertTo == 'Base64':
            for item in input:
                result.append(decimalToBase64(item))
        elif convertTo == 'Text':
            for item in input:
                result.append(decimalToText(item))
    elif convertFrom == 'Hexidecimal':
        if convertTo == 'Binary':
            for item in input:
                result.append(hexToBinary(item))
        elif convertTo == 'Decimal':
            for item in input:
                result.append(hexToDecimal(item))
        elif convertTo == 'Hexidecimal':
            result = input
        elif convertTo == 'Base64':
            for item in input:
                result.append(hexToB64(item))
        elif convertTo == 'Text':
            for item in input:
                result.append(hexToText(item))
    elif convertFrom == 'Base64':
        if convertTo == 'Binary':
            for item in input:
                result.append(base64ToBinary(item))
        elif convertTo == 'Decimal':
            for item in input:
                result.append(base64ToDecimal(item))
        elif convertTo == 'Hexidecimal':
            for item in input:
                result.append(base64ToHex(item))
        elif convertTo == 'Base64':
            result = input
        elif convertTo == 'Text':
                for item in input:
                    result.append(base64ToText(item))
    elif convertFrom == 'Text':
        if convertTo == 'Binary':
            for item in input:
                result.append(textToBinary(item))
        elif convertTo == 'Decimal':
            for item in input:
                result.append(textToDecimal(item))
        elif convertTo == 'Hexidecimal':
            for item in input:
                result.append(textToHex(item))
        elif convertTo == 'Base64':
            for item in input:
                result.append(textToB64(item))
        elif convertTo == 'Text':
            result = input
    return result