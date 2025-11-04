from models.subscription import Subscription

class AnnualSubscription(Subscription):
    def __init__(self, member, amount):
        super().__init__(member, amount)

    # inherits process_payment — LSP OK
