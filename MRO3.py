class A :
    def do_this(self):
        print("A")
        
class B(A):
    pass

class C(A):
    def do_this(self):
        print('C')
        
class D(B,C):
    pass

obj=D()
obj.do_this()