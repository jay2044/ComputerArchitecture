import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from binaryArith.binaryArith import *

#testing set up for a single test of array of values
single_test = [
    [["0001","0100"],["01000000","0000","00000100"]],
    [["0100","0001"],["00010000","0000","00000100"]]
    ]


def test_binMultiplication():
    # Combine all test cases into a single list for easier processing
    all_test_cases = single_test

    # Track the number of failed tests
    failed_tests = 0

    for test_case in all_test_cases:
        bit_string_input, expected_bit_string = test_case
        try:
            received_bit_string = multAlg(bit_string_input[0], bit_string_input[1])
        except Exception as e:
            print(f"Error doing multiplication: {bit_string_input}")
            print(f"\t{e}")
            failed_tests += 1
            continue
        
        i = 0
        for value in received_bit_string:
            if value != expected_bit_string[i]:
                print(f"Failed test for: {bit_string_input} expected: {expected_bit_string} received: {received_bit_string}")
                failed_tests += 1
                break
            i +=1

    if failed_tests == 0:
        print("All tests passed successfully.")
    else:
        print(f"{failed_tests} tests failed.")


test_binMultiplication()