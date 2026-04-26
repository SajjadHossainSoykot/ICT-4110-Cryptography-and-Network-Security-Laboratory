def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)

    shared_A = pow(B, a, p)
    shared_B = pow(A, b, p)

    return A, B, shared_A, shared_B


# Default values
p = 23
g = 5
a = 6
b = 15

while True:
    print("\n====== Diffie-Hellman Key Exchange ======")
    print("------------------------------------------")
    print("1. Generate Keys")
    print("2. Change Public Values (p, g)")
    print("3. Change Private Keys (a, b)")
    print(f"4. Show Current Values [p={p}, g={g}, a={a}, b={b}]")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        try:
            A, B, shared_A, shared_B = diffie_hellman(p, g, a, b)

            print("\nPublic key of A:", A)
            print("Public key of B:", B)
            print("Shared key for A:", shared_A)
            print("Shared key for B:", shared_B)

            if shared_A == shared_B:
                print("Shared secret key established successfully!")
            else:
                print("Error: Keys do not match!")

        except Exception as e:
            print("Error:", e)

    elif choice == '2':
        try:
            p = int(input("Enter prime number p: "))
            g = int(input("Enter primitive root g: "))
            print("Public values updated!")
        except ValueError:
            print("Invalid input! Enter integers only.")

    elif choice == '3':
        try:
            a = int(input("Enter private key of A: "))
            b = int(input("Enter private key of B: "))
            print("Private keys updated!")
        except ValueError:
            print("Invalid input! Enter integers only.")

    elif choice == '4':
        print(f"Current values → p={p}, g={g}, a={a}, b={b}")

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")