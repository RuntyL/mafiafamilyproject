import random

class OperationManager :
    operations = [
        "Money laundering",
        "Casino control",
        "Smuggling operation",
        "Protection business",
        "Illegal gambling"
    ]

    locations = [
        "New York",
        "Chicago",
        "Sicily",
        "Las Vegas",
        "Brooklyn"
    ]
    @staticmethod
    def start_operation(target):
        operation = random.choice(OperationManager.operations)
        location = random.choice(OperationManager.locations)

        print("\nOPERATION STARTS\n")
        print(f"Target: {target}")
        print(f"Operation: {operation}")
        print(f"Location: {location}")
        
    @staticmethod
    def status_operation(target):
        statuses = [
            "The operation is going smoothly.",
            "Police activity has increased.",
            "The rival family is resisting.",
            "Business partners are cooperating.",
            "The streets are under control."
        ]

        print(f"\nStatus Report: {random.choice(statuses)}\n")

    @staticmethod
    def finish_operation(target):
        results = [
            "Operation completed successfully.",
            "The family earned more influence.",
            "The rivals backed down.",
            "The operation generated large profits.",
            "The city fears the family even more."
        ]

        print("\nOPERATION END:",random.choice(results), end="\n\n")
        

