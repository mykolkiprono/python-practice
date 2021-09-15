
def log(f, x,y):
	def logged(x,y):
		rv = f(x,y)
		print(f.name, x,y, "->", rv)

		return rv
	return logged

@log
def add(x, y):
	return x+y 

g = log(add, 5,5)
p




