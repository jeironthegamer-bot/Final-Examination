from src.strategies.encryption_strategy import EncryptionStrategy
from src.strategies.compression_strategy import CompressionStrategy


def test_encryption_strategy():
    strategy = EncryptionStrategy(0x4F)

    assert strategy.process([78, 82]) == [1, 29]


def test_compression_strategy():
    strategy = CompressionStrategy(0.85)

    assert strategy.process([100, 50]) == [85, 42]
