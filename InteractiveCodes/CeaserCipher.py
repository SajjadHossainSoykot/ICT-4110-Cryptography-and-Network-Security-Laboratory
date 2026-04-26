def encrypt(text, key):
    result = ""
    key %= 26

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key %= 26

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch

    return result


key = 0

while True:
    print("\n====== Caesar Cipher ======")
    print("---------------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print(f"3. Change Key [Current Key: {key}]")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()
        if plaintext:
            cipher = encrypt(plaintext, key)
            print("Encrypted text:", cipher)
        else:
            print("Empty input!")

    elif choice == '2':
        cipher_input = input("Enter ciphertext: ").strip()
        if cipher_input:
            decrypted = decrypt(cipher_input, key)
            print("Decrypted text:", decrypted)
        else:
            print("Empty input!")

    elif choice == '3':
        try:
            key = int(input("Enter new key: "))
            print("Key changed successfully!")
        except ValueError:
            print("Invalid key! Please enter an integer.")

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")