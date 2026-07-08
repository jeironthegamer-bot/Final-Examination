from src.processor import DataProcessor
from src.strategies.encryption_strategy import EncryptionStrategy
from src.strategies.compression_strategy import CompressionStrategy


def test_encryption():
    processor = DataProcessor(
        EncryptionStrategy(0x4F)
    )

    data = [78, 82]

    result = processor.process(data)

    assert result == [1, 29]


def test_compression():
    processor = DataProcessor(
        CompressionStrategy(0.85)
    )

    data = [100, 50]

    result = processor.process(data)

    assert result == [85, 42]