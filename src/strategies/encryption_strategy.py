from src.strategies.strategy import ProcessingStrategy

class EncryptionStrategy(ProcessingStrategy):

    def __init__(self, key):
        self.key = key

    def process(self, data):
        return [value ^ self.key for value in data]