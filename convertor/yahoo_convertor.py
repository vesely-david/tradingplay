from datetime import date, timedelta

from pandas import Timestamp
import yfinance as yf


class YahooConvertor:
    def __init__(self, ticker: str):
        self._ticker = ticker

    def convert(self, value: float, date_: date):
        ten_days = timedelta(days=10)
        _date_min = (date_ - ten_days).strftime('%Y-%m-%d')
        _date_max = (date_ + ten_days).strftime('%Y-%m-%d')
        prices = yf.download(self._ticker, start=_date_min, end=_date_max)
        return prices.loc[Timestamp(date_), "Close"] * value
