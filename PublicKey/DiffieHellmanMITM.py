
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import random

blockSizeBytes = 16

def padByteArray(array):
    if(len(array) % blockSizeBytes != 0):
        newLen = (len(array)//blockSizeBytes + 1) * blockSizeBytes
        addedBytes = newLen - len(array)
        padding = bytearray(addedBytes.to_bytes(1, 'little')) * addedBytes
        # print(padding)
        # print(array)
        return array + padding
    else:
        return array


# public key (large prime number)
p = 37

# generator (large any number)
g = p

# private keys
a = random.randint(0, p)
b = random.randint(0, p)

# mallory's private key
m = random.randint(0, p)

print(a,b)

# Alice
A = (g ** a) % p

# Bob
B = (g ** b) % p

print(A,B)

# Alice sends A over the network
# Mallory intercepts A and changes A to = p
A = p

# Bob sends B over the network
# Mallory intercepts B and changes B to = p
B = p

# Alice calculates private combined key with modified B
sa = (B ** a) % p

# Bob calculates private combined key with modified A
sb = (A ** b) % p

# sa, sb will always equal 0
print(sa, sb)

aliceKeyHash = SHA256.new()
aliceKeyHash.update(sa.to_bytes(8, 'big'))

bobKeyHash = SHA256.new()
bobKeyHash.update(sb.to_bytes(8, 'big'))

aliceSend = padByteArray(b'Hello There')

aliceCipher = AES.new(aliceKeyHash.hexdigest()[0:16], AES.MODE_CBC, aliceKeyHash.hexdigest()[16:32])
aliceMessage = aliceCipher.encrypt(aliceSend)

# print(aliceMessage)

bobCipher = AES.new(bobKeyHash.hexdigest()[0:16], AES.MODE_CBC, bobKeyHash.hexdigest()[16:32])
bobRecieved = bobCipher.decrypt(aliceMessage)

print(bobRecieved)


# if A, B = p, shared secret will always be 0, hash will always be SHA256(0)
mallorySecret = 0
malloryKeyHash = SHA256.new()
malloryKeyHash.update(mallorySecret.to_bytes(8, 'big'))
malloryCipher = AES.new(malloryKeyHash.hexdigest()[0:16], AES.MODE_CBC, malloryKeyHash.hexdigest()[16:32])
malloryRecieved = malloryCipher.decrypt(aliceMessage)

print(malloryRecieved)


