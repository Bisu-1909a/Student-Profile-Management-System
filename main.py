"""
Entry point of the Student Management System.
"""

import json

from services.student_service import StudentService
from utils.helper import Helper
from utils.menu import Menu
from services.report_service import ReportService
from utils.logger import Logger
from services.attendance_service import AttendanceService

Logger.info("Application Started")

def login():
    """
    Handles administrator login.
    """

    while True:

        Helper.clear_screen()
        Helper.print_header("ADMIN LOGIN")

        with open("data/admin.json", "r", encoding="utf-8") as file:
            admin = json.load(file)

        username = input("Username : ")
        password = input("Password : ")

        if (
            username == admin["username"]
            and password == admin["password"]
        ):
            print("\n✅ Login Successful!")
            Helper.pause()
            return

        print("\n❌ Invalid Username or Password!")
        Helper.pause()


def main():
    """
    Main function of the application.
    """

    login()

    while True:

        choice = Menu.main_menu()

        if choice == "1":
            StudentService.add_student()

        elif choice == "2":
            StudentService.view_students()

        elif choice == "3":

            Helper.clear_screen()
            Helper.print_header("SEARCH MENU")

            print("1. Search by Student ID")
            print("2. Search by Name")

            option = input("\nEnter your choice : ")

            if option == "1":
                 StudentService.search_by_id()

            elif option == "2":
                StudentService.search_by_name()

            else:
                print("❌ Invalid Choice")
                Helper.pause()

        elif choice == "4":
            StudentService.update_student()
            
        elif choice == "5":
            StudentService.delete_student()
            
        elif choice == "6":
            AttendanceService.mark_attendance()
            
        elif choice == "7":
            ReportService.view_statistics()
            
        elif choice == "8":
            Helper.clear_screen()
            Helper.print_header("THANK YOU")

            print("Thank you for using Student Management System.")
            print("\nDeveloped by Biswajeet Ojha")
            print("\nSee you again!")
            Helper.pause()
            break


if __name__ == "__main__":
    main()
    