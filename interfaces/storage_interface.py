from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def load_members(self):
        pass
