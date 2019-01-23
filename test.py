
def kh(s):
	def d(a,b):
		print("kh(s)")
		s(a,b)
	return d

@kh
def c(a,b):
	print(a*b)

#c=kh(c)


c(3,5)