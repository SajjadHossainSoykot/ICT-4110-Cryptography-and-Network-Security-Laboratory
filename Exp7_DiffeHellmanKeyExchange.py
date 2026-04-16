def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)

    shared_A = pow(B, a, p)
    shared_B = pow(A, b, p)

    return A, B, shared_A, shared_B

p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

A, B, shared_A, shared_B = diffie_hellman(p, g, a, b)

print("Public key of A:", A)
print("Public key of B:", B)
print("Shared key for A:", shared_A)
print("Shared key for B:", shared_B)