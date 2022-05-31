from Crypto.Hash import SHA256
import datetime as t
import os
import hashlib
# from matplotlib import pyplot as plt


def task1_a():
    shaHash = SHA256.new()  
    for i in range(10):
        shaHash.update(os.urandom(16))
        print(shaHash.hexdigest())

def task1_b():
    shaHash = SHA256.new()
    for i in range(10):
        byteArray1 = os.urandom(16)
        byteArray2 = byteArray1[0:15] + bytes((byteArray1[15] ^ 1))
        print('=====================')
        shaHash.update(byteArray1)
        print(shaHash.hexdigest())
        shaHash.update(byteArray2)
        print(shaHash.hexdigest())

def task1_c_generateData():
    for i in range(8, 52, 2):
        print(f'Digest Size = {i}')
        a = task1_c(i)

def task1_c(hashBitWidth):
    attemptedHashes = {}
    currentNum = 0
    startTime = t.datetime.now()
    while True:
        shaHash = hashlib.sha256(str(currentNum).encode('utf-8'))
        currentHash = int.from_bytes(shaHash.digest(),'big') & (2**hashBitWidth - 1)
        if currentHash not in attemptedHashes:
            attemptedHashes[currentHash] = currentNum
        elif attemptedHashes[currentHash] != currentNum:
            break
        currentNum += 1
        endTime = t.datetime.now()
    print(f'{currentNum}\t{endTime - startTime}')


def importUserHashes(filepath):
    with open(filepath, 'rb') as inputFile:
        contents = inputFile.readlines()
    userHashes = {}
    for user in contents:
        name = user[0:user.index(b':')]
        saltHash = user[user.index(b':') + 1:]
        userHashes[name] = {'salt':saltHash[0:29], 'hash':saltHash[29:], 'saltHash':saltHash}
    return userHashes


task1_c_generateData()

# task1_a()
# task1_b()
