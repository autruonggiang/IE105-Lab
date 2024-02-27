def rail_fence_encrypt(plaintext, rails):
    encrypted = ''
    fence = [''] * rails
    down = False
    row = 0

    for ch in plaintext:
        fence[row] += ch

        if row == 0 or row == rails - 1:
            down = not down

        row += 1 if down else -1

    encrypted = ''.join(fence)

    return encrypted

def main():
    plaintext = "Au Truong Giang"
    rails = 3

    encrypted_text = rail_fence_encrypt(plaintext, rails)

    print("Encrypted:", encrypted_text)

if __name__ == "__main__":
    main()
