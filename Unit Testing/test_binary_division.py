import pytest
import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from binaryArith.binaryArith import *


"""
Test Case Groups (Only testing 4 bit numbers):
1. Basic Division
2. Dividing a smaller number by a bigger number
3. Positive and negative
4. Test for double negative, should be the same as normal
"""

#the format for these tests are [[dividend, divisor], [dividend, divisor, quotient]]
#idk how to tell when the divisor is supposed to be 1 or 0, if someone can figure that out that would be nice
division_tests = [

#some basic division
[["0010", "0001"], ["0000", "0", "0010"]], # 1 / 1 = 1 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 2 / 1 = 2 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 3 / 1 = 3 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 4 / 1 = 4 r 0
[["0010", "0001"], ["0000", "0", "0010"]], # 4 / 2 = 2 r 0
[["0101", "0010"], ["0001", "1", "0010"]], # 5 / 2 = 2 r 1
[["0101", "0011"], ["0010", "1", "0001"]], # 5 / 3 = 1 r 2
[["1000", "0100"], ["0000", "0", "0010"]], # 8 / 4 = 2 r 0 


#dividing a smaller number by a larger number
[["0001", "0101"], ["0101", "0", "0000"]], # 1 / 5 = 0 r 5
[["0001", "0010"], ["0010", "1", "0000"]], # 1 / 2 = 0 r 2
[["0010", "0101"], ["0101", "0", "0000"]], # 2 / 5 = 0 r 5
[["0011", "0111"], ["0111", "1", "0000"]], # 3 / 7 = 0 r 7

]

@pytest.mark.parametrize("input, expected", division_tests)
def test_divAlg_(input, expected):
    result = divAlg(input[0], input[1], False)
    # Check if the second-to-last element of return value matches the expected output
    assert result == [expected[0], expected[1], expected[2]], f"Failed for input {input}: expected {expected}, got {result[-2]}"
