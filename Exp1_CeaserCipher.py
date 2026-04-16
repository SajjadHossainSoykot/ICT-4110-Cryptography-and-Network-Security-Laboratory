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

plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

cipher = encrypt(plaintext, key)
print("Encrypted text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted text:", plain)