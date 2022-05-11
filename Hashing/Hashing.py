from Crypto.Hash import SHA256
import datetime as t
import os
from matplotlib import pyplot as plt


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

def task1_c(hashWidth):
    shaHash = SHA256.new()
    attemptedHashes = {}
    currentNum = 0
    startTime = t.datetime.now()

    bitmask = int('1'*hashWidth, 2)

    while True:
        shaHash.update(bytes(currentNum))
        # currentHash = shaHash.hexdigest()[0:hashWidth]
        currentHash = int.from_bytes(shaHash.digest(), 'little')
        currentHash = currentHash & bitmask

        if currentHash not in attemptedHashes:
            attemptedHashes[currentHash] = currentNum
        elif attemptedHashes[currentHash] != currentNum:
            print(f'{currentNum} and {attemptedHashes[currentHash]} both share the first {hashWidth} bits: {currentHash}')
            break
        
        currentNum += 1

    endTime = t.datetime.now()
    print(f'Time elapsed = {endTime - startTime}')
    print(f'Number of inputs tried = {currentNum}')
    print(f'Datapoint for graph: ({hashWidth}, {endTime - startTime})')
    return hashWidth, endTime - startTime, currentNum

def task1_c_generateData():
    x = []
    y = []
    z = []
    for i in range(8, 50):
        print(f'Digest Size = {i}')
        a = task1_c(i)
        x.append(a[0])
        y.append(a[1].total_seconds())
        z.append(a[2])
    plt.subplot(1, 2 ,1)
    plt.plot(x, y, '-')
    plt.subplot(1, 2, 2)
    plt.plot(x, z, '-')
    plt.show()

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
