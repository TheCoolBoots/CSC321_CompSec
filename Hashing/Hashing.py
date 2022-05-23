from Crypto.Hash import SHA256
import datetime as t
import os
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

def task1_c(hashWidth):
    shaHash = SHA256.new()

    attemptedHashes = {}
    currentNum = 0
    startTime = t.datetime.now()

    bitmask = int('1'*hashWidth, 2)

    while True:
        shaHash.new()
        # shaHash.update(bytes(currentNum))
        currentHash = shaHash.hexdigest()[0:hashWidth]
        currentHash = int.from_bytes(shaHash.digest(), 'little')
        currentHash = currentHash & bitmask

        if currentHash not in attemptedHashes:
            attemptedHashes[currentHash] = currentNum
        elif attemptedHashes[currentHash] != currentNum:
            # print(f'{currentNum} and {attemptedHashes[currentHash]} both share the first {hashWidth} bits: {currentHash}')
            break
        
        currentNum += 1

    endTime = t.datetime.now()
    # print(f'Time elapsed = {endTime - startTime}')
    print(f'Number of inputs tried = {currentNum}')
    print(f'Datapoint for graph: ({hashWidth}, {endTime - startTime})')
    return hashWidth, endTime - startTime, currentNum

def task1_c_generateData():
    x = []
    y = []
    z = []
    for i in range(8, 50, 2):
        print(f'Digest Size = {i}')
        a = task1_c(i)
        # x.append(a[0])
        # y.append(a[1].total_seconds())
        # z.append(a[2])
    # plt.subplot(1, 2 ,1)
    # plt.plot(x, y, '-')
    # plt.subplot(1, 2, 2)
    # plt.plot(x, z, '-')
    # plt.show()

def task1_c(hashBitWidth):
    attemptedHashes = {}
    currentNum = 0
    startTime = t.datetime.now()
    while True:
        shaHash = hashlib.sha256(str(currentNum).encode('utf-8'))
        currentHash = int.from_bytes(shaHash.digest(),'big') & (2**hashBitWidth - 1)
        # print(bin(2**hashBitWidth - 1))
        # print(hex(currentHash))
        if currentHash not in attemptedHashes:
            attemptedHashes[currentHash] = currentNum
        elif attemptedHashes[currentHash] != currentNum:
            print(f'{currentNum} and {attemptedHashes[currentHash]} both share the first {hashBitWidth} bits: {bin(currentHash)}')
            break
        currentNum += 1
        endTime = t.datetime.now()
    print(f'Time elapsed = {endTime - startTime}')
    print(f'Number of inputs tried = {currentNum}')
    print(f'Datapoint for graph: ({currentHash}, {endTime - startTime})')


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

"""
8, 0:00:00.001136
9, 0:00:00.000238
10, 0:00:00.000377
11, 0:00:00.000335
12, 0:00:00.000289
13, 0:00:00.000322
14, 0:00:00.002197
15, 0:00:00.002100
16, 0:00:00.002393
17, 0:00:00.001805
18, 0:00:00.005223
19, 0:00:00.005636
20, 0:00:00.015409
21, 0:00:00.042417
22, 0:00:00.042848
23, 0:00:00.055597
24, 0:00:00.187713
25, 0:00:00.177291
26, 0:00:00.176393
27, 0:00:00.176875
28, 0:00:01.501429
29, 0:00:01.996534
30, 0:00:01.998325
31, 0:00:21.199042
32, 0:00:20.461063
33, 0:00:20.763102
34, 0:01:19.221674
35, 0:02:46.703342
36, 0:17:23.859476
37, 0:16:42.442957
38, 1:22:16.198924
"""
'''
Digest Size = 8
15 and 1 both share the first 8 bits: 110 
Time elapsed = 0:00:00.000999
Number of inputs tried = 15
Digest Size = 9
32 and 31 both share the first 9 bits: 392
Time elapsed = 0:00:00
Number of inputs tried = 32
Digest Size = 10
32 and 31 both share the first 10 bits: 392
Time elapsed = 0:00:00.001000
Number of inputs tried = 32
Digest Size = 11
32 and 31 both share the first 11 bits: 392
Time elapsed = 0:00:00
Number of inputs tried = 32
Digest Size = 12
32 and 31 both share the first 12 bits: 2440
Time elapsed = 0:00:00.001001
Number of inputs tried = 32
Digest Size = 13
32 and 31 both share the first 13 bits: 2440
Time elapsed = 0:00:00
Number of inputs tried = 32
Digest Size = 14
183 and 159 both share the first 14 bits: 3553
Time elapsed = 0:00:00
Number of inputs tried = 183
Digest Size = 15
183 and 159 both share the first 15 bits: 19937
Time elapsed = 0:00:00.001001
Number of inputs tried = 183
Digest Size = 16
183 and 159 both share the first 16 bits: 19937
Time elapsed = 0:00:00.000999
Number of inputs tried = 183
Digest Size = 17
183 and 159 both share the first 17 bits: 85473
Time elapsed = 0:00:00.000999
Number of inputs tried = 183
Digest Size = 18
505 and 310 both share the first 18 bits: 51114
Time elapsed = 0:00:00.001997
Number of inputs tried = 505
Digest Size = 19
505 and 310 both share the first 19 bits: 51114
Time elapsed = 0:00:00.003002
Number of inputs tried = 505
Digest Size = 20
1168 and 1137 both share the first 20 bits: 1016156
Time elapsed = 0:00:00.007685
Number of inputs tried = 1168
Digest Size = 21
2447 and 241 both share the first 21 bits: 688505
Time elapsed = 0:00:00.019594
Number of inputs tried = 2447
Digest Size = 22
2447 and 241 both share the first 22 bits: 2785657
Time elapsed = 0:00:00.021000
Number of inputs tried = 2447
Digest Size = 23
2965 and 1727 both share the first 23 bits: 2596205
Time elapsed = 0:00:00.025999
Number of inputs tried = 2965
Digest Size = 24
7450 and 7325 both share the first 24 bits: 796297
Time elapsed = 0:00:00.128124
Number of inputs tried = 7450
Digest Size = 25
7450 and 7325 both share the first 25 bits: 17573513
Time elapsed = 0:00:00.132312
Number of inputs tried = 7450
Digest Size = 26
7450 and 7325 both share the first 26 bits: 51127945
Time elapsed = 0:00:00.121695
Number of inputs tried = 7450
Digest Size = 27
7450 and 7325 both share the first 27 bits: 118236809
Time elapsed = 0:00:00.121791
Number of inputs tried = 7450
Digest Size = 28
25189 and 19558 both share the first 28 bits: 258849779
Time elapsed = 0:00:01.190425
Number of inputs tried = 25189
Digest Size = 29
29340 and 9883 both share the first 29 bits: 86256205
Time elapsed = 0:00:01.616811
Number of inputs tried = 29340
Digest Size = 30
29340 and 9883 both share the first 30 bits: 86256205
Time elapsed = 0:00:01.605000
Number of inputs tried = 29340
Digest Size = 31
95640 and 71132 both share the first 31 bits: 1112123858
Time elapsed = 0:00:16.363322
Number of inputs tried = 95640
Digest Size = 32
95640 and 71132 both share the first 32 bits: 1112123858
Time elapsed = 0:00:16.496624
Number of inputs tried = 95640
Digest Size = 33
95640 and 71132 both share the first 33 bits: 5407091154
Time elapsed = 0:00:16.351938
Number of inputs tried = 95640
Digest Size = 34
187195 and 148972 both share the first 34 bits: 14802283747
Time elapsed = 0:01:01.987727
Number of inputs tried = 187195
Digest Size = 35
277080 and 195216 both share the first 35 bits: 30837019020
Time elapsed = 0:02:14.736514
Number of inputs tried = 277080
Digest Size = 36
688973 and 82586 both share the first 36 bits: 60523568804
Time elapsed = 0:13:48.161403
Number of inputs tried = 688973
Digest Size = 37
688973 and 82586 both share the first 37 bits: 60523568804
Time elapsed = 0:13:47.520263
Number of inputs tried = 688973
Digest Size = 38
1395304 and 844406 both share the first 38 bits: 180182528605
Time elapsed = 0:57:54.391910
Number of inputs tried = 1395304
Digest Size = 39
1438595 and 1138778 both share the first 39 bits: 251932628062
Time elapsed = 1:01:40.180083
Number of inputs tried = 1438595
Digest Size = 40
2213850 and 1552115 both share the first 40 bits: 304073305611
Time elapsed = 2:28:23.115429
Number of inputs tried = 2213850
Digest Size = 41
2213850 and 1552115 both share the first 41 bits: 304073305611
Time elapsed = 2:28:11.793961
Number of inputs tried = 2213850
Digest Size = 42
2213850 and 1552115 both share the first 42 bits: 2503096561163
Time elapsed = 2:28:06.518409
Number of inputs tried = 2213850
Digest Size = 43
2877245 and 2349620 both share the first 43 bits: 4018358257482
Time elapsed = 4:11:02.310583
Number of inputs tried = 2877245
Digest Size = 44
'''