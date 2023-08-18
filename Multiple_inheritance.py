class Abdullah:
    def A_Abdullah(self):
        print('The is Abdullah')

class Sude:
    def S_Abdullah(self):
        print('This is Suad Abdullah ')
        
class AbdullahS(Abdullah , Sude): #مثال 1 يمكن للكلاس الورارثه من اكثر من كلاس بذا الطريقه 
    def A_Saud(self):
        print('This is Abdullah Saud')

AbdullahS1= AbdullahS()
AbdullahS1.A_Saud()
AbdullahS1.A_Abdullah()
AbdullahS1.S_Abdullah()