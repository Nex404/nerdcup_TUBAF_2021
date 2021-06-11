import requests
import pandas as pd




def main():
    r = requests.get('https://api.github.com/events')
    print(r.text)

if __name__ == "__main__":
    main()
