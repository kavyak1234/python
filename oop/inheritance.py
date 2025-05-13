#1.single inheritance
#2.multiple inheritance
#3multievel inheritance
#4hyrarchieal inheritance
#5hybrid inheritance
#1.single inheritance
class A:
    def a (self):
        print('A class a method')
class B(A):
    def b (self):
        print('B class b method')

obj=B()
obj.a()