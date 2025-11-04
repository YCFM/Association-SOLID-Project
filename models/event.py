from abc import ABC, abstractmethod
from interfaces.organizable import Organizable

class Event(Organizable, ABC):
    """Base Event class — Open for extension. Stores data only (SRP compliant)."""
    def __init__(self, name, description, date, organizer):
        self.name = name
        self.description = description
        self.date = date
        self.organizer = organizer
        self.participants = []

    @abstractmethod
    def describe(self):
        pass

    def schedule(self):
        return f"Event '{self.name}' scheduled on {self.date}"
