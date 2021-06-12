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
        ax1.set_xlabel("Week")
        ax1.set_ylabel("Mensa Visitors", color="gray")
        l1 = ax1.bar(height=anzahl, x=woche, width=0.8, bottom=None, align='center', color="gray")

        ax2 = ax1.twinx()
        ax2.set_ylabel("COVID-19", color="red")
        l2, = ax2.plot(woche, covid, color="red")
        
        plt.legend([l1, l2], ["Mensa Visitors", "COVID-19"])

        fig.tight_layout()
        plt.savefig(f"{output}/mensa{index}.png", dpi=200)

def covid_temperature(mensa_list, output):
    temp = mensa_list[0]["Temp_DHT"].values
    covid = mensa_list[0]["COVID"].values
    woche = mensa_list[0]["Woche"].values
    
    fig, ax1 = plt.subplots(figsize=(20, 5))
    plt.xticks(rotation=45)
    ax1.set_title(f"Temp and Covid")
    ax1.set_xlabel("Week")
    ax1.set_ylabel("Temp", color="blue")
    l1, = ax1.plot(woche, temp, color="blue")

    ax2 = ax1.twinx()
    ax2.set_ylabel("COVID-19", color="red")
    l2, = ax2.plot(woche, covid, color="red")
    
    plt.legend([l1, l2], ["Temperature", "COVID-19"])

    fig.tight_layout()
    plt.savefig(f"{output}/Temp_covid.png", dpi=200)

def covid_temperature_mensa(mensa_list, output):
    temp = mensa_list[0]["Temp_DHT"].values
    covid = mensa_list[0]["COVID"].values
    woche = mensa_list[0]["Woche"].values
    
    # Calculate the sum of all visitors in every week
    total_mensa = [0 for x in range(len(temp))]
    for mensa in mensa_list:
        for index, count in enumerate(mensa["Anzahl"]):
            total_mensa[index] += count
    
    fig, ax1 = plt.subplots(figsize=(20, 5))
    plt.xticks(rotation=45)
    ax1.set_xlabel("Week")
    ax1.set_ylabel("Mensa Visitors", color="gray")
    l1 = ax1.bar(height=total_mensa, x=woche, width=0.8, bottom=None, align='center', color="gray")

    ax3 = ax1.twinx()
    ax3.set_title(f"Temperature, Covid and Mensa Visitors")
    ax3.set_xlabel("Week")
    ax3.set_ylabel("Temp", color="blue")
    l3, = ax3.plot(woche, temp, color="blue")

    ax2 = ax1.twinx()
    ax2.set_ylabel("COVID-19", color="red")
    l2, = ax2.plot(woche, covid, color="red")

    plt.legend([l1, l2, l3], ["Mensa Visitors", "COVID-19", "Temperature"])

    fig.tight_layout()
    plt.savefig(f"{output}/Temp_covid_mensa.png", dpi=200)   


def covid_humidity_mensa(mensa_list, output):
    temp = mensa_list[0]["hum_DHT"].values
    covid = mensa_list[0]["COVID"].values
    woche = mensa_list[0]["Woche"].values
    
    # Calculate the sum of all visitors in every week
    total_mensa = [0 for x in range(len(temp))]
    for mensa in mensa_list:
        for index, count in enumerate(mensa["Anzahl"]):
            total_mensa[index] += count
    
    fig, ax1 = plt.subplots(figsize=(20, 5))
    plt.xticks(rotation=45)
    ax1.set_xlabel("Week")
    ax1.set_ylabel("Mensa Visitors", color="gray")
    l1 = ax1.bar(height=total_mensa, x=woche, width=0.8, bottom=None, align='center', color="gray", label="Mensa Visitors")

    ax3 = ax1.twinx()
    ax3.set_title(f"Humidity, Covid and Mensa Visitors")
    ax3.set_xlabel("Week")
    ax3.set_ylabel("Humidity", color="blue")
    l3, = ax3.plot(woche, temp, color="blue", label="Humidity")

    ax2 = ax1.twinx()
    ax2.set_ylabel("COVID-19", color="red")
    l2, = ax2.plot(woche, covid, color="red", label="COVID-19")
    
    plt.legend([l1, l2, l3], ["Mensa Visitors", "COVID-19", "Humidity"])

    fig.tight_layout()
    plt.savefig(f"{output}/Hum_covid_mensa.png", dpi=200)   

def main():
    total_values = preprocessing()
    
    mensa_isolated(total_values, "./images/")
    covid_temperature(total_values, "./images")
    covid_temperature_mensa(total_values, "./images")
    covid_humidity_mensa(total_values, "./images")
    

if __name__ == "__main__":
    main()
