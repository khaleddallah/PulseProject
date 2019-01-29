class a:
	def __init__(self):
		self.aa=0


class n:
	def __init__(self):
		self.nn=0

class b(a,n):
	def __init__(self):
		super(b,self).__init__()
		self.bb=0