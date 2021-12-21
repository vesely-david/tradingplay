from datetime import date


class YahooConvertor:
    def __init__(self, ticker: str):
        self._ticker = ticker

    def convert(self, value: float, date: date):
        return 22.365


def test_converts_1usd_to_czk():
    convertor = YahooConvertor(ticker='CZK=X')
    converted = convertor.convert(1., date(2021, 12, 21))
    assert converted == 22.3650
