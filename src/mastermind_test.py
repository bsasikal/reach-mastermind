import unittest
from unittest import mock
from unittest.mock import patch

from mastermind import *


class TestMasterMind(unittest.TestCase):

    def test_generate_random_number(self):
        random_num, random_list = generate_random_number(3)
        self.assertTrue(len(str(random_num)) == 3)

        random_num, random_list = generate_random_number(4)
        self.assertTrue(len(str(random_num)) == 4)

        random_num, random_list = generate_random_number(5)
        self.assertTrue(len(str(random_num)) == 5)

        random_num, random_list = generate_random_number(1)
        self.assertTrue(len(str(random_num)) == 1)

    def test_choose_game_complexity(self):
        with mock.patch('builtins.input', return_value='1'):
            self.assertTrue(choose_game_complexity() == 3)

        with mock.patch('builtins.input', return_value='2'):
            self.assertTrue(choose_game_complexity() == 4)

        with mock.patch('builtins.input', return_value='3'):
            self.assertTrue(choose_game_complexity() == 5)

        with mock.patch('builtins.input', side_effect=[0, 4, 5, 1]):
            self.assertTrue(choose_game_complexity() == 3)

        with mock.patch('builtins.input', side_effect=[0, 4, 5, 2]):
            self.assertTrue(choose_game_complexity() == 4)

        with mock.patch('builtins.input', side_effect=[0, 4, 5, 3]):
            self.assertTrue(choose_game_complexity() == 5)

    def test_guess_the_number(self):
        with mock.patch('builtins.input', return_value='111'):
            self.assertTrue(guess_the_number(3) == '111')

        with mock.patch('builtins.input', return_value='5678'):
            self.assertTrue(guess_the_number(4) == '5678')

        with mock.patch('builtins.input', return_value='22334'):
            self.assertTrue(guess_the_number(5) == '22334')

        with mock.patch('builtins.input', side_effect=[11, 22, 333, 0]):
            self.assertTrue(guess_the_number(3) == '333')

        with mock.patch('builtins.input', side_effect=[1, 22, 333, 4444]):
            self.assertTrue(guess_the_number(4) == '4444')

        with mock.patch('builtins.input', side_effect=[1, 22, 333, 4444, 55555]):
            self.assertTrue(guess_the_number(5) == '55555')

        with mock.patch('builtins.input', side_effect=['AA', 'AAAA', 'AAAA', 'AAAAA', 55555]):
            self.assertTrue(guess_the_number(5) == '55555')

        with mock.patch('builtins.input', side_effect=['', '@#@#', '32432423', '232132132121', 5]):
            self.assertTrue(guess_the_number(1) == '5')


if __name__ == '__main__':
    unittest.main()
