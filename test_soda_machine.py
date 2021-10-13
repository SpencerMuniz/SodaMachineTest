from _typeshed import Self
import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """ Test the fill register method """

    def setUp(self):
        self.register = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        length = len(self.register.register)
        self.assertEqual(88,length)

class TestFillInventory(unittest.TestCase):
    """ Test the fill inventory method """

    def setUp(self):
        self.inventory = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        length = len(self.inventory.inventory)
        self.assertEqual(30,length)

class TestGetCoinFromRegister(unittest.TestCase):
    """ Test the get coin from register method """

    def setUp(self):
        self.coins_from_register = SodaMachine()

    def test_get_coins_from_register_quarter(self):
        """ Test that Quarter can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Quarter')
        self.assertEqual('Quarter', coin.name)

    def test_get_coins_from_register_dime(self):
        """ Test that Dime can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Dime')
        self.assertEqual('Dime', coin.name)
    
    def test_get_coins_from_register_nickel(self):
        """ Test that Nickel can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Nickel')
        self.assertEqual('Nickel', coin.name)
    
    def test_get_coins_from_register_penny(self):
        """ Test that Penny can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Penny')
        self.assertEqual('Penny', coin.name)

    def test_get_coins_from_register_none(self):
        """ Test that None type can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('test_coin')
        self.assertIsNone(coin)
        

    class test_register_has_coins(unittest.TestCase):
        """ Test types of coins that can be returned from the register"""
        def setUp(self):
            self.register_has_coins = SodaMachine() 

        def 



if __name__ == '__main__':
    unittest.main()