"""
Handles admin login using credentials stored in data/admin.json.
"""

import json
from pathlib import Path

from utils.helper import Helper
from utils.logger import Logger


class AuthService:
    """
    Handles authentication for the Student Management System.
    """

    ADMIN_FILE = Path("data/admin.json")

    @staticmethod
    def login():
        """
        Authenticate the admin user.
        Returns True if login is successful, otherwise False.
        """

        Helper.clear_screen()
        Helper.print_header("ADMIN LOGIN")

        # Load admin credentials
        try:
            with open(AuthService.ADMIN_FILE, "r", encoding="utf-8") as file:
                admin = json.load(file)

        except FileNotFoundError:
            print("❌ admin.json file not found.")
            Logger.error("Login failed: admin.json file not found.")
            Helper.pause()
            return False

        except json.JSONDecodeError:
            print("❌ admin.json contains invalid JSON.")
            Logger.error("Login failed: Invalid JSON in admin.json.")
            Helper.pause()
            return False

        # Get user input
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        # Validate credentials
        if (
            username == admin["username"]
            and password == admin["password"]
        ):

            Logger.info(f"Admin Login | Username={username}")

            print("\n✅ Login Successful!")

            Helper.pause()

            return True

        # Failed login
        Logger.warning(f"Failed Login Attempt | Username={username}")

        print("\n❌ Invalid Username or Password.")

        Helper.pause()

        return False