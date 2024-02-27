def caesar_cipher_encode(plain_text, shift):
    result = ''
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def caesar_cipher_decode(encoded_text, shift):
    result = ''
    for char in encoded_text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_cipher_brute_force(encoded_text):
    for shift in range(26):
        decoded_text = caesar_cipher_decode(encoded_text, shift)
        print(f"Key = {shift}:\n{decoded_text}\n")


print("1. Encode\n2. Decode\n3. Brute force")
option = int(input("What you want to do: "))

if option == 1:
    plain_text = input("Enter plain text please: ")
    shift = int(input("Enter the key: "))
    encoded_text = caesar_cipher_encode(plain_text, shift)
    print(encoded_text)


if option == 2:
    encoded_text = input("Enter encoded text please: ")
    shift = int(input("Enter the key: "))
    decoded_text = caesar_cipher_decode(encoded_text, shift)
    print(decoded_text)

if option == 3:
    encoded_text = input("Enter encoded text please: ")
    caesar_cipher_brute_force(encoded_text)