from interfaces.ui_interface import UIInterface

class CLIUI(UIInterface):
    """CLI implementation of UI interface."""
    
    def display_event_details(self, event_details: str):
        """Display event details to console."""
        print("\n" + "="*50)
        print("EVENT DETAILS")
        print("="*50)
        print(event_details)
        print("="*50)
    
    def display_transactions(self, transactions):
        """Display transactions to console."""
        print("\n" + "="*50)
        print("TRANSACTIONS")
        print("="*50)
        if isinstance(transactions, list):
            for transaction in transactions:
                print(f"  • {transaction}")
        else:
            print(transactions)
        print("="*50)
    
    def display_message(self, message: str):
        """Display a message to console."""
        print(f"\n{message}")
    
    def show_results(self, event_details: str, transactions):
        """Show combined results."""
        self.display_event_details(event_details)
        self.display_transactions(transactions)

