from Cryptodome.PublicKey import RSA

def generateRSAKeyPair(keySize):
    key = RSA.generate(keySize)
    privateKey = key.export_key()
    publicKey = key.publickey().export_key()
    p = key.p
    q = key.q
    n = key.n
    e = key.e
    d = key.d

    return publicKey, privateKey, p, q, n, e, d
