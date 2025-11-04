import pandas as pd
from models.player import Player
from models.coach import Coach
from interfaces.storage_interface import StorageInterface

class CSVStorage(StorageInterface):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_members(self):
        df = pd.read_csv(self.file_path)
        members = []

        for _, row in df.iterrows():
            if row["Role"].strip().lower() == "player":
                m = Player(
                    row["Full Name"], row["Email"], row["Phone"], row["Address"],
                    row["Join Date"], row["Skills"].split(", ") if str(row["Skills"]) != "nan" else [],
                    row["Interests"].split(", ") if str(row["Interests"]) != "nan" else []
                )
            else:
                m = Coach(
                    row["Full Name"], row["Email"], row["Phone"], row["Address"],
                    row["Join Date"], row["Skills"].split(", ") if str(row["Skills"]) != "nan" else [],
                    row["Interests"].split(", ") if str(row["Interests"]) != "nan" else [],
                    specialty="General"
                )
            members.append(m)

        return members
