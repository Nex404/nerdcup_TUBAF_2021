from os import sep
import pandas as pd
from utils import *

def main():
    # Mensa dataframe
    all_mensa_data = list()
    for mensa in mensa_data:
        data = pd.read_csv(mensa["filename"], sep=",", header=0)
        print(data)
        all_mensa_data.append(data)
    
    # Covid dataframe
    covid_csv = "./data/covid19/Mittelsachsen.csv"
    covid_data = pd.read_csv(covid_csv, sep=",", header=0)
    print(covid_data)

if __name__ == "__main__":
    main()
