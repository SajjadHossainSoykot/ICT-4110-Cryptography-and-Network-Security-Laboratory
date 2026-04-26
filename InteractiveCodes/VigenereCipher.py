def generate_key(text, key):
    key = key.upper()
    text = text.upper()
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            result += key[j % len(key)]
            j += 1
        else:
            result += ch

    return result


def encrypt_vigenere(text, key):
    text = text.upper()
    key = generate_key(text, key)
    cipher = ""

    for t, k in zip(text, key):
        if t.isalpha():
            cipher += chr((ord(t) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
        else:
            cipher += t

    return cipher


def decrypt_vigenere(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher, key)
    plain = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            plain += chr((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26 + ord('A'))
        else:
            plain += c

    return plain


keyword = "KEY"

while True:
    print("\n====== Vigenere Cipher ======")
    print("-----------------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print(f"3. Change Keyword [Current Keyword: {keyword}]")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()
        if plaintext:
            cipher = encrypt_vigenere(plaintext, keyword)
            print("Encrypted text:", cipher)
        else:
            print("Empty input!")

    elif choice == '2':
        cipher_input = input("Enter ciphertext: ").strip()
        if cipher_input:
            decrypted = decrypt_vigenere(cipher_input, keyword)
            print("Decrypted text:", decrypted)
        else:
            print("Empty input!")

    elif choice == '3':
        new_keyword = input("Enter new keyword: ").strip()

        if new_keyword.isalpha():
            keyword = new_keyword.upper()
            print("Keyword changed successfully!")
        else:
            print("Invalid keyword! Please enter alphabetic characters only.")

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")