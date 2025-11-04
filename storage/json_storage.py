import json
from models.player import Player
from models.coach import Coach
from interfaces.storage_interface import StorageInterface

class JSONStorage(StorageInterface):
    """JSON implementation of StorageInterface following DIP."""
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_members(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        members = []
        for item in data:
            if item["Role"].strip().lower() == "player":
                m = Player(
                    item["Full Name"], item["Email"], item["Phone"], item["Address"],
                    item["Join Date"], 
                    item.get("Skills", "").split(", ") if item.get("Skills") else [],
                    item.get("Interests", "").split(", ") if item.get("Interests") else []
                )
            else:
                m = Coach(
                    item["Full Name"], item["Email"], item["Phone"], item["Address"],
                    item["Join Date"],
                    item.get("Skills", "").split(", ") if item.get("Skills") else [],
                    item.get("Interests", "").split(", ") if item.get("Interests") else [],
                    specialty="General"
                )
            members.append(m)
        
        return members

