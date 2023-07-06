class Student(Person):
	def __init__(self, first_name, last_name, subject_area):
		super().__init__(first_name, last_name)
		self.subject_area = subject_area
		
	def printNameSubject(self):
	full_name = self.get_full_name()
	print(f"{full_name},{self.subject_area}")
