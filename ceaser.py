def encrypt(message):
    cipher_text = ""
    
    for char in message:
        if char == " ":
            cipher_text += " "
        elif char.isupper():
            cipher_text += chr((ord(char)-62)%26 + 65) 
        elif char.islower():
            cipher_text += chr((ord(char)-94)%26 + 97) 
    
    return cipher_text

def decrypt(cipher_text):
    plain_text = ""
    
    for char in cipher_text:
        if char == " ":
            plain_text += " "
        elif char.isupper():
            plain_text += chr((ord(char)-68)%26 +65)
        elif char.islower():
            plain_text += chr((ord(char)-100)%26 +97)
            
    return plain_text

if __name__ == "__main__":
    message = "Hello World"
    
    cipher_text = encrypt(message)
    plain_text = decrypt(cipher_text)
    
    print("\n Encrypted text: " + cipher_text)
    print("\n Decrypted text: " + plain_text)