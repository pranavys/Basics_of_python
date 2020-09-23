my_student = {
    'name': 'ysp',
    'grades': [12, 45, 67, 89]
}

def avg_grade(stud):
    return sum(stud['grades']) / len(stud['grades'])

print(avg_grade(my_student))

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('ysp', [23, 45, 67, 89])
student_two = Student('psy', [32, 54, 67, 76])


print(student_one.name)
print(student_two.name)

print(student_one.average())
print(Student.average(student_one))#same as above

