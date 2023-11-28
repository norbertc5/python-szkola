f = open("zbiorLiczb.txt", "r")
text = f.readlines()
numbers = list(text)

for el in text:
    print(el)
    numbers[text.index(el)] = int(el)

print(numbers)

sum = 0

for el in numbers:
    sum += int(el)

avg = sum / len(numbers)

print("Suma wynosi: " + str(sum))
print("Średnia wynosi: " + str(avg))
print("Dominująca wartość to: " + str(max(set(numbers), key = numbers.count)))