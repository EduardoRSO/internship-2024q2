import json
import pandas as pd
from datetime import datetime, date
from solution.calculator_handler import CalculatorHandler

def display_message(df: pd.DataFrame, range_of: int = 500):
    df = df.reset_index()
    max_amount_id = df['acc_var'].idxmax()
    row_end = df.iloc[max_amount_id]
    row_start = df.iloc[max_amount_id-500]
 
    print(
        f"\nThe best day to invest is {row_start['Date']}, with an amount earned of {row_end['Amount earned']} after {range_of} days "
        f"({row_start['Date']} to {row_end['Date']})"
    )

def save_dataframe(df:pd.DataFrame, file_name):
    df.to_csv(file_name)

if __name__ == '__main__':
    environment_variables = json.load(open('config.json','r'))
    c = CalculatorHandler(environment_variables)
    c.calculate()
    display_message(c.dataframe)
    save_dataframe(c.dataframe,'solution.csv')
    save_dataframe(c.dataframe,'df_raw.csv')


