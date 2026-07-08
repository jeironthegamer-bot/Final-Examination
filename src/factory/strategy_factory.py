from src.strategies.encryption_strategy import EncryptionStrategy
from src.strategies.compression_strategy import CompressionStrategy


class StrategyFactory:

    def create_strategy(self, strategy_type, value):

        if strategy_type == "encryption":
            return EncryptionStrategy(value)

        elif strategy_type == "compression":
            return CompressionStrategy(value)

        raise ValueError("Invalid strategy type.")