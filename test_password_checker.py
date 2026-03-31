import unittest
from password_checker import check_password_strength

class TestPasswordChecker(unittest.TestCase):

    def test_weak_password(self):
        password = "abc"
        result = check_password_strength(password)
        self.assertEqual(result, "Weak Password")

    def test_medium_password(self):
        password = "hello123"
        result = check_password_strength(password)
        self.assertEqual(result, "Medium Password")

    def test_strong_password(self):
        password = "Strong@123"
        result = check_password_strength(password)
        self.assertEqual(result, "Strong Password")

if __name__ == "__main__":
    unittest.main()
