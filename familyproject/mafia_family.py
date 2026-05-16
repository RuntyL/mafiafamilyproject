class MafiaFamily:
    def __init__(self,family_name):
        self.family_name = family_name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def show_members(self):
        print(f"Members of the {self.family_name} family:")

        for member in self.members:
            member.intro()

    def family_income(self):
        total_income = 0

        for member in self.members:
            total_income += member.collect_revenue()

        print(f"\nTotal income for the {self.family_name} family: ${total_income:.2f}")