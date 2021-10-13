import unittest
from coins import Dime, Nickel, Penny, Quarter
import user_interface
from cans import Cola, OrangeSoda, RootBeer


class TestValidateMainMenu(unittest.TestCase):
    def test_validate_main_menu(self):
        answer_one = user_interface.validate_main_menu(1)
        self.assertEqual(answer_one, (True, 1))
    def test_validate_main_menu_two(self):
        answer_two = user_interface.validate_main_menu(2)
        self.assertEqual(answer_two, (True, 2))
    def test_validate_main_menu_three(self):
        answer_three = user_interface.validate_main_menu(3)
        self.assertEqual(answer_three, (True, 3))
    def test_validate_main_menu_four(self):
        answer_four = user_interface.validate_main_menu(4)
        self.assertEqual(answer_four, (True, 4))
    def test_validate_main_menu_five(self):
        answer_five = user_interface.validate_main_menu(5)
        self.assertEqual(answer_five, (False, None))

class TestTryParseInt(unittest.TestCase):
    def test_try_parse_int(self):
        answer = user_interface.try_parse_int("10")
        self.assertEqual(answer, 10)
    def test_try_parse_int_word(self):
        answer = user_interface.try_parse_int("hello")
        self.assertEqual(answer, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    def test_get_unique_can_names(self):
        cola = Cola()
        root_beer = RootBeer()
        orange_soda = OrangeSoda()
        list_of_soda = [cola, cola, orange_soda, orange_soda, root_beer, root_beer]
        unique_cans = user_interface.get_unique_can_names(list_of_soda)
        self.assertEqual(len(unique_cans), 3)

    def test_get_unique_can_names_no_cans(self):
        list_of_soda = []
        unique_cans = user_interface.get_unique_can_names(list_of_soda)
        self.assertEqual(len(unique_cans), 0)

class TestDisplayPaymentValue(unittest.TestCase):
    def test_display_payment_value(self):
        penny = Penny()
        nickel = Nickel()
        dime = Dime()
        quarter = Quarter()
        list_of_money = [penny, nickel, dime, quarter]
        total_value = user_interface.display_payment_value(list_of_money)
        self.assertEqual(total_value, .41) 

    def test_display_payment_value_of_nothing(self):
        list_of_money = []
        total_value = user_interface.display_payment_value(list_of_money)
        self.assertEqual(total_value, 0) 


class TestValidateCoinSelection(unittest.TestCase):
    def test_validate_coin_selection(self):
        answer_one = user_interface.validate_coin_selection(1)
        self.assertEqual(answer_one, (True, "Quarter"))
    def test_validate_coin_selection_two(self):
        answer_two = user_interface.validate_coin_selection(2)
        self.assertEqual(answer_two, (True, "Dime"))
    def test_validate_coin_selection_three(self):
        answer_three = user_interface.validate_coin_selection(3)
        self.assertEqual(answer_three, (True, "Nickel"))
    def test_validate_coin_selection_four(self):
        answer_four = user_interface.validate_coin_selection(4)
        self.assertEqual(answer_four, (True, "Penny"))
    def test_validate_coin_selection_five(self):
        answer_five = user_interface.validate_coin_selection(5)
        self.assertEqual(answer_five, (True, "Done"))
    def test_validate_coin_selection_six(self):
        answer_six = user_interface.validate_coin_selection(6)
        self.assertEqual(answer_six, (False, None))

if __name__ == '__main__':
    unittest.main()