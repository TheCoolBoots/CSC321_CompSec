from blockEncryptions import padByteArray
from blockEncryptions import CBCEncryptBinary
from blockEncryptions import CBCDecryptBinary
import os

numUsers = 456
numSessions = 31337
blockSizeBytes = 16

def urlEncodeString(string:str):
    string = string.replace(';', '%3B')
    string = string.replace('=', '%3D')
    return string

def CDCattack(targetString, encryptedMsg, decryptedMsg):
    newStr = bytearray()
    for i, char in enumerate(targetString.encode()):
        decChar = encryptedMsg[i] ^ decryptedMsg[i+ blockSizeBytes]
        newChar = decChar ^ char
        newStr.append(newChar)
    return newStr + encryptedMsg[len(targetString):]

def submit(userData):
    key = os.urandom(blockSizeBytes)
    iv = os.urandom(blockSizeBytes)
    userData = urlEncodeString(userData)
    userString = "userid="+str(numUsers)+';userdata='+userData+';session-id='+str(numSessions)
    userString = padByteArray(userString.encode())
    cipherText = CBCEncryptBinary(key, iv, userString)

    return (key, iv, cipherText)

def verify(key, iv, cipherText):
    plaintext = CBCDecryptBinary(key, iv, cipherText)
    return b';admin=true;' in plaintext


result = submit("asdf;alksdjf;alkjfasdlfkjf")
decryptedStr = CBCDecryptBinary(result[0], result[1], result[2])
encryptedAttack = CDCattack(";admin=true;", result[2], decryptedStr)
print(verify(result[0], result[1], encryptedAttack))