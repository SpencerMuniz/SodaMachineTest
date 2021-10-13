import unittest
from wallet import Wallet



class TestFillWallet(unittest.TestCase):
    """ Test the fill wallet method """

    def setUp(self):
        self.wallet = Wallet()

    def test_fill_wallet(self):
        """ Test the length of the wallet object """
        lenght = len(self.wallet.money)
        self.assertEqual(88,lenght)

        



if __name__ == '__main__':
    unittest.main()

