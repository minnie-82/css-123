def encrypt(plaintext, key):
    # add padding if necessary
    if len(plaintext) % key != 0:
        plaintext += ' ' * (key - len(plaintext) % key)

    # create the ciphertext
    ciphertext = ''
    for i in range(key):
        for j in range(len(plaintext) // key):
            ciphertext += plaintext[j * key + i]
    return ciphertext

def decrypt(ciphertext, key):
    # create the plaintext
    plaintext = ''
    for i in range(len(ciphertext) // key):
        for j in range(key):
            plaintext += ciphertext[i + j * (len(ciphertext) // key)]
    return plaintext.strip()

while True:
    print('Transposition Cipher\n')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Quit')
    choice = input('\nEnter your choice: ')

    if choice == '1':
        plaintext = input('\nEnter plaintext: ')
        key = int(input('Enter key: '))
        ciphertext = encrypt(plaintext, key)
        print('\nCiphertext:', ciphertext)

    elif choice == '2':
        decrypted_plaintext = decrypt(ciphertext, key)
        print('Decrypted plaintext:', decrypted_plaintext)

    elif choice == '3':
        break

    else:
        print('\nInvalid choice. Try again.')

