import unittest

from encodeMain import encodeMain

class EncodeNotByByteNoLeadingZeros(unittest.TestCase):
    binaryResult = '0111010001101000011010010111001100100000011010010011010100100000011000010010000001110100001100110111001101110100001000000110110101100101011100110111001101100001011001110110010100100001'
    decimalResult = '11149657805798639286321096005603228193703661170091058465'
    hexResult = '7468697320693520612074337374206d65737361676521'
    base64Result = 'dGhpcyBpNSBhIHQzc3QgbWVzc2FnZSE='
    textResult = 'this i5 a t3st message!'

    byBytes = False
    leadingZeros = False

    # Binary to...
    def test_binToBin(self):
        result = encodeMain(self.binaryResult, 'Binary', 'Binary', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.binaryResult)

    def test_binToDec(self):
        result = encodeMain(self.binaryResult, 'Binary', 'Decimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.decimalResult)

    def test_binToHex(self):
        result = encodeMain(self.binaryResult, 'Binary', 'Hexidecimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.hexResult)

    def test_binToBase64(self):
        result = encodeMain(self.binaryResult, 'Binary', 'Base64', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.base64Result)

    def test_binToText(self):
        result = encodeMain(self.binaryResult, 'Binary', 'Text', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.textResult)

    ################################################################################
    # Decimal to...
    def test_decToBin(self):
        result = encodeMain(self.decimalResult, 'Decimal', 'Binary', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.binaryResult)

    def test_decToDec(self):
        result = encodeMain(self.decimalResult, 'Decimal', 'Decimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.decimalResult)

    def test_decToHex(self):
        result = encodeMain(self.decimalResult, 'Decimal', 'Hexidecimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.hexResult)

    def test_decToBase64(self):
        result = encodeMain(self.decimalResult, 'Decimal', 'Base64', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.base64Result)

    def test_decToText(self):
        result = encodeMain(self.decimalResult, 'Decimal', 'Text', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.textResult)

    ################################################################################
    # Hex to...
    def test_hexToBin(self):
        result = encodeMain(self.hexResult, 'Hexidecimal', 'Binary', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.binaryResult)

    def test_hexToDec(self):
        result = encodeMain(self.hexResult, 'Hexidecimal', 'Decimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.decimalResult)

    def test_hexToHex(self):
        result = encodeMain(self.hexResult, 'Hexidecimal', 'Hexidecimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.hexResult)

    def test_hexToBase64(self):
        result = encodeMain(self.hexResult, 'Hexidecimal', 'Base64', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.base64Result)

    def test_hexToText(self):
        result = encodeMain(self.hexResult, 'Hexidecimal', 'Text', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.textResult)

    ################################################################################
    # Base64 to...
    def test_b64ToBin(self):
        result = encodeMain(self.base64Result, 'Base64', 'Binary', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.binaryResult)

    def test_b64ToDec(self):
        result = encodeMain(self.base64Result, 'Base64', 'Decimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.decimalResult)

    def test_b64ToHex(self):
        result = encodeMain(self.base64Result, 'Base64', 'Hexidecimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.hexResult)

    def test_b64ToBase64(self):
        result = encodeMain(self.base64Result, 'Base64', 'Base64', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.base64Result)

    def test_b64ToText(self):
        result = encodeMain(self.base64Result, 'Base64', 'Text', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.textResult)

    ################################################################################
    # Text to...
    def test_textToBin(self):
        result = encodeMain(self.base64Result, 'Base64', 'Binary', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.binaryResult)

    def test_textToDec(self):
        result = encodeMain(self.base64Result, 'Base64', 'Decimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.decimalResult)

    def test_textToHex(self):
        result = encodeMain(self.base64Result, 'Base64', 'Hexidecimal', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.hexResult)

    def test_textToBase64(self):
        result = encodeMain(self.base64Result, 'Base64', 'Base64', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.base64Result)

    def test_textToText(self):
        result = encodeMain(self.base64Result, 'Base64', 'Text', self.byBytes, self.leadingZeros)
        self.assertEqual(result, self.textResult)


if __name__ == '__main__':
    unittest.main()