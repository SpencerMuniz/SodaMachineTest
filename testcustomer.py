import unittest
from customer import Customer
from wallet import Wallet

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin_method"""
    def setUp(self):
        self.customer = Customer()


    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)
        
    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)
       
    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_can_return_none(self):
        """Pass in any '' other than a coin, method should return a none instance"""
        returned_coin = self.customer.get_wallet_coin('Quartr')
        self.assertIsNone(returned_coin)

class TestAddCoinsToWallet(unittest.TestCase):
    """Test's for adding coins to Customer's wallet"""

    def setUp(self):
        self.customer = Customer()
        #self.wallet = Wallet()

    def test_add_coins_to_wallet(self):
        """Pass in list of three coins, method should return the updated list"""
        coins = ["Quarter", "Quarter", "Dime"]
        self.customer.add_coins_to_wallet(coins)
        length = len(self.wallet.money)
        self.assertEqual(length, len(coins))
        


if __name__ == '__main__':
    unittest.main()