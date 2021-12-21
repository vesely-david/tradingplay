from datetime import date

import pytest

from convertor.yahoo_convertor import YahooConvertor


@pytest.mark.parametrize(
    'value,expected',
    [
        (1.0, 22.3280),
        (10, 223.280)
    ]
)
def test_converts_usd_to_czk(value, expected):
    convertor = YahooConvertor(ticker='CZK=X')
    converted = convertor.convert(value, date(2021, 12, 20))
    assert converted == pytest.approx(expected, 0.001)


@pytest.mark.parametrize(
    'value,expected',
    [
        (1.0, 1/22.3280),
        (10, 10/22.3280)
    ]
)
def test_converts_czk_to_usd(value, expected):
    convertor = YahooConvertor(ticker='CZK=X', inverse=True)
    converted = convertor.convert(value, date(2021, 12, 20))
    assert converted == pytest.approx(expected, 0.001)


@pytest.mark.parametrize(
    'value,expected',
    [
        (1.0, 46880.28),
        (10, 468802.8)
    ]
)
def test_converts_btc_to_usd(value, expected):
    convertor = YahooConvertor(ticker='BTC-USD')
    converted = convertor.convert(value, date(2021, 12, 20))
    assert converted == pytest.approx(expected, 0.001)
