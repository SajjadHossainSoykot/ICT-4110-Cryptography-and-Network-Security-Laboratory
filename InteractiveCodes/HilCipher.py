def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists.")


def matrix_inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det, 26)

    inv = [
        [(d * det_inv) % 26, (-b * det_inv) % 26],
        [(-c * det_inv) % 26, (a * det_inv) % 26]
    ]

    return inv


def is_valid_key(matrix):
    try:
        matrix_inverse_2x2(matrix)
        return True
    except ValueError:
        return False


def process_text(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha())

    if len(text) % 2 != 0:
        text += 'X'

    return text


def text_to_numbers(text):
    return [ord(ch) - ord('A') for ch in text]


def numbers_to_text(nums):
    return "".join(chr(n % 26 + ord('A')) for n in nums)


def encrypt_hill(text, key):
    text = process_text(text)
    nums = text_to_numbers(text)
    result = []

    for i in range(0, len(nums), 2):
        pair = nums[i:i + 2]

        c1 = (key[0][0] * pair[0] + key[0][1] * pair[1]) % 26
        c2 = (key[1][0] * pair[0] + key[1][1] * pair[1]) % 26

        result.extend([c1, c2])

    return numbers_to_text(result)


def decrypt_hill(cipher, key):
    cipher = process_text(cipher)
    inv_key = matrix_inverse_2x2(key)
    nums = text_to_numbers(cipher)
    result = []

    for i in range(0, len(nums), 2):
        pair = nums[i:i + 2]

        p1 = (inv_key[0][0] * pair[0] + inv_key[0][1] * pair[1]) % 26
        p2 = (inv_key[1][0] * pair[0] + inv_key[1][1] * pair[1]) % 26

        result.extend([p1, p2])

    return numbers_to_text(result)


def show_key_matrix(key):
    print("Key Matrix:")
    for row in key:
        print(row)


def input_key_matrix():
    try:
        print("Enter 2x2 key matrix values:")
        a = int(input("Enter value a: "))
        b = int(input("Enter value b: "))
        c = int(input("Enter value c: "))
        d = int(input("Enter value d: "))

        new_key = [[a, b], [c, d]]

        if is_valid_key(new_key):
            return new_key
        else:
            print("Invalid key matrix! Determinant has no inverse modulo 26.")
            return None

    except ValueError:
        print("Invalid input! Please enter integer values.")
        return None


key = [[3, 3], [2, 5]]

while True:
    print("\n====== Hill Cipher ======")
    print("-------------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print(f"3. Change Key Matrix [Current Key: {key}]")
    print("4. Show Key Matrix")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()

        if plaintext:
            cipher = encrypt_hill(plaintext, key)
            print("Encrypted text:", cipher)
        else:
            print("Empty input!")

    elif choice == '2':
        cipher_input = input("Enter ciphertext: ").strip()

        if cipher_input:
            decrypted = decrypt_hill(cipher_input, key)
            print("Decrypted text:", decrypted)
        else:
            print("Empty input!")

    elif choice == '3':
        new_key = input_key_matrix()

        if new_key:
            key = new_key
            print("Key matrix changed successfully!")

    elif choice == '4':
        show_key_matrix(key)

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")