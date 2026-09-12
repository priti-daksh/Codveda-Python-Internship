from cryptography.fernet import Fernet


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


def encrypt_file():
    key = load_key()
    fernet = Fernet(key)

    file_name = input("Enter file name to encrypt: ")

    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open("encrypted_file.txt", "wb") as file:
            file.write(encrypted_data)

        print("\nFile encrypted successfully!")
        print("Encrypted file saved as encrypted_file.txt")

    except FileNotFoundError:
        print("File not found!")


def decrypt_file():
    key = load_key()
    fernet = Fernet(key)

    file_name = input("Enter file name to decrypt: ")

    try:
        with open(file_name, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open("decrypted_file.txt", "wb") as file:
            file.write(decrypted_data)

        print("\nFile decrypted successfully!")
        print("Decrypted file saved as decrypted_file.txt")

    except FileNotFoundError:
        print("File not found!")

    except Exception:
        print("Unable to decrypt the file!")


def main():
    while True:
        print("\n===== FILE ENCRYPTION / DECRYPTION =====")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            encrypt_file()

        elif choice == "2":
            decrypt_file()

        elif choice == "3":
            print("\nThank you for using the application!")
            break

        else:
            print("Invalid choice! Please try again.")


main()