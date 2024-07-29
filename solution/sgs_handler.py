import logging
from bcb import sgs
from datetime import date

class SGSHandler():

    def __init__(self, sgs_code, start_date: date = None, end_date: date = None, last_n: int = 0, freq: str = None) -> None:
        self.sgs_code = sgs_code
        self.start_date = start_date
        self.end_date = end_date
        self.last_n = last_n
        self.freq = freq
        self.dataframe = None
        self.logger = None
        self.set_logger()

    def set_logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def set_dataframe(self):
        self.logger.debug(f"[+] Executing {self.__class__.__name__}.set_dataframe with parameters: "
                          f"sgs_code={self.sgs_code}, start_date={self.start_date}, end_date={self.end_date}, "
                          f"last_n={self.last_n}, freq={self.freq}")
        self.dataframe = sgs.get(self.sgs_code, self.start_date, self.end_date, self.last_n, self.freq)
        self.logger.debug(f"[+] Executed {self.__class__.__name__}.set_dataframe and returned dataframe with shape {self.dataframe.shape}")

    def get_dataframe(self):
        self.logger.debug(f"[+] Executing {self.__class__.__name__}.get_dataframe with parameters: None")
        df = self.dataframe
        self.logger.debug(f"[+] Executed {self.__class__.__name__}.get_dataframe and returned dataframe with shape {df.shape}")
        return df

    def try_set_dataframe(self):
        self.logger.debug(f"[+] Executing {self.__class__.__name__}.try_set_dataframe")
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                self.set_dataframe()
                self.logger.debug(f" [+] Executed {self.__class__.__name__}.try_set_dataframe successfully on attempt {attempts + 1}")
                return
            except Exception as e:
                attempts += 1
                self.logger.error(f" [-] Error in {self.__class__.__name__}.set_dataframe: {e}. Attempt {attempts} of {max_attempts}")
                if attempts >= max_attempts:
                    self.logger.error(f" [-] Failed to set dataframe after {max_attempts} attempts.")
                    break