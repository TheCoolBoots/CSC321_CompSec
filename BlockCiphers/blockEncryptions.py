import random
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


blockSizeBytes = 16


def padByteArray(array):
    if (len(array) % blockSizeBytes != 0):
        newLen = (len(array) // blockSizeBytes + 1) * blockSizeBytes
        addedBytes = newLen - len(array)
        padding = bytearray(addedBytes.to_bytes(1, 'little')) * addedBytes
        # print(padding)
        # print(array)
        return array + padding
    else:
        return array


def xorByteArray(arr1, arr2):
    if len(arr1) != len(arr2):
        print("ERROR: arrays are not of equal length")
        return
    newArray = bytearray()
    for i in range(len(arr1)):
        newArray.append(arr1[i] ^ arr2[i])
    return newArray


def ECBEncryptBinary(key, plaintext):
    if len(key) != blockSizeBytes:
        print("ERROR: key is not of length " + str(blockSizeBytes))
        return

    plaintext = padByteArray(plaintext)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    cipherText = bytearray()

    for i in range(0, len(plaintext) // blockSizeBytes):
        cipherTextBuf = encryptor.update(plaintext[i * blockSizeBytes: i * blockSizeBytes + blockSizeBytes])
        cipherText += cipherTextBuf

    return cipherText


def CBCEncryptBinary(key, initVector, plaintext):
    if len(key) != blockSizeBytes:
        print("ERROR: key is not of length " + blockSizeBytes)
        return
    if len(initVector) != blockSizeBytes:
        print("ERROR: key is not of length " + blockSizeBytes)
        return

    plaintext = padByteArray(plaintext)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    cipherText = bytearray()
    lastBlock = bytearray(initVector)

    for i in range(0, len(plaintext) // blockSizeBytes):
        prePlainText = plaintext[i * blockSizeBytes: i * blockSizeBytes + blockSizeBytes]
        preCipherText = xorByteArray(prePlainText, lastBlock)
        cipherTextBuf = encryptor.update(preCipherText)
        lastBlock = cipherTextBuf
        cipherText += lastBlock

    return cipherText


def ECBDecryptBinary(key, cipherText):
    if len(key) != blockSizeBytes:
        print("ERROR: key is not of length " + blockSizeBytes)
        return

    plaintext = bytearray()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    for i in range(0, len(cipherText) // blockSizeBytes):
        plaintext += decryptor.update(cipherText[i * blockSizeBytes: i * blockSizeBytes + blockSizeBytes])

    return plaintext


def CBCDecryptBinary(key, initVector, cipherText):
    if len(key) != blockSizeBytes:
        print("ERROR: key is not of length " + blockSizeBytes)
        return
    if len(initVector) != blockSizeBytes:
        print("ERROR: key is not of length " + blockSizeBytes)
        return

    plainText = bytearray()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    lastBlock = initVector

    for i in range(0, len(cipherText) // blockSizeBytes):
        prePlaintext = decryptor.update(cipherText[i * blockSizeBytes: i * blockSizeBytes + blockSizeBytes])
        newPlaintext = xorByteArray(prePlaintext, lastBlock)
        lastBlock = cipherText[i * blockSizeBytes: i * blockSizeBytes + blockSizeBytes]
        plainText += newPlaintext

    return plainText


def encryptBMP(filepath):
    key1 = os.urandom(blockSizeBytes)
    key2 = os.urandom(blockSizeBytes)
    initVector = os.urandom(blockSizeBytes)

    with open(filepath, 'rb') as ecbInput:
        txt = bytearray(ecbInput.read())

    # print(txt)
    header = txt[0:54]
    ecbEncryptedMessage = ECBEncryptBinary(key1, txt)
    ecbEncryptedMessage = header + ecbEncryptedMessage[54:]

    with open('ECB.bmp', 'wb+') as file:
        file.write(ecbEncryptedMessage)

    # print(txt)
    header = txt[0:54]
    cbcEncryptedMessage = CBCEncryptBinary(key2, initVector, txt)
    cbcEncryptedMessage = header + cbcEncryptedMessage[54:]

    with open('CBC.bmp', 'wb+') as file:
        file.write(cbcEncryptedMessage)


def encryptFile(filepath):
    key1 = os.urandom(blockSizeBytes)
    key2 = os.urandom(blockSizeBytes)
    initVector = os.urandom(blockSizeBytes)

    with open(filepath, 'rb') as ecbInput:
        txt = bytearray(ecbInput.read())

    # print(txt)
    header = txt[0:54]
    ecbEncryptedMessage = ECBEncryptBinary(key1, txt)
    ecbEncryptedMessage = header + ecbEncryptedMessage[54:]

    with open('ECB.bmp', 'wb+') as file:
        file.write(ecbEncryptedMessage)

    # print(txt)
    header = txt[0:54]
    cbcEncryptedMessage = CBCEncryptBinary(key2, initVector, txt)
    cbcEncryptedMessage = header + cbcEncryptedMessage[54:]

    with open('CBC.bmp', 'wb+') as file:
        file.write(cbcEncryptedMessage)

    ecbDecryptedMessage = ECBDecryptBinary(key1, ecbEncryptedMessage)
    cbcDecryptedMessage = CBCDecryptBinary(key2, initVector, cbcEncryptedMessage)

    with open('ECBdec.bmp', 'wb+') as file:
        file.write(header + ecbDecryptedMessage[54:])

    with open('CBCdec.bmp', 'wb+') as file:
        file.write(header + cbcDecryptedMessage[54:])


encryptFile('cp-logo.bmp')
# encryptBMP('cp-logo.bmp')
