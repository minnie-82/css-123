def encrypt_message(message, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return ''.join(cipher)


def decrypt_cipher(cipher, key):
    num_of_columns = len(cipher) // key
    num_of_rows = key
    num_of_shaded_boxes = len(cipher) % key
    plaintext = [''] * num_of_columns
    col = 0
    row = 0

    for symbol in cipher:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)


# Example usage
key = 8
message = "Hello, World!"
encrypted_message = encrypt_message(message, key)
decrypted_cipher = decrypt_cipher(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted cipher:", decrypted_cipher)
