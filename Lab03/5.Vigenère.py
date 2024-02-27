def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_len = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_len]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_len = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_len]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

# Test the Vigenère cipher with a message and key
message = "The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution."
key = "AUTRUONGGIANG"

encrypted_message = vigenere_encrypt(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = vigenere_decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)