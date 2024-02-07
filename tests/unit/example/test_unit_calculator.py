# tests/unit/test_unit_calculator.py

import pytest

import sys

for p in sys.path : print(p)

for m in sys.modules: 
    if m == 'lzma':  print('-----------------', m)

from src.example.calculator import Calculator




@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3

def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3
