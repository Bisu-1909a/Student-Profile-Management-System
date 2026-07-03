import unittest

from utils.validator import Validator


class TestValidator(unittest.TestCase):

    def test_email(self):
        self.assertTrue(
            Validator.validate_email("abc@gmail.com")
        )

    def test_phone(self):
        self.assertTrue(
            Validator.validate_phone("9876543210")
        )


if __name__ == "__main__":
    unittest.main()
    