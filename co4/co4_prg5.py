class Publisher:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(self.name)
class Book(Publisher):
    def __init__(self,name,title,auth):
        Publisher.__init__(self,name)
        self.title=title
        self.auth=auth
    def disp(self):
        print(self.title,self.author)
class Python(Book):
    def __init__(self,name,title,auth,price,nop):
        Book.__init__(self,name,title,auth)
        self.price=price
        self.nop=nop
    def disp(self):
        print(self.name)
        print(self.title)
        print(self.auth)
        print("Rs.",self.price,self.nop)
obj=Python("Oxford University press","Programming in Python","Reema Theraja",479,560)
obj.disp()
