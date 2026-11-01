import random
class Sponsor:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def negotiate_sponsorship(self):
        # Реалізація логіки переговорів про спонсорство
        random_outcome = random.choice(["success", "failure"])
        print(f"Negotiating sponsorship with {self.name}...")
        if random_outcome == "success":
            print(f"Sponsorship with {self.name} was successful!")
            return True
        else:
            print(f"Sponsorship with {self.name} failed.")
            return False

    def __str__(self):
        return f"Sponsorship with {self.name}"

    def __repr__(self) -> str:
        return f"Sponsor(name={self.name})"