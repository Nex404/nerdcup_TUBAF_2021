from os import sep
import pandas as pd
import numpy as np
from utils import *
import matplotlib.pyplot as plt

def main():
    # Mensa dataframe
    all_mensa_data = list()
    for mensa in mensa_data:
        data = pd.read_csv(mensa["filename"], sep=",", header=0)
        all_mensa_data.append(data)
    
    all_mensa = pd.concat(all_mensa_data, ignore_index=True)
    
    # Covid dataframe
    covid_csv = "./data/covid19/Mittelsachsen.csv"
    covid_data = pd.read_csv(covid_csv, sep=",", header=0)
    
    # weather dataframe
    weather_csv = "./data/Wetter/wetter_mod6.csv"
    weather_data = pd.read_csv(weather_csv, sep=",", header=0)

    # Join the mensa info with the covid information
    merged_df = pd.merge(all_mensa, covid_data, on="Woche")
    
    # hier noch mal gucken ob alles passt
    merged_df = pd.merge(merged_df, weather_data, on="Woche")
    print(merged_df.head())
    # Group by week
    grouped_df = merged_df.groupby(by=["Woche"])

    x1 = list(merged_df[merged_df["Name"] == "Auflaeufe und Pizzen"]["Anzahl"])
    x2 = list(merged_df[merged_df["Name"] == "mensaVital"]["Anzahl"])
    x3 = list(merged_df[merged_df["Name"] == "Selbstwahltheken Gemuese Pasta Salat"]["Anzahl"])
    x4 = list(merged_df[merged_df["Name"] == "tabula-CT und Wok"]["Anzahl"])
    x5 = list(merged_df[merged_df["Name"] == "Vegetarisch"]["Anzahl"])

    colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']

    plt.hist([x1, x2, x3, x4, x5], color=colors, label=mensa_names, stacked=True)
    plt.legend()
    plt.savefig("test.png")

if __name__ == "__main__":
    main()
