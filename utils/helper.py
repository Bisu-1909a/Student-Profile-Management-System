"""
Contains reusable helper functions used throughout
the Student Management System.
"""

import os
from datetime import datetime


class Helper:
    """
    Utility helper functions.
    """

    @staticmethod
    def clear_screen():
        """
        Clears the terminal screen.
        Works on Windows and Linux/macOS.
        """
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def pause():
        """
        Pause the program until the user presses Enter.
        """
        input("\nPress Enter to continue...")

    @staticmethod
    def print_header(title):
        """
        Prints a formatted title/header.
        """

        print("\n" + "=" * 50)
        print(title.center(50))
        print("=" * 50)

    @staticmethod
    def current_date():
        """
        Returns today's date.
        """
        from datetime import datetime
        return datetime.now().strftime("%d-%m-%Y")

        