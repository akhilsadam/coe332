from typing import Type
import water   
import numpy as np
import pytest
# class tests:

def test_turbid():
    assert water.turbid(3,4) == 12
    assert water.turbid(3,0) == 0
    assert type(water.turbid(3,4)) == int
    assert type(water.turbid(3.1,0)) == float
    assert water.turbid(3.1,4) == 12.4
# Note no exceptions necessary for this function as it has been designed quite simply.

def test_time():
    assert water.time(1,1) == 0.0
    assert type(water.time(1,0.5)) == np.float64
    assert abs(water.time(40) - 182.5) < 0.5
    assert water.time(1,1,2.0) == -1
    assert water.time(-1) == -1
    with pytest.raises(TypeError):
        water.time(np.abs,3)
    with pytest.raises(TypeError):
        water.time(3,'a')

def test_sort():
    assert type(water.sort([
        {"a":5,"b":6},
        {"a":4,"b":8},
        {"a":5,"b":7}
    ],"b")) == list
    assert water.sort([],"b") == []
    assert water.sort([
        {"a":5},
        {"a":4},
        {"a":5}
    ],"a") == [
        {"a":5},
        {"a":5},
        {"a":4}
    ]
    assert water.sort([
        {"a":4,"b":8},
    ],"b") == [
        {"a":4,"b":8},
    ]
    assert water.sort([
        {"a":5,"b":6},
        {"a":4,"b":8},
        {"a":5,"b":7}
    ],"b") == [
        {"a":4,"b":8},
        {"a":5,"b":7},
        {"a":5,"b":6}
    ]
    with pytest.raises(TypeError):
        water.sort(3)

def test_current():
    assert type(water.current([
        {water.cc:5,water.dc:6},
    ])) == float
    assert water.current([
        {water.cc:5,water.dc:6},
    ]) == 30
    assert water.current([
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:4,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:5,water.dc:6},
    ]) == 84/5
    assert water.current([
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:4,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:6},
    ]) == 84/5
    assert water.current([
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:4,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:5,water.dc:6},
    ],1) == 30
    with pytest.raises(TypeError):
        water.current([
        {water.cc:5,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:4,water.dc:6},
        {water.cc:5,water.dc:0},
        {water.cc:5,water.dc:6},
        ],1.45)
    with pytest.raises(TypeError):
        water.current("Really?",1)
    
def test_read():
    assert type(water.read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json"))==dict
    assert type(water.read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")[water.name])==list
    assert type(water.read("---"))==dict #since we now have the data downloaded
    assert water.read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")[water.name][0][water.cc] == 1.022
    assert water.read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")[water.name][5][water.dc] == 1.104
    with pytest.raises(TypeError):
        water.read(3)
    

# def run():
#     "Run all tests."
#     for test in dir(tests):
#         item = getattr(tests,test)
#         if callable(item) and test.startswith('test'):
#             print(item)
#             item()

# if __name__ == '__main__':
#     run()
