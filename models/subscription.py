from interfaces.payable import Payable

class Subscription(Payable):
    def __init__(self, member, amount):
        self.member = member
        self.amount = amount
        self.status = "unpaid"

    def process_payment(self):
        self.status = "paid"
        return f"{self.member.full_name} paid {self.amount} DA"
