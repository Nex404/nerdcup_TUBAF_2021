import requests
import pandas as pd
from mensa import preprocessing
import matplotlib.pyplot as plt

def main():
    # r = requests.get('https://api.github.com/events')
    # print(r.text)
    total_values = preprocessing()
    
    print(total_values)
    total_values[0].to_csv("test.csv")
    # total_values[0]["Woche"].plt
    anzahl = total_values[0][total_values[0]["year"] == 2020]["Anzahl"].values
    woche = total_values[0][total_values[0]["year"] == 2020]["Woche"].values
    plt.bar(height=anzahl, x=woche)
    plt.xticks(rotation=45)
    plt.savefig("Mensa0.png")
    
    print(anzahl)
    print(woche)

if __name__ == "__main__":
    main()
