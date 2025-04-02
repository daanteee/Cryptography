import hashlib

#要計算的text
text = b'I love cryptography.'

#計算SHA-3-512 message digest
sha3_512_digest = hashlib.sha3_512(text).hexdigest()

print("SHA-3-512 digest: ", sha3_512_digest)