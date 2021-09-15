class BaseMeta(type):
	def __new__(cls, name, bases, body):
		if 'bar' not in body:
			# raise TypeError()
			print("bar should be implemented")
		return super().__new__(cls, name, bases, body)


class Base(metaclass = BaseMeta):
	def baz(self):
		# we want to make sure the user.py implements the bar metho
		return self.bar
