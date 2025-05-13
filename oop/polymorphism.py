
class A:
    def a(self):
        print('A is a method')

class B(A):
    def b(self):
        print('B is b method')

class C:
    def c(self):
        print('C is c method')

class D(B,C):
    def d(self):
        print('D is d method')

obj1=D()
obj1.a()
obj1.b()
obj1.c()
obj1.d()

