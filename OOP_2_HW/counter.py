import functools

def instances_counter(cls):

	setattr(cls,'instance' , 0)
	
	def counter__init__(self, *args, **kwargs):
		cls.instance += 1
		
	setattr(cls,'__init__' , counter__init__)
	
	def get(*args, **kwargs):
		return cls.instance
		
	def reset(*args, **kwargs):
		last_instance = cls.instance
		cls.instance = 0 
		return last_instance
	
	setattr(cls, 'get_created_instances', get)
	setattr(cls, 'reset_instances_counter', reset)
	
	return cls 

@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()
    user, user_1, user_2 = User(), User(), User()
    user.get_created_instances()
    user.reset_instances_counter()
