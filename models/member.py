class Member:
    """Stores member data only — SRP compliant."""
    def __init__(self, full_name, email, phone, address, join_date, skills=None, interests=None):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.skills = skills if skills else []
        self.interests = interests if interests else []

    def __str__(self):
        return self.full_name
