class DataProcessor:

    def encrypt(self, data, key):
        encrypted = []

        for value in data:
            encrypted.append(value ^ key)

        return encrypted

    def compress(self, data, factor):
        compressed = []

        for value in data:
            compressed.append(round(value * factor))

        return compressed