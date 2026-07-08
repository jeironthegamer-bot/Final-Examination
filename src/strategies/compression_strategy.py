from src.strategies.strategy import ProcessingStrategy


class CompressionStrategy(ProcessingStrategy):

    def __init__(self, factor):
        self.factor = factor

    def process(self, data):
        return [round(value * self.factor) for value in data]
