import unittest

from crypto.challenge import set_one as one
from .test_helper import get_file_as_str, DIR_PATH


class TestChallengeSetOne(unittest.TestCase):
    path = f'{DIR_PATH}/data/set_one'

    def test__set_1_challenge_1__valid(self):
        in_ = get_file_as_str(f'{self.path}/1_in.txt')
        expected = get_file_as_str(f'{self.path}/1_sol.txt').encode()

        output = one.challenge_one(in_)

        self.assertEqual(expected, output)

        print(output)

    def test__set_1_challenge_2__valid(self):
        in_ = get_file_as_str(f'{self.path}/2_in_p1.txt')
        xor = get_file_as_str(f'{self.path}/2_in_p2.txt')
        expected = bytes.fromhex(get_file_as_str(f'{self.path}/2_sol.txt'))

        output = one.challenge_two(in_, xor)

        self.assertEqual(expected, output)

        print(output)

    def test__set_1_challenge_3__valid(self):
        in_ = get_file_as_str(f'{self.path}/3_in.txt')
        expected = get_file_as_str(f'{self.path}/3_sol.txt').encode()

        output = one.challenge_three_own_sol(in_)

        self.assertEqual(expected, output)

        print(output)

    def test__set_1_challenge_4__valid(self):
        in_ = []
        expected = get_file_as_str(f'{self.path}/4_sol.txt').encode()
        with open(f'{self.path}/4_in.txt') as file:
            for line in file:
                line = line.rstrip()
                in_.append(line.encode())

            output = one.challenge_four(in_)

            self.assertEqual(expected, output)
            print(output)

    def test__set_1__challenge_5__valid(self):
        in_ = get_file_as_str(f'{self.path}/5_in_p1.txt')
        in_key = get_file_as_str(f'{self.path}/5_in_p2.txt')
        expected = get_file_as_str(f'{self.path}/5_sol.txt')

        output = one.challenge_five(in_, in_key)

        self.assertEqual(expected, output)

        print(output)
