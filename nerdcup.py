import requests
import pandas as pd
from mensa import preprocessing
import matplotlib.pyplot as plt
from utils import *

def mensa_isolated(mensa_list, output):
    for index, mensa in enumerate(mensa_list):
        # mensa.to_csv("test.csv")

        # total_values[0]["Woche"].plt
        anzahl = mensa["Anzahl"].values
        covid = mensa["COVID"].values
        woche = mensa["Woche"].values

        fig, ax1 = plt.subplots(figsize=(20, 5))
        plt.xticks(rotation=45)
        ax1.set_title(f"{mensa_names[index]}")
        ax1.set_xlabel("Woche")
        ax1.set_ylabel("Einkäufe", color="blue")
        ax1.bar(height=anzahl, x=woche, width=0.8, bottom=None, align='center', color="blue")

        ax2 = ax1.twinx()
        ax2.set_ylabel("COVID-19", color="red")
        ax2.plot(woche, covid, color="red")
        
        fig.tight_layout()
        plt.savefig(f"{output}/mensa{index}.png", dpi=200)

def covid_temperature(mensa_list, output):
    temp = mensa_list[0]["Temp_DHT"].values
    covid = mensa_list[0]["COVID"].values
    woche = mensa_list[0]["Woche"].values
    
    fig, ax1 = plt.subplots(figsize=(20, 5))
    plt.xticks(rotation=45)
    ax1.set_title(f"Temp and Covid")
    ax1.set_xlabel("Woche")
    ax1.set_ylabel("Temp", color="blue")
    ax1.plot(woche, temp, color="blue")

    ax2 = ax1.twinx()
    ax2.set_ylabel("COVID-19", color="red")
    ax2.plot(woche, covid, color="red")
        
    fig.tight_layout()
    plt.savefig(f"{output}/Temp_covid.png", dpi=200)
                      

def main():
    total_values = preprocessing()
    
    # mensa_isolated(total_values, "./images/")
    covid_temperature(total_values, "./images")
    

if __name__ == "__main__":
    main()
