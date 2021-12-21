from datetime import date, timedelta

from pandas import Timestamp
import yfinance as yf


class YahooConvertor:
    """
    Convertor using yahoo finance to retrieve data.

    Parameters
    ----------
    ticker: str
        Yahoo finance valid ticker

    inverse: bool, default = False
        Uses inverse prices from ticker. The main goal is to enable using the same ticker
        for "currency -> symbol" as well as "symbol -> currency" conversion.

    precision: int, default = 3
        The ticker price value will be rounded to precision before conversion
    """
    def __init__(self, ticker: str, inverse: bool = False, precision: int = 3):
        self._ticker = ticker
        self._inverse = inverse
        self._precison = precision

    def convert(self, value: float, date_: date):
        price = self._find_price(date_)

        if self._inverse:
            return value * (1 / price)
        else:
            return value * price

    def _find_price(self, date_: date):
        ten_days = timedelta(days=10)
        _date_min = (date_ - ten_days).strftime('%Y-%m-%d')
        _date_max = (date_ + ten_days).strftime('%Y-%m-%d')
        prices = yf.download(self._ticker, start=_date_min, end=_date_max)
        close_price = prices.loc[Timestamp(date_), "Close"]
        return round(close_price, self._precison)
