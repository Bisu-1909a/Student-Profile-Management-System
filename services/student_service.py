"""
Contains all student-related business logic.
"""

from unicodedata import name

from models import student
from models.student import Student
from services.file_service import FileService
from utils.validator import Validator
from utils.helper import Helper
from utils.logger import Logger


class StudentService:
    """
    Handles all student operations.
    """

    @staticmethod
    def add_student():

        Helper.clear_screen()
        Helper.print_header("ADD STUDENT")

        while True:
            student_id = input("Enter Student ID : ")

            if Validator.validate_student_id(student_id):
                break
            
        if StudentService.find_student_by_id(student_id):
            print("\n❌ Student ID already exists.")

            Helper.pause()  
            return
        
        while True:
            name = input("Enter Name : ")

            if Validator.validate_name(name):
                break

        while True:

            try:
                age = int(input("Enter Age : "))

                if Validator.validate_age(age):
                    break

            except ValueError:
                print("❌ Age must be a number.")

        gender = input("Enter Gender : ")
        course = input("Enter Course : ")
        semester = int(input("Enter Semester : "))

        while True:
            email = input("Enter Email : ")

            if Validator.validate_email(email):
                break

        while True:
            phone = input("Enter Phone : ")

            if Validator.validate_phone(phone):
                break

        marks = int(input("Enter Marks : "))
        attendance = float(input("Enter Attendance : "))

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            gender=gender,
            course=course,
            semester=semester,
            email=email,
            phone=phone,
            marks=marks,
            attendance=attendance,
        )

        FileService.append_student(student)
        
        Logger.info(
            f"Student Added | "
            f"ID={student.student_id} | "
            f"Name={student.name} | "
            f"Course={student.course} | "
            f"Semester={student.semester}"
        )

        print("\n✅ Student added successfully!")
        
        Helper.pause()

    @staticmethod
    def view_students():
        """
        Display all students.
        """

        Helper.clear_screen()
        Helper.print_header("STUDENT LIST")

        students = FileService.read_students()

        if not students:
            print("No students found.\n")
            return

        for student in students:
            student.display()
            
        Helper.pause()
         

    @staticmethod
    def search_by_name():
        """
        Search students using Name.
        """

        Helper.clear_screen()
        Helper.print_header("SEARCH BY NAME")

        name = input("Enter Student Name : ").strip().lower()

        students = FileService.read_students()

        found = False

        for student in students:

            if name in student.name.lower():

                student.display()
                found = True

        if not found:
            print("\n❌ No student found.")

        Helper.pause()
        
    @staticmethod
    def find_student_by_id(student_id):
        """
        Returns the Student object if found,
        otherwise returns None.
        """

        students = FileService.read_students()

        for student in students:
            if student.student_id == student_id:
                return student

        return None
        
    @staticmethod
    def search_by_id():

        Helper.clear_screen()
        Helper.print_header("SEARCH STUDENT")

        student_id = input("Enter Student ID : ").strip()

        student = StudentService.find_student_by_id(student_id)

        if student:
            print("\n✅ Student Found!\n")
            student.display()
        else:
            print("\n❌ Student not found.")

        Helper.pause()
        
    @staticmethod
    def update_student():
        """
        Update an existing student's details.
        """

        Helper.clear_screen()
        Helper.print_header("UPDATE STUDENT")

        student_id = input("Enter Student ID : ").strip()

        students = FileService.read_students()

        student_to_update = None

        for student in students:
            if student.student_id == student_id:
                student_to_update = student
                break

        if student_to_update is None:
            print("\n❌ Student not found.")
            Helper.pause()
            return

        print("\nCurrent Student Details:\n")
        student_to_update.display()

        print("\nPress Enter to keep the current value.\n")

        # ---------------- Name ----------------
        while True:
            name = input(f"Name [{student_to_update.name}] : ").strip()

            if name == "":
                break

            if Validator.validate_name(name):
                student_to_update.name = name
                break

        # ---------------- Age ----------------
        while True:
            age = input(f"Age [{student_to_update.age}] : ").strip()

            if age == "":
                break

            try:
                age = int(age)

                if Validator.validate_age(age):
                    student_to_update.age = age
                    break

            except ValueError:
                print("❌ Invalid age.")

        # ---------------- Email ----------------
        while True:
            email = input(f"Email [{student_to_update.email}] : ").strip()

            if email == "":
                break

            if Validator.validate_email(email):
                student_to_update.email = email
                break

        # ---------------- Phone ----------------
        while True:
            phone = input(f"Phone [{student_to_update.phone}] : ").strip()

            if phone == "":
                break

            if Validator.validate_phone(phone):
                student_to_update.phone = phone
                break

        FileService.save_all_students(students)
        
        Logger.info(
                f"Student Updated | "
                f"ID={student.student_id} | "
                f"Name={student.name}"
            )

        print("\n✅ Student updated successfully!")

        Helper.pause()
        
    @staticmethod
    def delete_student():
        """
        Delete a student by Student ID.
        """

        Helper.clear_screen()
        Helper.print_header("DELETE STUDENT")

        student_id = input("Enter Student ID : ").strip()

        students = FileService.read_students()

        student_to_delete = StudentService.find_student_by_id(student_id)

        if student_to_delete is None:
            print("\n❌ Student not found.")
            Helper.pause()
            return

        print("\nStudent Found:\n")
        student_to_delete.display()

        confirm = input("\nAre you sure you want to delete this student? (Y/N): ").strip().upper()

        if confirm != "Y":
            print("\nDeletion cancelled.")
            Helper.pause()
            return

        updated_students = [
            student
            for student in students
            if student.student_id != student_id
        ]

        FileService.save_all_students(updated_students)
        
        Logger.info(
                f"Student Deleted | ID={student_id}"
            )

        print("\n✅ Student deleted successfully!")

        Helper.pause()
                    
    @staticmethod
    def mark_attendance():
        """
        Mark attendance for a student.
        """

        Helper.clear_screen()
        Helper.print_header("MARK ATTENDANCE")

        student_id = input("Enter Student ID : ").strip()

        student = StudentService.find_student_by_id(student_id)

        if student is None:
            print("\n❌ Student not found.")
            Helper.pause()
            return

        today = Helper.current_date()

        attendance = FileService.read_attendance()

        for record in attendance:

            if (
                record["student_id"] == student_id
                and record["date"] == today
            ):
                print("\n❌ Attendance already marked for today.")
                Helper.pause()
                return

        print("\nStudent Found\n")
        student.display()

        print("\nAttendance Status")
        print("1. Present")
        print("2. Absent")
        print("3. Leave")

        choice = input("\nEnter choice : ")

        status_map = {
            "1": "Present",
            "2": "Absent",
            "3": "Leave"
        }

        status = status_map.get(choice)

        if status is None:
            print("\n❌ Invalid choice.")
            Helper.pause()
            return

        FileService.append_attendance(
            student_id,
            today,
            status
        )
        
        Logger.info(
            f"Attendance Marked | "
            f"ID={student_id} | "
            f"Name={student.name} | "
            f"Date={today} | "
            f"Status={status}"
        )


        print("\n✅ Attendance marked successfully!")

        Helper.pause()