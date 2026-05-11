from vault import load_vault, save_vault
from crypto import encrypt, decrypt, check_master_password

def main():
    password = input("Enter master password: ")

    if not check_master_password(password):
        print("Wrong password ❌")
        return

    vault = load_vault()

    while True:
        print("\n=== Password Vault ===")
        print("1. Add password")
        print("2. View vault")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            site = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")

            vault[site] = {
                "username": username,
                "password": encrypt(password)
            }

            save_vault(vault)
            print("Saved ✔")

        elif choice == "2":
            print("\n--- Vault ---")
            for site, data in vault.items():
                print(f"{site} -> {data['username']} / {decrypt(data['password'])}")

        elif choice == "3":
            print("Bye 👋")
            break

        else:
            print("Invalid option")
if __name__ == "__main__":
    main()