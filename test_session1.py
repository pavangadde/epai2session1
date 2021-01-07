import pytest
import inspect
from test_utils import *
import re

import session1


WIDTH = 10
HEIGHT = 20
def test_fourspace_equal():
    assert fourspace(session1) == False, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session1) == False, "One of your function has a capitalized alphabet!"

# def test_rectangle_repr():
#     r = session1.Rectangle(WIDTH, HEIGHT)
#     assert r.__repr__() == f'Rectangle({WIDTH}, {HEIGHT})', 'The representation of the Rectangle object does not meet expectations'
