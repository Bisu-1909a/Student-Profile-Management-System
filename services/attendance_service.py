"""
Handles student attendance operations.
"""

from services.file_service import FileService
from services.student_service import StudentService
from utils.helper import Helper
from utils.logger import Logger


class AttendanceService:
    """
    Handles attendance-related operations.
    """

    @staticmethod
    def mark_attendance():
        """
        Mark attendance for a student.
        """

        Helper.clear_screen()
        Helper.print_header("MARK ATTENDANCE")

        student_id = input("Enter Student ID : ").strip()

        # Check whether student exists
        student = StudentService.find_student_by_id(student_id)

        if student is None:
            print("\n❌ Student not found.")
            Helper.pause()
            return

        today = Helper.current_date()

        # Read today's attendance records
        attendance = FileService.read_attendance()

        # Prevent duplicate attendance
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

        choice = input("\nEnter choice : ").strip()

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

        # Save attendance
        FileService.append_attendance(
            student_id,
            today,
            status
        )

        # Log attendance
        Logger.info(
            f"Attendance Marked | "
            f"ID={student.student_id} | "
            f"Name={student.name} | "
            f"Date={today} | "
            f"Status={status}"
        )

        print("\n✅ Attendance marked successfully!")

        Helper.pause()