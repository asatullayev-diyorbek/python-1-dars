ism = input("Ism: ").lower()
familiya = input("Familiya: ").lower()

username = f"{ism}_{familiya[:4]}"

print(f"Username: {username}")
