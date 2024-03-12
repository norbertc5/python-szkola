
class trojkat:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    def obw(self):
        return self.a+self.b+self.c
    
    def pole(self):
        p = (self.a + self.b + self.c) / 2
        pole = p * (p-self.a) * (p-self.b) * (p-self.c)
        pole = pole ** (1/2)
        return pole
    
    def czyPoprawny(self):
        return (self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a)
    



class t_rownoboczny(trojkat):
    def czyPoprawny(self):
        return (self.a == self.b and self.a == self.c and self.c == self.b)



class t_rownoramiennny(trojkat):
    def czyPoprawny(self):
        if(super().czyPoprawny() and (self.a == self.b or self.a == self.c or self.c == self.b)):
            return "Poprawny trojkat rownoramienny"
        else:
            return "Niepoprawny trojkat rownoramienny"



class t_prostokatny(trojkat):
    pass



t1 = trojkat(3, 4, 5)
t2 = t_rownoramiennny(6, 5, 6)
t3 = t_rownoboczny(6, 6, 6)
#print(t1)
#print(t1.czyPoprawny())
#print(t1.obw())
#print(t1.pole())

#print(t2.czyPoprawny())

print(t3.czyPoprawny())