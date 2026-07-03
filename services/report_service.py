from services.file_service import FileService
from utils.helper import Helper

class ReportService:
    """
    Handles reports and statistics.
    """
    
    @staticmethod
    def view_statistics():
        """
        Displays statistics about students.
        """

        Helper.clear_screen()
        Helper.print_header("STUDENT STATISTICS")

        students = FileService.read_students()

        total_students = len(students)
        average_age = (
            sum(student.age for student in students) / total_students
            if total_students > 0
            else 0
        )
        
        male_students = sum(1 for student in students if student.gender.lower() == "male")      
        female_students = sum(1 for student in students if student.gender.lower() == "female") 
        total_marks = sum(student.marks for student in students)
        average_marks = total_marks / total_students
        highest_marks = max(student.marks for student in students)
        lowest_marks = min(student.marks for student in students) 
        average_attendance = (sum(student.attendance for student in students)/ total_students if total_students > 0 else 0)
        topper = max(students,key=lambda student: student.marks)
        grades = {
        "A+": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
        }
        for student in students:
            grade = student.calculate_grade()
            grades[grade] += 1
        
            print("=" * 55)
            print(f"\n👨‍🎓 Total Students        : {total_students}")
            print(f"👦 Male Students         : {male_students}")
            print(f"👧 Female Students       : {female_students}")

            print("-" * 55)
            print(f"📚 Average Marks         : {average_marks:.2f}")
            print(f"🏆 Highest Marks         : {highest_marks}")
            print(f"📉 Lowest Marks          : {lowest_marks}")
            print(f"📊 Average Attendance    : {average_attendance:.2f}%")
            print(f"⭐ Top Performer         : {topper.name}")

            print("-" * 55)
            print("\n🎖 Grade Distribution\n")

            for grade, count in grades.items():
                print(f"{grade:<2} : {'█' * count} ({count})")

            print("\n" + "=" * 55)

            Helper.pause()