# Напишіть класи серіалізації контейнерів з даними Python у json, bin файли.
# Самі класи мають відповідати загальному інтерфейсу (абстрактному базовому класу) SerializationInterface.

from abc import abstractmethod, ABC
import pickle
import json


class SerializationInterface(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def load_data(self):
        pass


class SerializationJson(SerializationInterface):
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "w") as fh:
            json.dump(data, fh)

    def load_data(self):
        with open(self.filename, "r") as fh:
            return json.load(fh)


class SerializationPickle(SerializationInterface):
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "wb") as fh:
            pickle.dump(data, fh)

    def load_data(self):
        with open(self.filename, "rb") as fh:
            return pickle.load(fh)

