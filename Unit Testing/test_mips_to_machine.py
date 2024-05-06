# from converters.mips_to_machine import mips_to_machine

import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from converters.mips_to_machine import mips_to_machine


# Test examples:
r_type_test_examples = [
    ["add $t1, $t2, $t3", "00000001010010110100100000100000"],  # add
    ["addu $t1, $t2, $t3", "00000001010010110100100000100001"],  # addu
    ["and $t1, $t2, $t3", "00000001010010110100100000100100"],  # and
    ["jr $ra", "00000011111000000000000000001000"],  # jr
    ["nor $t1, $t2, $t3", "00000001010010110100100000100111"],  # nor
    ["or $t1, $t2, $t3", "00000001010010110100100000100101"],  # or
    ["slt $t1, $t2, $t3", "00000001010010110100100000101010"],  # slt
    ["sltu $t1, $t2, $t3", "00000001010010110100100000101011"],  # sltu
    ["sll $t1, $t2, 2", "00000000000010100100100010000000"],  # sll
    ["srl $t1, $t2, 2", "00000000000010100100100010000010"],  # srl
    ["sub $t1, $t2, $t3", "00000001010010110100100000100010"],  # sub
    ["subu $t1, $t2, $t3", "00000001010010110100100000100011"],  # subu
    ["div $t1, $t2", "00000001001010100000000000101010"],  # div
    ["divu $t1, $t2", "00000001001010100000000000101011"],  # divu
    ["mfhi $t1", "00000000000000000100100000010000"],  # mfhi
    ["mflo $t1", "00000000000000000100100000010010"],  # mflo
    ["mfc0 $t1, $0", "01000000000010010000000000000000"],  # mfc0, note: coprocessor 0 instruction
    ["mult $t1, $t2", "00000001001010100000000000011000"],  # mult
    ["multu $t1, $t2", "00000001001010100000000000011001"],  # multu
    ["sra $t1, $t2, 2", "00000000000010100100100000000011"]  # sra
]

i_type_test_examples = [
    ["addi $t1, $t2, 10", "00100001010010010000000000001010"],  # addi
    ["addiu $t1, $t2, 10", "00100101010010010000000000001010"],  # addiu
    ["andi $t1, $t2, 15", "00110001010010010000000000001111"],  # andi
    ["beq $t1, $t2, 16", "00010001001010000000000000010000"],  # beq
    ["bne $t1, $t2, 16", "00010101001010000000000000010000"],  # bne
    ["lbu $t1, 32($t2)", "10010001010010010000000000100000"],  # lbu
    ["lhu $t1, 32($t2)", "10010101010010010000000000100000"],  # lhu
    ["ll $t1, 32($t2)", "11000001010010010000000000100000"],  # ll (Load Linked)
    ["lui $t1, 1024", "00111100000010010000010000000000"],  # lui
    ["lw $t1, 32($t2)", "10001101010010010000000000100000"],  # lw
    ["ori $t1, $t2, 255", "00110101010010011111111111111111"],  # ori
    ["slti $t1, $t2, -10", "00101001010010011111111111110110"],  # slti
    ["sltiu $t1, $t2, 10", "00101101010010010000000000001010"],  # sltiu
    ["sb $t1, 32($t2)", "10100001010010010000000000100000"],  # sb
    ["sc $t1, 32($t2)", "11100001010010010000000000100000"],  # sc (Store Conditional)
    ["sh $t1, 32($t2)", "10100101010010010000000000100000"],  # sh
    ["sw $t1, 32($t2)", "10101101010010010000000000100000"]  # sw
]

j_type_test_examples = [
    ["j 0x00400000", "00001000000000010000000000000000"],  # j
    ["jal 0x00400000", "00001100000000010000000000000000"],  # jal
    ["jr $ra", "00000011111000000000000000001000"]  # jr
]


def test_mips_to_machine():
    # Combine all test cases into a single list for easier processing
    all_test_cases = r_type_test_examples + i_type_test_examples + j_type_test_examples

    # Track the number of failed tests
    failed_tests = 0

    for test_case in all_test_cases:
        mips_instruction, expected_machine_code = test_case
        try:
            received_machine_code = mips_to_machine(mips_instruction)
        except Exception as e:
            print(f"Error processing instruction: {mips_instruction}")
            print(f"\tBecause of exception: {e}")
            failed_tests += 1
            continue

        if received_machine_code != expected_machine_code:
            mnemonic = mips_instruction.split()[0]
            print(f"Failed test for: {mnemonic.ljust(20)} expected: {expected_machine_code.ljust(10)} received: {received_machine_code}")

            failed_tests += 1

    if failed_tests == 0:
        print("All tests passed successfully.")
    else:
        print(f"{failed_tests} tests failed.")


test_mips_to_machine()
