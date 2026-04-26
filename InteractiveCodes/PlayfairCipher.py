def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []

    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix_list.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch)
            matrix_list.append(ch)

    return [matrix_list[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    ch = ch.upper().replace("J", "I")

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def encrypt_playfair(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt_playfair(text, matrix):
    text = "".join(ch for ch in text.upper().replace("J", "I") if ch.isalpha())

    if len(text) % 2 != 0:
        text += "X"

    plain = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]

        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


keyword = "MONARCHY"
matrix = generate_key_matrix(keyword)

while True:
    print("\n====== Playfair Cipher ======")
    print("-----------------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print(f"3. Change Keyword [Current Keyword: {keyword}]")
    print("4. Show Key Matrix")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()

        if plaintext:
            cipher = encrypt_playfair(plaintext, matrix)
            print("Encrypted text:", cipher)
        else:
            print("Empty input!")

    elif choice == '2':
        cipher_input = input("Enter ciphertext: ").strip()

        if cipher_input:
            decrypted = decrypt_playfair(cipher_input, matrix)
            print("Decrypted text:", decrypted)
        else:
            print("Empty input!")

    elif choice == '3':
        new_keyword = input("Enter new keyword: ").strip()

        if new_keyword and any(ch.isalpha() for ch in new_keyword):
            keyword = new_keyword.upper().replace("J", "I")
            matrix = generate_key_matrix(keyword)
            print("Keyword changed successfully!")
        else:
            print("Invalid keyword! Please enter alphabetic characters.")

    elif choice == '4':
        print("Key Matrix:")
        for row in matrix:
            print(" ".join(row))

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")