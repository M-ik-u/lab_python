class Student(object):
    student_quantity = 0

    @classmethod
    def incr_std(cls):
        Student.student_quantity = Student.student_quantity + 1

    def __init__(self, name, course, grades):
        self.grades = grades
        self.name = name
        self.course = course
        self.incr_std()

    def avg_score_subject(self, subject):
        sum = 0
        for i in self.grades[subject]:
            sum = sum + i
        return float(sum/len(self.grades[subject]))

    def is_honors_student(self):
        for i in self.grades.keys():
            if self.avg_score_subject(i) < 8.5:
                return False
        return True

if __name__ == "__main__":
    student = Student("Anna", 2, {"programming": [9, 8, 10, 8, 10], "FE": [9, 8, 10, 9, 8]})

    print(student.is_honors_student())
    print(student.avg_score_subject("programming"))
