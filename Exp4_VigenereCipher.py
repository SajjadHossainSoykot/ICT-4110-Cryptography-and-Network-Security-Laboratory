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

plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

cipher = encrypt_vigenere(plaintext, keyword)
print("Encrypted text:", cipher)

plain = decrypt_vigenere(cipher, keyword)
print("Decrypted text:", plain)