
def decorator(func):
	print('We are in the decorator func')
	def wrapper(*args, **kwargs):
		print('We are in the wrapper func')
		a = func(*args, **kwargs)
		return a
	return wrapper

@decorator
def do_somthing(num):
	return num * 2


print(do_somthing(10))