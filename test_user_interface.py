import unittest
import user_interface
from cans import Cola, OrangeSoda, RootBeer


class TestValidateMainMenu(unittest.TestCase):
    def test_validate_main_menu(self):
        answer_one = user_interface.validate_main_menu(1)
        self.assertEquals(answer_one, (True, 1))
    def test_validate_main_menu(self):
        answer_two = user_interface.validate_main_menu(2)
        self.assertEquals(answer_two, (True, 2))
    def test_validate_main_menu(self):
        answer_three = user_interface.validate_main_menu(3)
        self.assertEquals(answer_three, (True, 3))
    def test_validate_main_menu(self):
        answer_four = user_interface.validate_main_menu(4)
        self.assertEquals(answer_four, (True, 4))
    def test_validate_main_menu(self):
        answer_five = user_interface.validate_main_menu(5)
        self.assertEqual(answer_five, (False, None))

class TestTryParseInt(unittest.TestCase):
    def test_try_parse_int(self):
        answer = user_interface.try_parse_int("10")
        print(answer)
    def test_try_parse_int(self):
        answer = user_interface.try_parse_int("hello")
        print(answer)

class TestGetUniqueCanNames(unittest.TestCase):
    def test_get_unique_can_names(self):
        cola = Cola()
        root_beer = RootBeer()
        orange_soda = OrangeSoda()
        list_of_soda = [cola, cola, orange_soda, orange_soda, root_beer, root_beer]
        print(user_interface.get_unique_can_names(list_of_soda))



if __name__ == '__main__':
    unittest.main()