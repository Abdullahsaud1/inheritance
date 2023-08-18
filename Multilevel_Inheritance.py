class Grandparent:
    def G_d(self):
        print('This is Grandparent Class')

class parent(Grandparent): #وارث من الجد 
    def P_d(slef):
        print('This is parent  Class')

class Child(parent): # وارث من الاب وليس الجد
    def C_d(slef):
        print("This is Child Class ")
Child1 = Child()
Child1.G_d()
Child1.P_d()
Child1.C_d()        