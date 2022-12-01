import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Air_Traffic.csv", delimiter=",")
dfANA = df[df["Operating Airline"] == "All Nippon Airways"]
dfAC = df[df["Operating Airline"] == "Air Canada"]
dfWA = df[df["Operating Airline"] == "WestJet Airlines"]

dataANA = pd.to_datetime(dfANA["Activity Period"], format="%Y%m")
countANA = df.groupby(dataANA.dt.year)["Passenger Count"].sum()

dataAC = pd.to_datetime(dfAC["Activity Period"], format="%Y%m")
countAC = df.groupby(dataAC.dt.year)["Passenger Count"].sum()

dataWA = pd.to_datetime(dfWA["Activity Period"], format="%Y%m")
countWA = df.groupby(dataWA.dt.year)["Passenger Count"].sum()


fig, ax = plt.subplots()
plt.plot(dict(countANA).keys(), dict(countANA).values(), "k")
plt.plot(dict(countAC).keys(), dict(countAC).values(), "r")
plt.plot(dict(countWA).keys(), dict(countWA).values(), "b")
plt.show()
