def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key += alphabet
    playfair_matrix = []

    for char in key:
        if char not in playfair_matrix:
            playfair_matrix.append(char)

    playfair_matrix = [playfair_matrix[i:i + 5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_coordinates(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    cipher_text = cipher_text.upper().replace("J", "I")

    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]

        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return decrypted_text

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    plain_text = plain_text.upper().replace("J", "I")

    # Remove spaces and punctuation
    plain_text = ''.join(char for char in plain_text if char.isalpha())

    # Add a padding character if the length is odd
    if len(plain_text) % 2 != 0:
        plain_text += 'X'

    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]

        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_text

# ...

key = input("Enter the key: ")
plain_text = input("Enter the plain-text to encrypt: ")

# Display the Playfair matrix
matrix = generate_playfair_matrix(key)
print("\nPlayfair Matrix:")
display_matrix(matrix)

# Encrypt the message
encrypted_text = playfair_encrypt(plain_text, key)
print("\nEncrypted Message:", encrypted_text)

# Decrypt the message
decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted Message:", decrypted_text)