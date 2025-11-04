from models.member import Member

class Coach(Member):
    def __init__(self, full_name, email, phone, address, join_date,
                 skills=None, interests=None, specialty=None, experience_years=0):
        super().__init__(full_name, email, phone, address, join_date, skills, interests)
        self.specialty = specialty
        self.experience_years = experience_years
