from abc import ABC, abstractmethod

class FamilyMember(ABC):
    def __init__(self, name):
        self.name= name

    @abstractmethod
    def execute_order (self, target):
        pass
    
    def collect_revenue (self):
        pass

    def intro (self):
        print(f"Hi, I'm {self.name} and I'm a member of the family.")