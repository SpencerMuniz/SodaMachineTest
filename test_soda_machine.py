import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """ Test the fill register method """

    def setUp(self):
        self.register = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        lenght = len(self.register.register)
        self.assertEqual(88,lenght)

class TestFillInventory(unittest.TestCase):
    """ Test the fill inventory method """

    def setUp(self):
        self.inventory = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        lenght = len(self.inventory.inventory)
        self.assertEqual(30,lenght)

class TestGetCoinFromRegister(unittest.TestCase):
    """ Test the get coin from register method """

    def setUp(self):
        self.coins_from_register = SodaMachine()

    def test_get_coins_from_register(self):
        """ Test that each type of coinn can be returned from register """
        
        self.assertEqual(


        



if __name__ == '__main__':
    unittest.main()