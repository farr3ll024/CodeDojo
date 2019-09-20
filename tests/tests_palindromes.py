import unittest

from _Palindromes import _palindromes


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome_true(self):
        self.assertTrue(_palindromes("rotator"))
        self.assertTrue(_palindromes("civic"))
        # self.assertTrue(_palindromes(userinput=input("input palindrome: ")))

    def test_is_palindrome_false(self):
        self.assertFalse(_palindromes("hello"))
        self.assertFalse(_palindromes("world"))
        # self.assertFalse(_palindromes(userinput=input("input !palindrome: ")))


if __name__ == '__main__':
    unittest.main()
