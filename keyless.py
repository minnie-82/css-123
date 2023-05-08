import math

def encrypt(message):
    cipher = ""
    num_cols = math.ceil(math.sqrt(len(message)))  # Number of columns in the transposition grid
    for col in range(num_cols):
        pointer = col
        while pointer < len(message):
            cipher += message[pointer]
            pointer += num_cols
    return cipher

def decrypt(cipher):
    message = ""
    num_cols = math.ceil(math.sqrt(len(cipher)))  # Number of columns in the transposition grid
    num_rows = math.ceil(len(cipher) / num_cols)  # Number of rows in the transposition grid
    num_blank = (num_cols * num_rows) - len(cipher)  # Number of blank spaces in the grid
    plaintext = [''] * num_cols

    col = 0
    row = 0
    for symbol in cipher:
        plaintext[col] += symbol
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_blank):
            col = 0
            row += 1

    for col in range(num_cols):
        message += plaintext[col]
    return message

# Example usage
input_message = "Hello, world!"
encrypted_message = encrypt(input_message)
decrypted_message = decrypt(encrypted_message)

print("Input message: ", input_message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
