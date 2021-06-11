import pandas as pd

def read_covid19_data(filepath):
    data = pd.read_csv(filepath, sep=",", header=0)
    print(data)
    return data

def main():
    covid19_mittelsachsen = "./data/covid19/Mittelsachsen.csv"
    covid19_data = read_covid19_data(covid19_mittelsachsen)

if __name__ == "__main__":
    main()