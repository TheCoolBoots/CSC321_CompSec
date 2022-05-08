from Crypto.Util import number
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


def RSA_encrypt(message, e, n):
    m_ord = [ord(c) for c in message]
    ciphertext = [m ** e % n for m in m_ord]

    return ciphertext


def RSA_decrypt(ciphertext, e, n, tot_n):
    d = modinv(e, tot_n)
    decryptedtext = [chr(c ** d % n) for c in ciphertext]
    m_conv = ''.join(decryptedtext)

    return m_conv


def RSA_decrypt_mal(ciphertext, e, n, t):
    d = modinv(e, tot_n)
    decryptedtext = [chr(c ** d % n) for c in ciphertext]
    m_conv = ''.join(decryptedtext)

    return m_conv


# Source = https://algorithmist.com/wiki/Modular_inverse
# Iterative Algorithm (xgcd)
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y


def modinv(a, m):
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def padString(string):
    if(len(string) % 16 != 0):
        newLen = (len(string)//16 + 1) * 16
        addedBytes = newLen - len(string)
        padding = chr(newLen) * addedBytes
        return string + padding
    else:
        return string


def textbookRSA(e, prime_len):
    p = number.getPrime(prime_len)
    q = number.getPrime(prime_len)

    n = p * q
    tot_n = (p - 1) * (q - 1)

    # begin encryption
    message = "Hi Alice"
    ciphertext = RSA_encrypt(message, e, n)
    # print(ciphertext)

    # begin decryption
    plaintext = RSA_decrypt(ciphertext, e, n, tot_n)
    print(plaintext)


def malloryRSA(e, prime_len):
    p = number.getPrime(prime_len)
    q = number.getPrime(prime_len)

    n = p * q
    tot_n = (p - 1) * (q - 1)

    # begin encryption from Bob
    bob_message = "Hi Alice"
    bob_ciphertext = RSA_encrypt(bob_message, e, n)
    # print(bob_ciphertext)

    # mallory interception
    mal_ciphertext = RSA_encrypt(chr(0), e, n)
    # print(mal_ciphertext)

    # begin decryption and encryption from Alice
    plaintext = RSA_decrypt(mal_ciphertext, e, n, tot_n)
    # print(plaintext)
    k = SHA256.new(plaintext.encode('utf-8'))

    alice_message = "Hi Bob"
    cipher = AES.new(k.digest(), AES.MODE_CBC)
    init_vector = cipher.iv
    alice_ciphertext = cipher.encrypt(pad(alice_message.encode('utf-8'), 16))
    # print(alice_ciphertext)

    # mallory interception
    mal_k = SHA256.new(chr(0).encode('utf-8'))
    mal_cipher = AES.new(mal_k.digest(), AES.MODE_CBC, iv=init_vector)
    dec_message = unpad(mal_cipher.decrypt(alice_ciphertext), 16).decode('utf-8')
    print(dec_message)


def main():
    e = 65537
    prime_len = 8

    print("Textbook")
    textbookRSA(e, prime_len)

    print("\n\nMallory")
    malloryRSA(e, prime_len)


if __name__ == "__main__":
    main()