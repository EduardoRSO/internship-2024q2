import json
import pandas as pd
from datetime import datetime, date, timedelta
from solution.calculator_handler import CalculatorHandler

def display_message(df: pd.DataFrame, range_of: int = 500):
    df = df.reset_index()
    max_amount_id = df['acc_var'].idxmax()
    row_end = df.iloc[max_amount_id]
    row_start = df[df.Date >= row_end.Date-timedelta(range_of)].head(1)
    
    print(
        f"\nThe best day to invest is {row_start['Date'].iloc[0]}, with an amount earned of {row_end['acc_var']} after {range_of} days "
        f"({row_start['Date'].iloc[0]} to {row_end['Date']})"
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


