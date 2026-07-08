from src.auth import authenticate
from src.processor import DataProcessor
from src.factory.strategy_factory import StrategyFactory


def main():
    print("=== Legacy Data Processing System ===")

    username = input("Username: ")
    password = input("Password: ")

    token = authenticate(username, password)

    if not token:
        print("Authentication Failed!")
        return

    print("\nAuthentication Successful!")

    print("\nJWT Token:")
    print(token)

    data_stream = [78, 82, 91, 65, 40, 99, 88]

    # Create the factory
    factory = StrategyFactory()

    # Create the processor with the Encryption Strategy
    processor = DataProcessor(
        factory.create_strategy("encryption", 0x4F)
    )

    encrypted = processor.process(data_stream)

    # Switch to the Compression Strategy
    processor.set_strategy(
        factory.create_strategy("compression", 0.85)
    )

    compressed = processor.process(encrypted)

    print("\nOriginal Data:")
    print(data_stream)

    print("\nEncrypted Data:")
    print(encrypted)

    print("\nCompressed Data:")
    print(compressed)


if __name__ == "__main__":
    main()