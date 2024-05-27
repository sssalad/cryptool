# Cryptool

Cryptool is a program intended to provide an all-in-one place to perform basic cryptographic operations. There are many online tools that can do the same things Cryptool does. Cryptool's aim is to put them all together and give the user as much freedom and customization as possible.

## Features
* Converstion to and from:
    * Binary
    * Decimal
    * Hexidecimal
    * Base64
    * Text
* Basic Encryption:
    * Caesar Cipher
    * XOR
* RSA
    * RSA Encryption (Mostly Using the [Cryptography Library](https://github.com/pyca/cryptography))
* Cracking
    * Wiener Attack (Using the [oWiener Library](https://github.com/orisano/owiener))



## Coming (Hopefully) Features
* [Conversion] Octal Conversion
* [Basic Encryption] Vigenere Cipher
* [RSA] RSA Signing
* [RSA] RSA Signature Verification
* [Cracking] Frequency Analyzer 

## Installation 
### Prerequisits
* [Python 3.10.12 or later](https://www.python.org/downloads/)

### Download or Clone this Repository
```
git clone https://github.com/sssalad/cryptool
```

### Install Required Python Libraries
```
cd cryptool
pip install -r requirements.txt
```

### Running Cryptool
```
python cryptool.py
```