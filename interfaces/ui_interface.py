from abc import ABC, abstractmethod

class UIInterface(ABC):
    """Interface for UI implementations following DIP."""
    
    @abstractmethod
    def display_event_details(self, event_details: str):
        """Display event details."""
        pass
    
    @abstractmethod
    def display_transactions(self, transactions):
        """Display transaction list."""
        pass
    
    @abstractmethod
    def display_message(self, message: str):
        """Display a general message."""
        pass
    
    @abstractmethod
    def show_results(self, event_details: str, transactions):
        """Show combined results."""
        pass

