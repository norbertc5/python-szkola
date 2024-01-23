class Ulamek:
    licznik = 1
    mianownik = 1

    def __init__(self, l=1, m=1) -> None:
        self.licznik = l
        self.mianownik = m

    def Ustaw(self, l:int, m:int):
            
            if(m == 0):
                return

            self.licznik = l
            self.mianownik = m

    def __str__(self) -> str:
         return f"{self.licznik}/{self.mianownik}"
    
    def Normalizuj(self):
        dzielnik = Ulamek.NWD(self.licznik, self.mianownik)
        self.licznik //= dzielnik
        self.mianownik //= dzielnik

        if(self.licznik < 0 and self.mianownik < 0):
              abs(self.licznik)
              abs(self.mianownik)

    
    def NWD(a, b):
        if(a==b):
            return a

        while(a!=b):
            if(a > b):
                a = a-b
            elif(a<b):
                b = b-a
        return a

A = Ulamek(-1, -2)
#A.Normalizuj()
#A.Ustaw(-8, 40)
A.Normalizuj()
print(A)