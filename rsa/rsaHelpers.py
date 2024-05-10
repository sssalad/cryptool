'''from Crypto.PublicKey import RSA

def getNFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.n

def getEFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.e

def getDFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.d

def getAllValuesFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)'''

from cryptography.hazmat.primitives import serialization
import os

def getNumbersFromPEMRSAKey(rsaKey):
    if "-----BEGIN PUBLIC KEY-----" in rsaKey:
        publicKey = serialization.load_pem_public_key(bytes(rsaKey, 'utf-8'))
        numbers = publicKey.public_numbers()
        return {'n': numbers.n, 'e': numbers.e}
    elif "-----BEGIN RSA PRIVATE KEY-----" in rsaKey:
        privateKey = serialization.load_pem_private_key(bytes(rsaKey, 'utf-8'), password=None)
        privateNumbers = privateKey.private_numbers()
        publicNumbers = privateNumbers.public_numbers

        return {'n': publicNumbers.n, 'e': publicNumbers.e, 'd': privateNumbers.d}