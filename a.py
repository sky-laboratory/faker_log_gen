import pandas as pd

data = pd.read_csv("country_codes.csv")


a = [i for i in data["Code"]]
print(a)
