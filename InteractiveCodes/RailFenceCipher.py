def encrypt_rail_fence(text, key):
    if key <= 1:
        return text

    rail = ['' for _ in range(key)]
    row = 0
    direction = 1

    for ch in text:
        rail[row] += ch
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(rail)


def decrypt_rail_fence(cipher, key):
    if key <= 1:
        return cipher

    pattern = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    row, direction = 0, 1
    for col in range(len(cipher)):
        pattern[row][col] = '*'
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    result = []
    row, direction = 0, 1
    for col in range(len(cipher)):
        result.append(pattern[row][col])
        row += direction

        if row == 0 or row == key - 1:
            direction *= -1

    return ''.join(result)


depth = 3

while True:
    print("\n====== Rail Fence Cipher ======")
    print("-------------------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print(f"3. Change Depth [Current Depth: {depth}]")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plaintext = input("Enter plaintext: ").strip()

        if plaintext:
            cipher = encrypt_rail_fence(plaintext, depth)
            print("Encrypted text:", cipher)
        else:
            print("Empty input!")

    elif choice == '2':
        cipher_input = input("Enter ciphertext: ").strip()

        if cipher_input:
            decrypted = decrypt_rail_fence(cipher_input, depth)
            print("Decrypted text:", decrypted)
        else:
            print("Empty input!")

    elif choice == '3':
        try:
            new_depth = int(input("Enter new depth: "))

            if new_depth > 1:
                depth = new_depth
                print("Depth changed successfully!")
            else:
                print("Invalid depth! Please enter a value greater than 1.")

        except ValueError:
            print("Invalid depth! Please enter an integer.")

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")