import json
import pandas as pd
from datetime import datetime
from solution.calculator_handler import CalculatorHandler

def display_message(df:pd.DataFrame):
    print(df.loc[df['Amount earned'].idxmax()])
    print(df[df.index == datetime(2016,10,28)])

def save_dataframe(df:pd.DataFrame, file_name):
    df.to_csv(file_name)

if __name__ == '__main__':
    environment_variables = json.load(open('config.json','r'))
    c = CalculatorHandler(environment_variables)
    c.calculate()
    display_message(c.dataframe)
    save_dataframe(c.dataframe,'solution.csv')
