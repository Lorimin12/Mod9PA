#Penguin.py
#Walter Lorimin
#11/01/2026
#Class representing a penguin

class Penguin:
    def __init__(self, sample_number, species, body_mass):
        self.sample_number = sample_number
        self.species = species
        self.body_mass = body_mass
    def display_info(self):
        print(f"Sample number: {self.sample_number}\n"
              f"Species: {self.species}\n"
              f"Body mass: {self.body_mass} g")
