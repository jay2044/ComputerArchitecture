import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from converters.machine_to_mips import *

def test_machineToMipsConversionRType():
    machineCode = "00000001010010110100100000100000"

    assert checkForOpcode(machineCode) == "add t1 t2 t3"

    machineCode = "00000010101010111000100000100100"

    assert checkForOpcode(machineCode) == "and s1 s5 t3"


def test_machineToMipsConversionIType():
    machineCode = "00100010011110000000000000100101"

    assert checkForOpcode(machineCode) == "addi t8 s3 37"


def test_machineToMipsConversionJType():
    machineCode = "00001000000000000010000000000000"

    assert checkForOpcode(machineCode) == "j 0x2000"
