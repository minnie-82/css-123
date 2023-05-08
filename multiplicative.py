from sympy import mod_inverse
import math

def multi_cypher_encrypt(plain_text, key):
    cipher_text = ""
    if math.gcd(26,key) == 1:
        for char in plain_text:
            if char == " ":
                cipher_text += " "
            elif char.isupper():
                cipher_text += chr(((ord(char)-65)*key)%26 + 65)
            elif char.islower():
                cipher_text += chr(((ord(char)-97)*key)%26 + 97)
                      
    return cipher_text

def multi_cypher_decrypt(cipher_text, key):
    plain_text = ""
    key_inv=mod_inverse(key, 26)
    for char in cipher_text:
        if char == " ":
                plain_text += " "
        elif char.isupper():
            plain_text += chr(((ord(char)-65)*key_inv)%26 + 65)
        elif char.islower():
            plain_text += chr(((ord(char)-97)*key_inv)%26 + 97)
        
    return plain_text

encrypt_message=multi_cypher_encrypt('Hello World',7)
print(encrypt_message)

decrypt_message=multi_cypher_decrypt(encrypt_message,7)
print(decrypt_message)