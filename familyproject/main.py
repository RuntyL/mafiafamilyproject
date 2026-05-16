from mafia_roles import Soldier, Caporegime, Consigliere, Don
from mafia_family import MafiaFamily
from operations import OperationManager


# CREATE MEMBERS
soldier1 = Soldier("Vito")
soldier2 = Soldier("Marco")

capo = Caporegime("Sonny")
capo.add_soldier(soldier1)
capo.add_soldier(soldier2)

consigliere = Consigliere("Tom")

don = Don("Michael")
don.add_capo(capo)


# CREATE FAMILY
family = MafiaFamily("Corleone")

family.add_member(don)
family.add_member(consigliere)


# SHOW MEMBERS
family.show_members()


# START OPERATION
OperationManager.start_operation("Rival Family")

OperationManager.status_operation("Rival Family")

don.execute_order("Rival Family")

OperationManager.finish_operation("Rival Family")


# COLLECT MONEY
family.family_income()