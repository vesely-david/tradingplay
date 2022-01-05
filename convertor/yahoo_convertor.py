from datetime import date

from pandas import Timestamp, Series
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
        self._prices = yf.download(self._ticker)

    def convert(self, value: float, date_: date):
        price = self._find_price(date_)

        if self._inverse:
            return value * (1 / price)
        else:
            return value * price

    def _find_price(self, date_: date):
        ts = Timestamp(date_)
        if ts not in self._prices.index:
            diffs = Series(self._prices.index - ts).abs()
            i = diffs.argmin()
            ts = self._prices.index[i]

        close_price = self._prices.loc[ts, "Close"]
        return round(close_price, self._precison)
