from typing import Type
import land   
import numpy as np
import pytest

def test_avg():
    ld = [{"a":5,"b":6},
        {"a":4,"b":8},
        {"a":5,"b":7}]
    assert land.average(ld,'a') == 14/3
    assert land.average(ld,'b') == 7
    with pytest.raises(KeyError):
        land.average(ld,'5')
    assert type(land.average(ld,'a')) == float
    assert land.average([{"a":5,"b":6}],'a') == 5
    with pytest.raises(ZeroDivisionError):
        land.average([],'5')

def test_loc():
    lat = [1,2,1,-5,-1]
    long = [4,1,-5,9,-2]
    out = ['Northern & Eastern','Northern & Eastern','Northern & Western','Southern & Eastern','Southern & Western']
    assert [land.loc(latk,longk) for latk,longk in zip(lat,long)] == out
    with pytest.raises(ValueError):
        land.loc(0,1)
    with pytest.raises(ValueError):
        land.loc(1,0)

def test_count():
    ld = [{"a":5,"b":6},
        {"a":4,"b":8},
        {"a":5,"b":7}]
    assert land.count(ld,'a') == {5:2,4:1}
    assert land.count(ld,'b') == {6:1,7:1,8:1}
    with pytest.raises(KeyError):
        land.count(ld,'5')
    assert type(land.count(ld,'a')) == dict
    assert land.count([{"a":5,"b":6}],'a') == {5:1}