class Teacher(Person):
    def __init__(self, first_name, last_name, course):
	super().__init__(first_name, last_name)
	self.course = course
	
    def printNameCourse(self):
	full_name = self.get_full_name()
	print(f"{full_name},{self.course}")
