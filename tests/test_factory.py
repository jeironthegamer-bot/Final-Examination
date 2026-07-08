from src.factory.strategy_factory import StrategyFactory
from src.strategies.encryption_strategy import EncryptionStrategy
from src.strategies.compression_strategy import CompressionStrategy

import pytest


def test_create_encryption_strategy():
    factory = StrategyFactory()

    strategy = factory.create_strategy("encryption", 0x4F)

    assert isinstance(strategy, EncryptionStrategy)


def test_create_compression_strategy():
    factory = StrategyFactory()

    strategy = factory.create_strategy("compression", 0.85)

    assert isinstance(strategy, CompressionStrategy)


def test_invalid_strategy():
    factory = StrategyFactory()

    with pytest.raises(ValueError):
        factory.create_strategy("invalid", 0)
