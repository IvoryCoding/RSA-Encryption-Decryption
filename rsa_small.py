#### IMPORTS ####
from math import gcd
import random

#### FUNCTIONS ####
def RSA(p: int, q: int):
    n = p * q

    t = (p - 1) * (q - 1)

    # selecting public key, e
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    
    # selecting private key, d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1

    # Return useful data
    return e, n, d

def encrypt_msg(message, e, n):
    ct = (message ** e) % n
    return ct

def decrypt_msg(ct, d, n):
    mes = (ct ** d) % n
    return mes

#### CODE ####
# RSA(p=53, q=59)
# p=53, q=59

# Example of multi character text
user_msg = "Hello my name is RAVEN."
# user_msg = "L"

user_msg = [ord(ch) for ch in user_msg]

e, n ,d = RSA(p=53, q=59)

ct = []
msg = []

for ch in user_msg:
    ct.append(encrypt_msg(ch, e, n))

for ch in ct:
    msg.append(decrypt_msg(ch, d, n))

print(f'\nEncrypted: {ct}')
print(f'Encrypted Message, as cipher:\n {"".join(str(i) for i in ct)}') # Combine each number into a long string
print(f'\nDecrypted: {msg}')
print(f'Decrypted Message, as plain text:\n {"".join(chr(ch) for ch in msg)}')

print(f'\nPublic Key: {e, n}')
print(f'Private Key: {d, n}\n')