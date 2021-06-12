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
        data["Woche"] = data["Woche"].astype(str)
        all_mensa_data.append(data)
    
    all_mensa = pd.concat(all_mensa_data, ignore_index=True)
    
    # Covid dataframe
    covid_csv = "./data/covid19/Mittelsachsen.csv"
    covid_data = pd.read_csv(covid_csv, sep=",", header=0)
    covid_data["Woche"] = data["Woche"].astype(str)
    
    # weather dataframe
    weather_csv = "./data/Wetter/wetter_mod6.csv"
    weather_data = pd.read_csv(weather_csv, sep=",", header=0)
    weather_data["Woche"] = weather_data["Woche"].astype(str)

    # Join the mensa info with the covid information
    merged_df = pd.merge(all_mensa, covid_data, on="Woche")
    
    # merged_df = pd.merge(merged_df, weather_data, on="Woche")
    # grouped_df = merged_df.groupby(by=["Woche"])

    total_values = list()
    for name in mensa_names:
        x = merged_df[(merged_df["Name"] == name)]
        x_total = x.groupby(by=["Woche", "Name"])["Anzahl"].sum()
        x_total = x_total.reset_index()
        print(x_total)
        total_values.append(x_total)

    colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']

    x_values = [temp_df["Woche"] for temp_df in total_values]
    y_values = [temp_df["Anzahl"] for temp_df in total_values]
    
    fig, ax = plt.subplots()

    for index, value in enumerate(mensa_names):
        ax.bar(x=x_values[index], height=y_values[index], color=colors[index], width=0.3, align="edge", label=value)

    # ax.set_xticklabels(mensa_names, fontdict=None, minor=False)
    # ax.xticks(rotation=45)    

    ax.legend()
    ax.set_ylabel('Scores')
    fig.tight_layout()

    plt.savefig("test.png")

if __name__ == "__main__":
    main()
