class Vehicle: #____________________________super class________________________________
    def __init__(self , company , owner , color , current_speed):
        self.company = company
        self.owner = owner
        self.color = color
        self.current_speed = current_speed
        
        
    def move(self):
        print("The acr has moved")
    def stop(self):
        print("The cae has stopped")
#______________________________________________child________________________       
class car(Vehicle): #نستخدم الوراثه ميثال 1 
    def m(self):
        print("This is the car class")
car1 =car("jeep", 'nada' , 'black ', 80 )
print(car1.company) # طلب النتيجه
print(car1.current_speed)
print(car1.owner)
print(car1.color)
car1.move() # نوصل للمثد
#__________________________________________________child______________________
class truck(Vehicle):
    def T(self):
        print('This is the truck class')
t=truck('BMW', 'Abdullah' , 'rad' , 95)
print(t.color)
print(t.company)
print(t.current_speed)
print(t.owner)
t.stop()