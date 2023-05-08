def encrypt(message, key):
    cipher_text = ""
    
    for char in message:
        if char == " ":
            cipher_text += " "
        elif char.isupper():
            cipher_text += chr((ord(char)+ key - 65)%26 + 65) 
        elif char.islower():
            cipher_text += chr((ord(char)+ key - 97)%26 + 97) 
    
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    
    for char in cipher_text:
        if char == " ":
            plain_text += " "
        elif char.isupper():
            plain_text += chr((ord(char)-key - 65)%26 +65)
        elif char.islower():
            plain_text += chr((ord(char)- key - 97)%26 +97)
            
    return plain_text

if __name__ == "__main__":
    message = "Hello World"
    key = 4
    
    cipher_text = encrypt(message, key)
    plain_text = decrypt(cipher_text, key)
    
    print("\n Encrypted text: " + cipher_text)
    print("\n Decrypted text: " + plain_text)