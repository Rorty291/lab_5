from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, name, age, country):
        self._name = name
        self._age = age
        self._country = country

    @abstractmethod
    def name(self):
        ### Обирає ім'я учасника ###
        pass

    @abstractmethod
    def country(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class TeamMember(Member):
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def country(self):
        return self._country

    def __str__(self):
        return f"{self.name} ({self.age} y.o.) from {self.country}"

    def __repr__(self):
        return f"TeamMember('{self.name}', {self.age}, '{self.country}')"