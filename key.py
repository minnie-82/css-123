def encrypt(plaintext, key):
    # add padding if necessary
    if len(plaintext) % len(key) != 0:
        plaintext += ' ' * (len(key) - len(plaintext) % len(key))

    # create the ciphertext
    ciphertext = ''
    for k in key:
        for j in range(len(plaintext) // len(key)):
            ciphertext += plaintext[j * len(key) + int(k) - 1]
    return ciphertext

def decrypt(ciphertext, key):
    # calculate the number of columns
    num_cols = len(key)

    # calculate the number of rows
    num_rows = len(ciphertext) // num_cols

    # calculate the number of leftover characters
    num_leftover_chars = len(ciphertext) % num_cols

    # create the transposition matrix
    matrix = []
    for k in sorted(key):
        column = key.index(str(k))
        if column < num_leftover_chars:
            offset = column * (num_rows + 1)
            matrix.append(ciphertext[offset:offset + num_rows + 1])
        else:
            offset = num_leftover_chars * (num_rows + 1) + (column - num_leftover_chars) * num_rows
            matrix.append(ciphertext[offset:offset + num_rows])

    # create the plaintext
    plaintext = ''
    for i in range(num_rows):
        for j in range(num_cols):
            plaintext += matrix[j][i]

    # add any leftover characters to the plaintext
    plaintext += ciphertext[num_rows * num_cols:]

    return plaintext
plaintext = input('\nEnter your PLAIN TEXT: ')
key = '53241'

while True:
    print('Transposition Cipher\n')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Quit')
    choice = input('\nEnter your choice: ')

    if choice == '1':
        ciphertext = encrypt(plaintext, key)
        print('Ciphertext:', ciphertext)

    elif choice == '2':
      decrypted_plaintext = decrypt(ciphertext, key)
      print('Decrypted plaintext:', decrypted_plaintext)

    elif choice == '3':
        break

    else:
        print('\nInvalid choice. Try again.')
