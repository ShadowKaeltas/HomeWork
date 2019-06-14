from datetime import datetime, time, date


class Person():
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
		
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


class Student(Person):
			
	def do_homework(self,homework, solution):
		assert homework.is_active() , "You're late!"
		HomeworkResult.author = self
		return HomeworkResult(homework, solution)


class HomeworkResult(homework,Student):
	
	def __init__ (self, work, solution):
		errmsg = 'You gave a not Homework object'
		assert isinstance(work, homework), errmsg
		self.work = work
		self.solution = solution 
		self.created = datetime.now(tz = None)
		
		
class Teacher(Person):
	
	global homework_done
	homework_done = {}	
	
	def __init__(self, *args, **kwargs):
		self.homework_done = homework_done
	
	def create_homework(self,text, days):
		return homework(text, days)
		
	def check_homework(self, HomeworkResult):	
		length = len(HomeworkResult.solution)	
		hwr = HomeworkResult
		key_dict = {HomeworkResult.work : []}
		if HomeworkResult.work not in homework_done:
			homework_done.update(key_dict)
		if homework_done[HomeworkResult.work] != hwr:
			if length > 5:
				homework_done[HomeworkResult.work].append(hwr)
			return True
		else:
			return False
	
	def reset_results(instance = None):
		if instance :
			del homework_done[instance]
		else:
			homework_done.clear()
