import logging
import pandas as pd
from datetime import datetime
from solution.sgs_handler import SGSHandler

class CalculatorHandler():
    def __init__(self, environment_variables: dict) -> None:
        self.set_logger()
        self.logger.info(f"[+] Executing {self.__class__.__name__}.__init__ with parameters: environment_variables={environment_variables}")
        self.set_parameters_setter_map()
        self.set_attributes(environment_variables['calculator_handler'])
        self.set_interest_rate_handlers_map()
        self.set_interest_rate_handler(environment_variables['interest_rate_handler'])
        self.dataframe = None
        self.logger.info(f"[+] Executed {self.__class__.__name__}.__init__")

    def set_logger(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def set_capital(self, value: str):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_capital with parameters: value={value}")
        self.capital = float(value)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_capital")

    def set_window(self, value: str):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_window with parameters: value={value}")
        self.window = int(value)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_window")

    def set_parameters_setter_map(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_parameters_setter_map")
        self.parameters_setter_map = {
            'window': self.set_window,
            'capital': self.set_capital,
        }
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_parameters_setter_map: self.parameters_setter_map={self.parameters_setter_map}")

    def set_attributes(self, environment_variables: dict):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_attributes with parameters: environment_variables={environment_variables}")
        for attribute_name, attribute_value in environment_variables.items():
            if self.parameters_setter_map.get(attribute_name) is not None:
                self.logger.info(f"[+] Setting attribute {attribute_name} with value {attribute_value}")
                self.parameters_setter_map[attribute_name](attribute_value)
            else:
                self.logger.error(f"[-] Error at {self.__class__.__name__}.set_attributes: Invalid attribute name: {attribute_name}, value: {attribute_value}")
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_attributes")

    def set_interest_rate_handlers_map(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_interest_rate_handlers_map")
        self.interest_rate_handlers_map = {
            'SELIC': SGSHandler
        }
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_interest_rate_handlers_map: self.interest_rate_handlers_map={self.interest_rate_handlers_map}")

    def set_interest_rate_handler(self, environment_variables: dict):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_interest_rate_handler with parameters: environment_variables={environment_variables}")
        self.interest_rate_handler = self.interest_rate_handlers_map[environment_variables['serie_name']](environment_variables)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_interest_rate_handler")

    def set_dataframe(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_dataframe")
        self.interest_rate_handler.try_set_dataframe()
        self.dataframe = self.interest_rate_handler.get_dataframe().copy()
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_dataframe DataFrame shape: {self.dataframe.shape}")

    def _aux_calculate(self, window):
        self.logger.info(f"[+] Executing {self.__class__.__name__}._aux_calculate with parameters: window len={len(window)}")
        _df = pd.Series(window, index=self.dataframe.index[-len(window):])
        result = self.capital * _df.shift().add(1).cumprod().fillna(1).iloc[-1]
        self.logger.info(f"[+] Executed {self.__class__.__name__}._aux_calculate Result: {result}")
        return result

    def calculate_window_accumulated_variation(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.calculate_window_accumulated_variation")
        self.dataframe['return'] = self.dataframe['valor'].rolling(window=self.window).apply(lambda x: self._aux_calculate(x), raw=True)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.calculate_window_accumulated_variation DataFrame shape: {self.dataframe.shape}")
        
    def calculate_compound(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.calculate_compound")
        self.dataframe['compound'] = self.capital
        self.dataframe['compound'] = (self.dataframe['compound']) * self.dataframe["valor"].shift().add(1).cumprod().fillna(1)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.calculate_compound DataFrame shape: {self.dataframe.shape}")
        
    def calculate_amount_earned(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.calculate_amount_earned")
        self.dataframe["Amount earned"] = self.dataframe["compound"] - self.capital
        self.logger.info(f"[+] Executed {self.__class__.__name__}.calculate_amount_earned DataFrame shape: {self.dataframe.shape}")

    def display_message(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.display_message")
        self.logger.info(f"Row with max value of 'return': \n{self.dataframe.loc[self.dataframe['Amount earned'].idxmax()]}")
        self.logger.info(f"Row with max value of 'return': \n{self.dataframe[self.dataframe.index == datetime(2016,10,28)]}")
        self.logger.info(f"[+] Executed {self.__class__.__name__}.display_message")


    def calculate(self):
        self.logger.info(f"[+] Executing {self.__class__.__name__}.calculate")
        self.set_dataframe()
        self.calculate_window_accumulated_variation()
        self.calculate_compound()
        self.calculate_amount_earned()
        self.display_message()
        self.logger.info(f"[+] Executed {self.__class__.__name__}.calculate DataFrame shape: {self.dataframe.shape}")