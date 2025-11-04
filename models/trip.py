from models.event import Event

class Trip(Event):
    def __init__(self, name, description, date, organizer, destination):
        super().__init__(name, description, date, organizer)
        self.destination = destination

    def describe(self):
        return f"Trip to {self.destination}: {self.description}"
