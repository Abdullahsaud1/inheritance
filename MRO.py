class A:
    def do_this(self):
        print("Doing this in class A")
        
class B(A): 
    pass

class C: 
    def do_this(self):
        print('Doing this in class C')
      
        
class D(B,C):
    pass



obj=D()
obj.do_this()
# ارجع للصوره رقم 4 