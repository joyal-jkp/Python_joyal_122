class Rectangle:
    def __init__(self,lenth,bread):
        self.lenth=lenth
        self.bread=bread
    def area(self):
        self.result=self.lenth*self.bread
        print("Area:",self.result)
    def peri(self):
        self.result=2*(self.lenth+self.bread)
        print("Perimeter:",self.result)
    def compare(self):
        print("Area of Rectangle1")
        
obj2=Rectangle(int(input("enter length")),int(input("enter breadth")))
obj1=Rectangle(int(input("enter length")),int(input("enter breadth")))
obj2.area()
obj1.peri()
