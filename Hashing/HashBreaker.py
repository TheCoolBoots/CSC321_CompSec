from nltk.corpus import words
import bcrypt

Bilbo = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq" # = welcome
Gandalf = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC" # = wizard
Thorin = b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q" # = diamond
Fili = b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm" # = desire
Kili = b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im" # = ossify
Balin = b"$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom" # hangout
Dwalin = b"$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be" # drossy
Oin = b"$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK" # ispaghul
Gloin = b"$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q" # oversave
Dori = b"$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq" # indoxylic
Nori = b"$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12" # swagsman
Ori = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O" # airway
Bifur = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK" # corrosible
Bofur = b"$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O" # libellate
Durin = b"$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay" # purrone
hashes = [Balin, Dwalin, Oin, Gloin, Dori, Nori, Ori, Bifur, Bofur, Durin]

filteredWords = []
for word in words.words():
    if len(word) >= 6 and len(word) <= 10:
        filteredWords.append(word.encode('utf-8'))
        print(len(filteredWords))

    with open('foundPasswords.txt', 'w') as outFile:
        for userID, userHash in enumerate(hashes):
            checked = 0
            found = False
            for word in filteredWords:
                if bcrypt.checkpw(word, userHash):
                    print(word)
                    outFile.write(word.decode('utf-8') + '\n')
                    found = True
                    break
                checked += 1
                if checked % 10000 == 0:
                    print(f'checked {checked} hashes for user {userID}')
            if not found:
                print(f'password not found for user {userID}')