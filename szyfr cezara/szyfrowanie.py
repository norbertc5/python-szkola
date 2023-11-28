
"""
Program wczytuje tekst z pliku tekstowego i szyfruje lub odszyfrowuje go w zależności od wyboru użytkownika, wykożystując szyfr cezara

"""



f = open("dane.txt", "r")
text = f.read()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y", "z"]
n = 3

def Modyfikuj(shift):
    tekstZaszyfrowany = ""
    for el in text:
        try:
            tekstZaszyfrowany += str(alphabet[alphabet.index(el) + shift])
        except:
            tekstZaszyfrowany += " "

    print(tekstZaszyfrowany)
    f = open("dane.txt", "w")
    f.write(tekstZaszyfrowany)




choice = input("Zaszyfrować [Z] czy odszyfrować [O]: ")

if choice == "Z":
    Modyfikuj(n)
elif choice == "O":
    Modyfikuj(-n)
else:
    print("Nie rozpozano inputu")
