import pandas as pd 
import csv

z_table = pd.read_csv("z_table.csv")

print(z_table.head(5))

def probValueLess (mean, value, std, n):
    z_value = (value-mean) / (std/(n**0.5))
    return z_value 

print(probValueLess(110, 120, 20, 25))
