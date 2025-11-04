from models.member import Member

class Player(Member):
    def __init__(self, full_name, email, phone, address, join_date,
                 skills=None, interests=None, sport_type=None, position=None):
        super().__init__(full_name, email, phone, address, join_date, skills, interests)
        self.sport_type = sport_type
        self.position = position
        self.performance_stats = {}

    def add_stat(self, key, value):
        self.performance_stats[key] = value
