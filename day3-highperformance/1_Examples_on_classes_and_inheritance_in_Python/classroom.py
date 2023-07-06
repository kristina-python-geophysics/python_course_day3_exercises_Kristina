class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, subject_area):
        super().__init__(first_name, last_name)
        self.subject_area = subject_area

    def printNameSubject(self):
        full_name = self.get_full_name()
        print(f"{full_name}, {self.subject_area}")

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        super().__init__(first_name, last_name)
        self.course = course
	
    def printNameCourse(self):
        full_name = self.get_full_name()
        print(f"{full_name},{self.course}")
