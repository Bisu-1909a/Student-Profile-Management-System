import unittest

from models.student import Student


class TestStudent(unittest.TestCase):

    def test_percentage(self):
        student = Student(
            "101",
            "Test",
            20,
            "Male",
            "B.Tech",
            6,
            "test@example.com",
            "9876543210",
            450,
            90
        )

        self.assertEqual(student.calculate_percentage(), 90.0)

    def test_grade(self):
        student = Student(
            "101",
            "Test",
            20,
            "Male",
            "B.Tech",
            6,
            "test@example.com",
            "9876543210",
            450,
            90
        )

        self.assertEqual(student.calculate_grade(), "A+")


if __name__ == "__main__":
    unittest.main()
    