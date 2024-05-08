import pytest
import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from binaryArith.binaryArith import *

# Testing Groups (All four bit numbers)
# 1. Positive * Positive
# 2. Positive * Negative
# 3. Negative * Positive
# 4. Negative * Negative

#TODO actually set up tests for the dvision algorithm, should be similar to the multiplication algorithm
#The quotient should always be the length of the bigger element, either the dividend or the divisor
#The remainder should also follow suit
division_tests = [
[["0010", "0001"], ["0000", "0", "0010"]], # 1 / 1 = 1 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 2 / 1 = 2 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 3 / 1 = 3 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 4 / 1 = 4 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 4 / 2 = 2 r 0
[["0101", "0010"], ["0001", "1", "0010"]], # 5 / 2 = 2 r 1
[["0101", "0011"], ["0010", "1", "0001"]], # 5 / 3 = 1 r 2
[["1000", "0100"], ["0000", "0", "0010"]], # 8 / 4 = 2 r 0 

#idk how to fix this one
[["0001", "0101"], ["0101", "0", "0000"]], # 1 / 5 = 0 r 5

]

@pytest.mark.parametrize("input, expected", division_tests)
def test_divAlg_(input, expected):
    result = divAlg(input[0], input[1], False)
    # Check if the second-to-last element of return value matches the expected output
    assert result == [expected[0], expected[1], expected[2]], f"Failed for input {input}: expected {expected}, got {result[-2]}"
