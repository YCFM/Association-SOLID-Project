from models.event import Event

class Competition(Event):
    def __init__(self, name, description, date, organizer, sport_type):
        super().__init__(name, description, date, organizer)
        self.sport_type = sport_type

    def describe(self):
        return f"Competition ({self.sport_type}): {self.description}"
