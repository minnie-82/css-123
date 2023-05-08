import random
import math

def is_prime(n):
    
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def generate_key_pair(p, q):
    
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal.')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    gcd = math.gcd(e, phi)
    while gcd != 1:
        e = random.randrange(1, phi)
        gcd = math.gcd(e, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    
    key, n = public_key
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
   
    key, n = private_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

# Example usage
p = 17
q = 19
public_key, private_key = generate_key_pair(p, q)

message = "Hello, World!"
encrypted_message = encrypt(public_key, message)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)