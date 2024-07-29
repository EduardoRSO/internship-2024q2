import logging
import pandas as pd
from bcb import sgs
from datetime import date

class SGSHandler():

    def __init__(self, sgs_code:int = None, start_date: date = None, end_date: date = None, last_n: int = 0, freq: str = None) -> None:
        self.set_logger()
        self.sgs_code_mapping = {
            'SELIC': 11
        }
        self.sgs_code = sgs_code
        self.start_date = start_date
        self.end_date = end_date
        self.last_n = last_n
        self.freq = freq
        self.dataframe = None
        self.logger.info(f" [+] Instantiated SGSHandler : {self.__str__()}")

    def __str__(self)->str:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.__str__ with parameters: None")
        result = (f"SGSHandler(sgs_code={self.sgs_code}, start_date={self.start_date}, end_date={self.end_date}, "
                  f"last_n={self.last_n}, freq={self.freq}, dataframe_shape={self.dataframe.shape if self.dataframe is not None else None}, sgs_code_mapping = {self.sgs_code_mapping})")
        self.logger.info(f"[+] Executed {self.__class__.__name__}.__str__ and returned string representation")
        return result


    def set_sgs_code(self, series_name: str)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_sgs_code with parameters: series_name={series_name}")
        self.series_name = self.sgs_code_mapping[series_name]
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_sgs_code with new value: sgs_code={self.sgs_code}")

    def set_start_date(self, start_date: date)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_start_date with parameters: start_date={start_date}")
        self.start_date = start_date
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_start_date with new value: start_date={self.start_date}")

    def set_end_date(self, end_date: date)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_end_date with parameters: end_date={end_date}")
        self.end_date = end_date
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_end_date with new value: end_date={self.end_date}")

    def set_last_n(self, last_n: int)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_last_n with parameters: last_n={last_n}")
        self.last_n = last_n
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_last_n with new value: last_n={self.last_n}")

    def set_freq(self, freq: str)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_freq with parameters: freq={freq}")
        self.freq = freq
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_freq with new value: freq={self.freq}")

    def set_logger(self)->None:
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def set_dataframe(self) ->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.set_dataframe with parameters: "
                          f"sgs_code={self.sgs_code}, start_date={self.start_date}, end_date={self.end_date}, "
                          f"last_n={self.last_n}, freq={self.freq}")
        self.dataframe = sgs.get(self.sgs_code, self.start_date, self.end_date, self.last_n, self.freq)
        self.logger.info(f"[+] Executed {self.__class__.__name__}.set_dataframe and returned dataframe with shape {self.dataframe.shape}")

    def get_dataframe(self) -> pd.DataFrame:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.get_dataframe with parameters: None")
        df = self.dataframe
        self.logger.info(f"[+] Executed {self.__class__.__name__}.get_dataframe and returned dataframe with shape {df.shape}")
        return df

    def try_set_dataframe(self)->None:
        self.logger.info(f"[+] Executing {self.__class__.__name__}.try_set_dataframe")
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                self.set_dataframe()
                self.logger.info(f" [+] Executed {self.__class__.__name__}.try_set_dataframe successfully on attempt {attempts + 1}")
                return
            except Exception as e:
                attempts += 1
                self.logger.error(f" [-] Error in {self.__class__.__name__}.set_dataframe: {e}. Attempt {attempts} of {max_attempts}")
                if attempts >= max_attempts:
                    self.logger.error(f" [-] Failed to set dataframe after {max_attempts} attempts.")
                    break