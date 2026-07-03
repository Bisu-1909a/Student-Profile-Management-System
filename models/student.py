"""
Contains the Student model.
One object of this class represents one student.
"""

class Student:
    # Represents a student in the Student Management System.
   
    TOTAL_MARKS = 500

    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        gender: str,
        course: str,
        semester: int,
        email: str,
        phone: str,
        marks: int = 0,
        attendance: float = 0.0,
    ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.semester = semester
        self.email = email
        self.phone = phone
        self.marks = marks
        self.attendance = attendance

    # -------------------------
    # Percentage Calculation
    # -------------------------

    def calculate_percentage(self):
        return round((self.marks / Student.TOTAL_MARKS) * 100, 2)

    # -------------------------
    # Grade Calculation
    # -------------------------

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        return "F"

    # -------------------------
    # Display Student
    # -------------------------

    def display(self):

        print("\n========== Student Details ==========\n")

        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Course     : {self.course}")
        print(f"Semester   : {self.semester}")
        print(f"Email      : {self.email}")
        print(f"Phone      : {self.phone}")
        print(f"Marks      : {self.marks}")
        print(f"Attendance : {self.attendance}%")
        print(f"Percentage : {self.calculate_percentage()}%")
        print(f"Grade      : {self.calculate_grade()}")

        print("=" * 36)

    # -------------------------
    # Object -> Dictionary
    # -------------------------

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "course": self.course,
            "semester": self.semester,
            "email": self.email,
            "phone": self.phone,
            "marks": self.marks,
            "attendance": self.attendance,
        }

    # -------------------------
    # Dictionary -> Object
    # -------------------------

    @classmethod
    def from_dict(cls, data):

        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=int(data["age"]),
            gender=data["gender"],
            course=data["course"],
            semester=int(data["semester"]),
            email=data["email"],
            phone=data["phone"],
            marks=int(data.get("marks", 0)),
            attendance=float(data.get("attendance", 0)),
        )