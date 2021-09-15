from base import Base

class Foo(Base):
	# def __init__(self):
	# 	super().baz()

	def bar(self):
		return 'baz'

f = Foo()
# print(f.baz())
