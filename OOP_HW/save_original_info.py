import  functools 

def save_original_info(func_1):
	def save_original(func_2):
		def wrapper(*args, **kwargs):
			"""Function-wrapper that saves information about original function"""
			return func_2(*args, **kwargs)
		wrapper.__name__ = func_1.__name__
		wrapper.__doc__ = func_1.__doc__
		wrapper.__original_func = func_1
		return wrapper
	return save_original

def print_result(func):
	@save_original_info(func)
	def wrapper(*args, **kwargs):
		"""Function-wrapper which print result of an original function"""
		result = func(*args, **kwargs)
		print (result)
		return result
	return wrapper
   
@print_result   
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
  
if __name__ == '__main__':
	custom_sum([1, 2, 3], [4, 5])
	custom_sum(1, 2, 3, 4)
	
	print(custom_sum.__doc__)
	print(custom_sum.__name__)
	print(custom_sum.__original_func)
