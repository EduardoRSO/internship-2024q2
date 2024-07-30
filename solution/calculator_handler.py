import numpy as np
import pandas as pd
from datetime import date
from sgs_handler import SGSHandler

class CalculatorHandler():
    def __init__(self, capital:float = 657.43, window:int = 20) -> None:
        self.available_handlers = {
            'SELIC': SGSHandler
        }
        self.parameters_setter_map = {}
        self.dataframe = None
        self.window = window
        self.capital = capital

    def set_capital(self, value:float):
        self.capital = value

    def set_range(self, value:int):
        self.window = value

    def set_parameters_setter_map(self):
        self.parameters_setter_map = {
            'serie_name' : self.interest_rate_handler.set_sgs_code,
            'start_date' : self.interest_rate_handler.set_start_date,
            'end_date' : self.interest_rate_handler.set_end_date,
            'freq' : self.interest_rate_handler.set_freq,
            'last_n': self.interest_rate_handler.set_last_n
        }

    def set_interest_rate_handler(self, parameters: dict):
        self.serie_name = parameters['serie_name']
        self.interest_rate_handler = self.available_handlers[self.serie_name](self.serie_name)
        self.set_parameters_setter_map()
        for parameter_name, parameter_value in parameters.items():
            self.parameters_setter_map[parameter_name](parameter_value)

    def set_dataframe(self):
        self.interest_rate_handler.try_set_dataframe()
        self.dataframe = self.interest_rate_handler.get_dataframe().copy()

    def _aux_calculate(self, window) :
        _df = pd.Series(window, index=self.dataframe.index[-len(window):])
        result = self.capital * _df.shift().add(1).cumprod().fillna(1).iloc[-1]
        return result

    def calculate(self):
        print(self.dataframe)
        self.dataframe['return'] = self.dataframe['valor'].rolling(window=self.window).apply(self._aux_calculate, raw=True)
        self.dataframe['compound'] = self.capital
        self.dataframe['compound'] = (self.dataframe['compound']) * self.dataframe["valor"].shift().add(1).cumprod().fillna(1)
        self.dataframe["Amount earned"] = self.dataframe["compound"] - self.capital