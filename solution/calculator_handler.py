import numpy as np
import pandas as pd
from datetime import date
from solution.sgs_handler import SGSHandler

class CalculatorHandler():
    def __init__(self, environment_variables:dict) -> None:
        self.set_parameters_setter_map()
        self.set_attributes(environment_variables['calculator_handler'])
        self.set_interest_rate_handlers_map()
        self.set_interest_rate_handler(environment_variables['interest_rate_handler'])
        self.dataframe = None

    def set_capital(self, value:float):
        self.capital = value

    def set_window(self, value:int):
        self.window = value

    def set_parameters_setter_map(self):
        self.parameters_setter_map = {
            'window' : self.set_window,
            'capital' : self.set_capital,
        }

    def set_attributes(self, enviroment_variables:dict):
        for attribute_name, attribute_value in enviroment_variables.items():
            if self.parameters_setter_map.get(attribute_name) != None:
                self.parameters_setter_map[attribute_name](attribute_value)
            else:
                '''logger message [-] Error at <class name>.<function name>: Invalid attribute name: {attribute_name} '''

    def set_interest_rate_handlers_map(self):
        self.available_handlers = {
            'SELIC': SGSHandler
        }

    def set_interest_rate_handler(self, enviroment_variables:dict):
        self.interest_rate_handler = self.available_handlers[enviroment_variables['serie_name']](enviroment_variables)

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