class a:
	s=1
	p=2

	def __init__(self,l,m):
		print('...a\n')
		self.l=l
		self.m=m

	def bb(self):
		print(a.s * self.m)

	def cc(self):
		print(self.s)

	def dd():
		print(a.p)

	def ee():
		print(self.p)



class b:
	def __init__(self):
		print('...b\n')
		# super().__init__()
		self.k=0

	def mmm(self):
		print('hi')


class c(b,a):
	def __init__ (self,x,y,z):
		super().__init__()
		print('...c\n')
