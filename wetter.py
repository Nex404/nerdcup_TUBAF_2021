# import requests
import pandas as pd

filepath = "data/Wetter/wetter_mod5.csv"

data = pd.read_csv(filepath, delimiter=",", header=0)



###########################################
# edit original data 
###########################################

# data = data.drop(columns=["latitude", "longitude", "elevation", "Light", "TEMP_680", "Hum_680", "entry_id"])
# print(type(data.iloc[0]["created_at"]))


# replace cet in timestamp
# data["created_at"] = data["created_at"].str.replace('CET|CEST', '')

# data.to_csv("wetter_mod.csv")


##########################################
# filter Saturdays and Sundays out
##########################################

# weg = []
# temp_data = pd.read_csv(filepath, delimiter=",", header=0)
# for index, value in enumerate(temp_data.iterrows()):
#     temp_day = get_day(data, index)
#     # print(temp_day)
#     # temp_week = get_week(data, index)
#     if temp_day in ["Saturday", "Sunday"]:
#         weg.append(index)
#         # print(index)
        

# temp_data = temp_data.drop(index=weg)

# temp_data.to_csv("wetter_mod2.csv")


#########################################
# filter data only between 1130 and 1330
#########################################


# data["created_at"] = pd.to_datetime(data["created_at"])
# data = data.set_index("created_at")
# data = data.between_time("11:30", "13:30")
# data.to_csv("wetter_mod3.csv")
# print(data.head())



#########################################
# group by date and average all grouped columns
#########################################

# data["created_at"] = pd.to_datetime(data.created_at)
# data = data.assign(date=data.created_at.dt.date)

# # data["date"] = data.created_at.dt.date
# data = data.groupby("date").mean()
# data.to_csv("wetter_mod4.csv")


########################################
# Group by year and week
########################################

# data["date"] = pd.to_datetime(data["date"])


# data = data.groupby([data.date.dt.year, data.date.dt.week]).mean()
# data = data.drop(columns=["Unnamed: 0", "Unnamed: 0.1"])
# data.to_csv("data/Wetter/wetter_mod5.csv")
# print(data)
# print(data.dtypes)



##########################################
# help functions
##########################################

def get_week(df, index):
    # get week of a timestamp
    week = pd.Timestamp(data.iloc[index]["created_at"])
    # print(week.week)
    return week.week


def get_day(df, index):
    # get day of timestemp
    dayname = pd.Timestamp(df.iloc[index]["created_at"])
    # print(friday.day_name())
    return dayname.day_name()  




# Testing
# for index, value in enumerate(data.iterrows()):
#     temp_day = get_day(data, index)
    # print(temp_day)
# week = get_week(data, 50000)
# print(week)
# print(type(week))
# print(get_week(data, 55))
# print(get_day(data, 50000))
# print(type(get_day(data, 50000)))
# print(data.head())

