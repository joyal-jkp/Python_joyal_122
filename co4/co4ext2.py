class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,d):
        return self.salary*d.day
class Time:
    def __init__(self,name,day):
        self.name=name
        self.day=day

emp=Employee("Korra",225)
time=Time("Korra",20)
sal=emp*time
print("Salary",sal)
