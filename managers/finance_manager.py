from interfaces.payable import Payable

class FinanceManager:
    """Handles all payments (SRP)."""

    def __init__(self):
        self.transactions = []

    def process(self, payment: Payable):
        result = payment.process_payment()
        self.transactions.append(result)
        return result

    def list_transactions(self):
        return self.transactions
