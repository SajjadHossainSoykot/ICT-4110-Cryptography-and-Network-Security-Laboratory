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

plaintext = input("Enter plaintext: ")
depth = int(input("Enter depth: "))

cipher = encrypt_rail_fence(plaintext, depth)
print("Encrypted text:", cipher)

plain = decrypt_rail_fence(cipher, depth)
print("Decrypted text:", plain)