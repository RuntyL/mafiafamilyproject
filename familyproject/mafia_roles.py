from family_member import FamilyMember

class Soldier(FamilyMember):

    def execute_order(self, target):
        print(f"{self.name} is executing an order on {target}.")

    def collect_revenue(self):
        print(f"{self.name} is collecting revenue for the family.")
        return 1000

class Caporegime(FamilyMember):

    def __init__(self, name):
        super().__init__(name)
        self.soldiers = []

    def add_soldier(self, soldier):
        self.soldiers.append(soldier)

    def execute_order(self, target):
        print (f"{self.name} is giving an order to execute on {target}.")

        for soldier in self.soldiers:
            soldier.execute_order(target)

    def collect_revenue(self):
        print (f"{self.name} is collecting revenue from his soldiers.")

        total = 0

        for soldier in self.soldiers: 
            total += soldier.collect_revenue()

        return total * 0.8

class Consigliere(FamilyMember):
    def execute_order(self, target):
        print(f"{self.name} is advising on an order to execute on {target}.")

    def collect_revenue(self):
        print(f"{self.name} manages legal business income.")
        return 5000

class Don(FamilyMember):
    def __init__(self, name):
        super().__init__(name)
        self.capos = []

    def add_capo(self, capo):
        self.capos.append(capo)

    def execute_order(self, target):
        print(f"{self.name} is giving an order to execute on {target}.")

        for capo in self.capos:
            capo.execute_order(target)

    def collect_revenue(self):
        print(f"{self.name} is collecting revenue from his capos.")

        total = 0

        for capo in self.capos:
            total += capo.collect_revenue()

        return total * 0.8
            

       
