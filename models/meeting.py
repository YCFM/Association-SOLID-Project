from models.event import Event

class Meeting(Event):
    def __init__(self, name, description, date, organizer, location):
        super().__init__(name, description, date, organizer)
        self.location = location

    def describe(self):
        return f"Meeting at {self.location}: {self.description}"
