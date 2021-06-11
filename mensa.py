from os import sep
import pandas as pd
from utils import *

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

    # Join the mensa info with the covid information
    new_df = pd.merge(all_mensa, covid_data, on="Woche")
    print(new_df)

if __name__ == "__main__":
    main()
