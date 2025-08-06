

class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def display(self):
        print(f"Card Name: {self.name}")
        print(f"Description: {self.description}")