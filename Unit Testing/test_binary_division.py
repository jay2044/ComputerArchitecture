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

mult_tests = [
    [["0001","0001", False],["00010000","0000","00000001"]], #1 * 1
    [["0001","0010", False],["00010000","0000","00000010"]], #1 * 2
    [["0010","0001", False],["00100000","0000","00000010"]], #2 * 1
    [["0001","0011", False],["00010000","0000","00000011"]], #1 * 3
    [["0011","0001", False],["00110000","0000","00000011"]], #3 * 1
    [["0001","0100", False],["00010000","0000","00000100"]], #1 * 4
    [["0100","0001", False],["01000000","0000","00000100"]], #4 * 1
    ]

def test_multAlg():
    for values in mult_tests:
        assert multAlg(values[0][0], values[0][1], values[0][2]) == [values[1][0],values[1][1],values[1][2]]