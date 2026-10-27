import random
class Sponsor:
    def __init__(self, name):
        self.name = name
    def negotiateSponsorship(self):
        # Реалізація логіки переговорів про спонсорство
        random_outcome = random.choice(["success", "failure"])
        print(f"Negotiating sponsorship with {self.name}...")
        if random_outcome == "success":
            print(f"Sponsorship with {self.name} was successful!")
        else:
            print(f"Sponsorship with {self.name} failed.")


    def __repr__(self) -> str:
        return f"Sponsor(name={self.name})"