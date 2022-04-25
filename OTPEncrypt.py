import random


def xorByteArray(arr1, arr2):
    if len(arr1) != len(arr2):
        print("ERROR: arrays are not of equal length")
        return
    newArray = bytearray()
    for i in range(len(arr1)):
        newArray.append(arr1[i] ^ arr2[i])
    return newArray


def generateRandomByteKey(length):
    return [random.randint(0, 255) for _ in range(length)]


def encryptFile(filepath, keyFilepath, cipherFilepath):
    try:
        plainTextFile = open(filepath, 'rb')
    except IOError:
        print("Could not find inputfile " + filepath)

    plainText = plainTextFile.read()
    randomKey = generateRandomByteKey(len(plainText))
    cipherText = xorByteArray(plainText, randomKey)

    print('Key placed in ' + keyFilepath)
    print('Cipher text placed in ' + cipherFilepath)

    with open("key", "wb+") as key_file:
        key_file.write(randomKey)

    with open("outputs/cipherTxt", "wb+") as cipher_file:
        cipher_file.write(cipherText)
    

def encryptBMP(filepath):
    with open(filepath, 'rb') as file:
        plaintext = file.read()
        originalheader = plaintext[0:54]
        randomkey = generateRandomByteKey(len(plaintext))
        ciphertext = xorByteArray(plaintext, randomkey)
        ciphertext = originalheader + ciphertext[54:]

    with open('outputs/cipherImg.bmp', 'wb+') as cipherfile:
        cipherfile.write(ciphertext)

    return randomkey


def decryptBMP(imgFilepath, bmpKey):
    with open(imgFilepath, mode='rb') as file:
        bmpImg = file.read()

    # header is 54 bytes long, need to preserve them if we are to see the encoded image
    bmpHeader = bmpImg[0:54]
    originalFile = xorByteArray(bmpImg, bmpKey)
    originalFile = bmpHeader + originalFile[54:]

    with open('outputs/original.bmp', 'wb+') as file:
        file.write(originalFile)

def twoTimeEncrypt(file1, file2):
    with open(file1, mode='rb') as file:
        bmpImg1 = file.read()

    with open(file2, mode='rb') as file:
        bmpImg2 = file.read()

    if len(bmpImg1) != len(bmpImg2):
        print("ERROR: images are not same size")
        return
    
    randomKey = generateRandomByteKey(len(bmpImg1))
    header1 = bmpImg1[0:54]
    header2 = bmpImg2[0:54]

    cipher1 = xorByteArray(bmpImg1, randomKey)
    cipher2 = xorByteArray(bmpImg2, randomKey)
    cipher3 = xorByteArray(cipher1, cipher2)

    cipher1 = header1 + cipher1[54:]
    cipher2 = header2 + cipher2[54:]
    cipher3 = header1 + cipher3[54:]

    with open("outputs/cipherImg1.bmp", "wb+") as cipher_file:
        cipher_file.write(cipher1)
    
    with open("outputs/cipherImg2.bmp", "wb+") as cipher_file:
        cipher_file.write(cipher2)

    with open("outputs/cipherImg3.bmp", "wb+") as cipher_file:
        cipher_file.write(cipher3)


encryptedKey = encryptBMP('cp-logo.bmp')
decryptBMP('outputs/cipherImg.bmp', encryptedKey)

doubleEncrypt = twoTimeEncrypt('cp-logo.bmp', 'mustang.bmp')

str1 = b"Darlin dont you go"
str2 = b"and cut your hair!"
str3 = xorByteArray(str1, str2)
print(str3.hex() == '250f164c0a1b54441601015259071449154e')