"""
Contains all menu screens for the Student Management System.
"""

from utils.helper import Helper


class Menu:
    """
    Displays all menus.
    """

    @staticmethod
    def main_menu():
        
        Helper.clear_screen()
        Helper.print_header("STUDENT MANAGEMENT SYSTEM")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Mark Attendance")
        print("7. View Statistics")
        print("8. Exit")

        print("-" * 50)

        choice = input("Enter your choice (1-8): ")

        return choice
    