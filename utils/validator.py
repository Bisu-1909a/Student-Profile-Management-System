"""
Contains input validation functions for the Student Management System.
"""

import re


class Validator:
    """
    Performs validation on user input.
    """

    @staticmethod
    def validate_student_id(student_id: str) -> bool:
        """
        Validate Student ID.
        """

        if not student_id.strip():
            print("❌ Student ID cannot be empty.")
            return False

        if not student_id.isdigit():
            print("❌ Student ID should contain only digits.")
            return False

        return True

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validate student name.
        """

        if not name.strip():
            print("❌ Name cannot be empty.")
            return False

        if not all(char.isalpha() or char.isspace() for char in name):
            print("❌ Name should contain only letters and spaces.")
            return False

        return True

    @staticmethod
    def validate_age(age: int) -> bool:
        """
        Validate age.
        """

        if age < 16 or age > 100:
            print("❌ Age must be between 16 and 100.")
            return False

        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address.
        """

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.fullmatch(pattern, email):
            print("❌ Invalid email address.")
            return False

        return True

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate phone number.
        """

        if not phone.isdigit():
            print("❌ Phone number should contain only digits.")
            return False

        if len(phone) != 10:
            print("❌ Phone number must contain exactly 10 digits.")
            return False

        return True
    