# class A:
#     def a(self):
#         print("a is a method")
# class B:
#     def b(self):
#         print("b is a method")
# class C(A,B):
#     def c(self):
#         print("c is a method")
# obj=C()
# obj.a()
# obj.b()
# obj.c()

class school():
    def hour(self):
        print("8hours")
    def subjects(self):
        print("differnt subjects")
    def teachers(self):
        print("differnt teachers")
class tution():
    def hours(self):
        print("only 2 hours")
    def teacher(self):
        print("only one teacher")
class student(school,tution):
    def study(self):
        print("studying in school and tution")
    def exam(self):
        print("examattending school and tution")
kavya=student()
kavya.teacher()
kavya.hour()
kavya.subjects()
kavya.exam()
kavya.study()