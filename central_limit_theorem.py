import pandas as pd 
import csv

df = pd.read_csv("/Users/mnicasio/Desktop/Data/CentralLimitTheorem/z_table_clt.csv")

def probVal (mean, value, std, n):
    """[This function calculates the probability that a value will be either greater than or less than the mean]
    
    Arguments:
        mean {[int]} -- [the mean of the distribution]
        value {[int]} -- [the value of interest]
        std {[int]} -- [the standard deviation of the distribution]
        n {[int]} -- [the sample size]
    """
    z_value = (value-mean) / (std/(n**0.5))
    z = str(z_value)
    prob = round(float(df.loc[:, z] * 100), 2)
    print('The probability is ' +str(prob)+ " %")

probVal(110, 120, 20, 25)