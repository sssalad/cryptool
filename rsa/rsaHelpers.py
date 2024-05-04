from Crypto.PublicKey import RSA

def getNFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.n

def getEFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.e

def getDFromASN1(rsaASN):
    key = RSA.importKey(rsaASN)
    return key.d