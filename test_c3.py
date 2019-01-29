class A:
    def __init__(self):
        print('Running A.__init__')
        # super().__init__()

class B(A):
    def __init__(self):
        print('Running B.__init__')    
        # A.__init__(self)    
        super().__init__()

class C(A):
    def __init__(self):
        print('Running C.__init__')
        # A.__init__(self)
        super().__init__()


class T:
    def __init__(self):
        print('Running T.__init__')


class X(A):
    def __init__(self):
        print('Running X.__init__') 
        super().__init__()


class Y(X):
    def __init__(self):
        print('Running Y.__init__')
        super().__init__()


class Z(X):
    def __init__(self):
        print('Running Z.__init__')
        super().__init__()




class D(B,C,Y,Z):
    def __init__(self):
        print('Running D.__init__')
        super().__init__()
        # T.__init__(self)
        # B.__init__(self)
        # C.__init__(self)

foo = D()