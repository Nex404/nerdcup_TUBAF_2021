from os import sep
import pandas as pd
import numpy as np
from utils import *
import matplotlib.pyplot as plt

def preprocessing():
    # Mensa dataframe
    all_mensa_data = list()
    for mensa in mensa_data:
        data = pd.read_csv(mensa["filename"], dtype={"Woche": object}, sep=",", header=0)
        data["Woche"] = data["Woche"].astype(str)
        all_mensa_data.append(data)
    
    all_mensa = pd.concat(all_mensa_data, ignore_index=True)
    
    # Covid dataframe
    covid_csv = "./data/covid19/Mittelsachsen.csv"
    covid_data = pd.read_csv(covid_csv, dtype={"Woche": object}, sep=",", header=0)
    covid_data["Woche"] = covid_data["Woche"].astype(str)
    
    # weather dataframe
    weather_csv = "./data/Wetter/wetter_mod6.csv"
    weather_data = pd.read_csv(weather_csv, dtype={"Woche": object}, sep=",", header=0)
    weather_data["Woche"] = weather_data["Woche"].astype(str)

    # Join the mensa info with the covid information
    merged_df = pd.merge(all_mensa, covid_data, on="Woche")
    # grouped_df = merged_df.groupby(by=["Woche"])

    total_values = list()
    for name in mensa_names:
        x = merged_df[(merged_df["Name"] == name)]
        x_total = x.groupby(by=["Woche", "Name"])["Anzahl"].sum()
        x_total = x_total.reset_index()
        total_values.append(x_total)

    # Fill the holes with 0
    for week in covid_data["Woche"]:
        for index, mensa in enumerate(total_values):
            is_empty = mensa[mensa["Woche"] == week].empty
            if is_empty == True:
                new_row = {
                    "Woche": week,
                    "Name": mensa_names[index],
                    "Anzahl": 0
                }
                total_values[index] = mensa.append(new_row, ignore_index=True)
    
    # Create new columns (week/year)
    for index, mensa in enumerate(total_values):
        mensa.insert(0, "week", 0)
        mensa.insert(1, "year", 0)

    for index, mensa in enumerate(total_values):
        for row in mensa.iterrows():
            unformatted_date = row[1]["Woche"]
            year = int(unformatted_date.split(".")[0])
            week = int(unformatted_date.split(".")[1])
            total_values[index].at[row[0], "year"] = year
            total_values[index].at[row[0], "week"] = week


    return total_values

def main():
    total_values = preprocessing()

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
