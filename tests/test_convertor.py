from datetime import date

import pytest

from convertor.yahoo_convertor import YahooConvertor


@pytest.mark.parametrize(
    'value,expected',
    [
        (1.0, 22.3430),
        (10, 223.430)
    ]
)
def test_converts_usd_to_czk(value, expected):
    convertor = YahooConvertor(ticker='CZK=X')
    converted = convertor.convert(value, date(2021, 12, 21))
    assert converted == pytest.approx(expected, 0.001)


@pytest.mark.parametrize(
    'value,expected',
    [
        (1.0, 1/22.3430),
        (10, 10/22.3430)
    ]
)
def test_converts_czk_to_usd(value, expected):
    convertor = YahooConvertor(ticker='CZK=X', inverse=True)
    converted = convertor.convert(value, date(2021, 12, 21))
    assert converted == pytest.approx(expected, 0.001)
