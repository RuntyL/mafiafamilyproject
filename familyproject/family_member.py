from abc import ABC, abstractmethod

class FamilyMember(ABC):
    def __init__(self, name):
        self.name= name