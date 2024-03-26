import pandas as pd

df = pd.read_csv("temperature.csv",sep=";")
#print(df.to_string())

#print("Ilość rekordów w obiekcie DF wynosi: ", len(df))

#print(df.head(100).to_string())

#print(df.tail(100).to_string())

#print(df[["Country","City"]].to_string())

#print(df[df["Country"] == "Poland"].to_string())

#print(df[df["City"] == "Wroclaw"][df["year"] >= 1900][df["year"] <= 1999].to_string())

#print(df[df["City"] == "Warsaw"] ["AverageTemperatureFahr"].mean())

#print(df[df["Country"] == "Poland"] ["AverageTemperatureFahr"].max())
#print(df[df["Country"] == "Poland"] ["AverageTemperatureFahr"].min())

#print(df[["year"]] [df["year"] >= 1900] [df["year"] <= 1999].mean())

def F2C(temp):
    return 5*(temp-32)/9

df.rename(columns={"AverageTemperatureFahr":"AvgTempF"}, inplace=True)
df.rename(columns={"AverageTemperatureUncertaintyFahr":"AvgTempUnF"}, inplace=True)

#print(df)

df["AvgTempC"] = df["AvgTempF"].map(F2C)
df["AvgTempUnC"] = df["AvgTempUnF"].map(F2C)
del df["AvgTempUnF"]


def Latitude(lat):
    if(lat[-1] == 'S'):
        return -float(lat[:-1])
    elif(lat[-1] == 'N'):
        return float(lat[:-1])
    else:
        return 0.0
    
def Longitude(lat):
    if(lat[-1] == 'E'):
        return -float(lat[:-1])
    elif(lat[-1] == 'W'):
        return float(lat[:-1])
    else:
        return 0.0

df["Latitude"] = df["Latitude"].map(Latitude)
df["Longitude"] = df["Longitude"].map(Longitude)

print(df)