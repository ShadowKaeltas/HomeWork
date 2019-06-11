from datetime import datetime, time, date

class homework():	
	
	def __init__ (self, text, final):			
		self.text = text
		self.created = datetime.now(tz = None)
		self.deadline = datetime(self.created.year ,self.created.month,
		 self.created.day + final, self.created.hour,
		 self.created.minute, self.created.second,
		 self.created.microsecond ) - self.created 			

	def is_active(self):						
		return self.deadline

class Student():
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def do_homework(self,homework):
		if homework.is_active():
			return homework
		else:
			return "You are late"
			
class Teacher():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def create_homework(self,text, days):
		return homework(text, days)
				
if __name__ == '__main__':
	teacher = Teacher('Daniil', 'Shadrin')
	student = Student('Roman', 'Petrov')	
	teacher.last_name
	student.first_name
	
	expired_homework = teacher.create_homework('Learn functions', 0)
	expired_homework.created
	expired_homework.deadline
	expired_homework.text
	
	create_homework_too = teacher.create_homework
	oop_homework = create_homework_too('create 2 simple classes', 5)
	oop_homework.deadline
	
	student.do_homework(oop_homework)
	student.do_homework(expired_homework)
	
