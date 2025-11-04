from models.event import Event

class EventManager:
    """Handles event logic separately from Event data (SRP)."""

    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def register_member_for_event(self, event: Event, member):
        """Handles member registration logic for events (SRP - business logic separated from data)."""
        if event not in self.events:
            self.add_event(event)
        # All registration logic is here - Event only stores data
        if member not in event.participants:
            event.participants.append(member)
            return f"{member.full_name} registered for {event.name}"
        return f"{member.full_name} is already registered for {event.name}"

    def list_events(self):
        return [e.name for e in self.events]

    def display_event_details(self, event: Event):
        return event.describe()
