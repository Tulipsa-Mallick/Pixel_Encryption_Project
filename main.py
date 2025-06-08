from src.encryption import encrypt_image, decrypt_image

def main():
    print("=== Pixel-Based Image Encryption Tool ===")

    while True:
        print("\nSelect an option:")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Encrypt & Decrypt an Image")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            original_image = input("Enter path to the input image: ")
            encrypted_image = input("Enter path for the encrypted image: ")
            try:
                key = int(input("Enter encryption key (integer): "))
                encrypt_image(original_image, encrypted_image, key)
            except ValueError:
                print("[!] Please enter a valid integer key.")
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '2':
            encrypted_image = input("Enter path to the encrypted image: ")
            decrypted_image = input("Enter path for the decrypted image: ")
            try:
                key = int(input("Enter decryption key (same as used for encryption): "))
                decrypt_image(encrypted_image, decrypted_image, key)
            except ValueError:
                print("[!] Please enter a valid integer key.")
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '3':
            original_image = input("Enter path to the input image: ")
            encrypted_image = input("Enter path for the encrypted image: ")
            decrypted_image = input("Enter path for the decrypted image: ")
            try:
                key = int(input("Enter encryption key (integer): "))
                encrypt_image(original_image, encrypted_image, key)
                decrypt_image(encrypted_image, decrypted_image, key)
            except ValueError:
                print("[!] Please enter a valid integer key.")
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
