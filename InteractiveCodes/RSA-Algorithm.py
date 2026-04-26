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

# Fixed primes
p = 61
q = 53

# initial e
e = 17

def generate_keys():
    return rsa_keygen(p, q, e)

public_key, private_key = generate_keys()

while True:
    print("\n====== RSA MENU ======")
    print("Public Key :", public_key)
    print("Private Key:", private_key)
    print("----------------------")
    print("1. Send a Message")
    print("2. Receive a Message")
    print("3. Change Public Key (e)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        plaintext = input("Enter plaintext: ")
        cipher = rsa_encrypt(plaintext, public_key)
        print("Encrypted text:", cipher)

        decrypted = rsa_decrypt(cipher, private_key)
        print("Decrypted text:", decrypted)

    elif choice == '2':
        cipher_input = input("Enter Ciphertext (space separated numbers): ")
        try:
            cipher = list(map(int, cipher_input.split()))
            decrypted = rsa_decrypt(cipher, private_key)
            print("Decrypted text:", decrypted)
        except:
            print("Invalid ciphertext input!")

    elif choice == '3':
        try:
            new_e = int(input("Enter new value for e: "))
            phi = (p - 1) * (q - 1)

            if gcd(new_e, phi) != 1:
                print("Invalid e! It must be coprime with phi(n).")
            else:
                e = new_e
                public_key, private_key = generate_keys()
                print("Public key updated successfully!")

        except:
            print("Invalid input! Enter an integer.")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")