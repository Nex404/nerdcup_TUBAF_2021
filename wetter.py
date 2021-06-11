# import requests
import pandas as pd

filepath = "data/Wetter/Wetterdaten_HumboldtBau.csv"

data = pd.read_csv(filepath, delimiter=",", header=0)

data = data.drop(columns=["latitude", "longitude", "elevation", "Light", "TEMP_680", "Hum_680"])
print(data.iloc[0])

print(data.describe())