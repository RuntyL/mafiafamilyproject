import unittest
from mafia_roles import Soldier, Caporegime, Consigliere, Don
class TestSoldier(unittest.TestCase):
     
    def test_soldier(self):
        def test_revenue(self):
            soldier = Soldier("Vito")
            self.assertEqual(soldier.collect_revenue(), 1000)

class TestCapo(unittest.TestCase):

    def test_no_soldier(self):
        def test_revenue(self):
            capo = Caporegime("Sonny")
            self.assertEqual(capo.collect_revenue(), 0)

    def test_one_soldier(self):
        def test_revenue(self):
            capo = Caporegime("Sonny")
            capo.add_soldier(Soldier("Vito"))
            self.assertEqual(capo.collect_revenue(), 800)

    def test_two_soldier(self):
        def test_revenue(self):
            capo = Caporegime("Sonny")
            capo.add_soldier(Soldier("Vito"))
            capo.add_soldier(Soldier("Marco"))
            self.assertEqual(capo.collect_revenue(), 1600)

class TestConsigliere(unittest.TestCase):

    def test_revenue(self):
        consigliere = Consigliere("Tom")
        self.assertEqual(consigliere.collect_revenue(), 5000)

class TestDon(unittest.TestCase):

    def test_no_capos(self):
        don = Don("Michael")
        self.assertEqual(don.collect_revenue(), 0)

    def test_one_capo(self):
        capo = Caporegime("Sonny")
        capo.add_soldier(Soldier("Vito"))
        don = Don("Michael")
        don.add_capo(capo)
        self.assertEqual(don.collect_revenue(), 640)

    def test_two_capos(self):
        capo1 = Caporegime("Sonny")
        capo1.add_soldier(Soldier("Vito"))
        capo2 = Caporegime("Fredo")
        capo2.add_soldier(Soldier("Marco"))
        don = Don("Michael")
        don.add_capo(capo1)
        don.add_capo(capo2)
        self.assertEqual(don.collect_revenue(), 1280)


if __name__ == '__main__':
    unittest.main()