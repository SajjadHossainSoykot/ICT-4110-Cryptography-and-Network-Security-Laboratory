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
        [( d * det_inv) % 26, (-b * det_inv) % 26],
        [(-c * det_inv) % 26, ( a * det_inv) % 26]
    ]
    return inv

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
        pair = nums[i:i+2]
        c1 = (key[0][0]*pair[0] + key[0][1]*pair[1]) % 26
        c2 = (key[1][0]*pair[0] + key[1][1]*pair[1]) % 26
        result.extend([c1, c2])

    return numbers_to_text(result)

def decrypt_hill(cipher, key):
    inv_key = matrix_inverse_2x2(key)
    nums = text_to_numbers(cipher)
    result = []

    for i in range(0, len(nums), 2):
        pair = nums[i:i+2]
        p1 = (inv_key[0][0]*pair[0] + inv_key[0][1]*pair[1]) % 26
        p2 = (inv_key[1][0]*pair[0] + inv_key[1][1]*pair[1]) % 26
        result.extend([p1, p2])

    return numbers_to_text(result)

key = [[3, 3], [2, 5]]

plaintext = input("Enter plaintext: ")
print("Plaintext:", plaintext)
print("Key Matrix:", key)
cipher = encrypt_hill(plaintext, key)
print("Encrypted text:", cipher)

plain = decrypt_hill(cipher, key)
print("Decrypted text:", plain)