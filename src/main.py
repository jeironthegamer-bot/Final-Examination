from auth import authenticate
from processor import DataProcessor


def main():
    print("=== Legacy Data Processing System ===")

    username = input("Username: ")
    password = input("Password: ")

    if not authenticate(username, password):
        print("Authentication Failed!")
        return

    print("\nAuthentication Successful!")

    data_stream = [78, 82, 91, 65, 40, 99, 88]

    processor = DataProcessor()

    encrypted = processor.encrypt(data_stream, 0x4F)
    compressed = processor.compress(encrypted, 0.85)

    print("\nOriginal Data:")
    print(data_stream)

    print("\nEncrypted Data:")
    print(encrypted)

    print("\nCompressed Data:")
    print(compressed)


if __name__ == "__main__":
    main()