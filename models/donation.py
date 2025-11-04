from interfaces.payable import Payable

class Donation(Payable):
    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount

    def process_payment(self):
        return f"Donation of {self.amount} DA received from {self.donor_name}"
