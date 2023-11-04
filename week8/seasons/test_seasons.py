from seasons import convert
import pytest


def test_convert():
    assert (
        convert(7547)
        == "Ten million, eight hundred sixty-seven thousand, six hundred eighty minutes"
    )
    assert convert(7665) == "Eleven million, thirty-seven thousand, six hundred minutes"
