class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        h=self.__hour+other.__hour
        m=self.__minute+other.__minute
        s=self.__second+other.__second
        return str(h)+str(m)+str(s)
t1=Time(11,34,10)
t2=Time(20,34,50)
t3=t1+t2
print(t3)
