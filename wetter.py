# import requests
import pandas as pd

filepath = "data/Wetter/Wetterdaten_HumboldtBau.csv"

data = pd.read_csv(filepath, delimiter=",", header=0)

data = data.drop(columns=["latitude", "longitude", "elevation", "Light", "Temp_680", "hum_680"])
print(data.describe())