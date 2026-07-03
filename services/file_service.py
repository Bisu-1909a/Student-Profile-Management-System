"""
Handles all CSV file operations for Student Management System.
"""

import csv
from pathlib import Path

from models.student import Student


class FileService:
    """
    Handles reading and writing student data to CSV files.
    """

    DATA_FILE = Path("data/students.csv")
    ATTENDANCE_FILE = Path("data/attendance.csv")

    @classmethod
    def read_students(cls):
        """
        Read all students from CSV.
        Returns a list of Student objects.
        """

        students = []

        if not cls.DATA_FILE.exists():
            return students

        with open(cls.DATA_FILE, mode="r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(Student.from_dict(row))

        return students

    @classmethod
    def write_students(cls, students):
        """
        Overwrite CSV with a list of Student objects.
        """

        with open(cls.DATA_FILE, mode="w", newline="", encoding="utf-8") as file:

            fieldnames = [
                "student_id",
                "name",
                "age",
                "gender",
                "course",
                "semester",
                "email",
                "phone",
                "marks",
                "attendance",
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())

    @classmethod
    def append_student(cls, student):
        """
        Add one new student to CSV.
        """

        students = cls.read_students()

        students.append(student)

        cls.write_students(students)

    @classmethod
    def update_student(cls, updated_student):
        """
        Update an existing student.
        """

        students = cls.read_students()

        for index, student in enumerate(students):

            if student.student_id == updated_student.student_id:
                students[index] = updated_student
                break

        cls.write_students(students)

    @classmethod
    def delete_student(cls, student_id):
        """
        Delete a student using student ID.
        """

        students = cls.read_students()

        students = [
            student
            for student in students
            if student.student_id != student_id
        ]

        cls.write_students(students)
        
    @staticmethod
    def save_all_students(students):
        """
        Overwrite students.csv with the updated student list.
        """

        with open(
            FileService.DATA_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "student_id",
                    "name",
                    "age",
                    "gender",
                    "course",
                    "semester",
                    "email",
                    "phone",
                    "marks",
                    "attendance",
                ],
            )

            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())
                
    @staticmethod
    def read_attendance():
        """
        Read all attendance records.
        """

        attendance = []

        with open(
            FileService.ATTENDANCE_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                attendance.append(row)

        return attendance
    
    
    @staticmethod
    def append_attendance(student_id, date, status):
        """
        Save attendance into attendance.csv
        """

        with open(
            FileService.ATTENDANCE_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                student_id,
                date,
                status
            ])
            