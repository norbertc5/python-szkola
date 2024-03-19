import pandas as pd

csv = pd.read_csv("Pracownicy 1.csv", sep=";")
print(csv[csv["Płeć"] == "M"])


