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
				

