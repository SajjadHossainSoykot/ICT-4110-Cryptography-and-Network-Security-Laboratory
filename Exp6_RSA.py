from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Modular inverse not found.")

def rsa_keygen(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with phi(n).")

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(text, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in text]

def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)

p = 61
q = 53
e = 17

public_key, private_key = rsa_keygen(p, q, e)

print("Public Key:", public_key)
print("Private Key:", private_key)

plaintext = input("Enter plaintext: ")
cipher = rsa_encrypt(plaintext, public_key)
print("Encrypted text:", cipher)

plain = rsa_decrypt(cipher, private_key)
print("Decrypted text:", plain)