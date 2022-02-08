class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
        self.__area=length*breadth
    def __lt__(self,m):
        return self.__area<m.__area
r=Rectangle(4,10)
r1=Rectangle(6,16)
if r<r1:
    print("Rectangle two has largest area")
else:
    print("Rectangle one has largest area")
