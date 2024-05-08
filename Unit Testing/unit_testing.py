import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
<<<<<<< HEAD
from converters.machine_to_mips import machine_to_mips

=======
from converters.machine_to_mips import *
from binaryArith.binaryArith import *
>>>>>>> 6425afd4ec4e5044a93ceaf42d2ff3191f48cdf1

def test_machineToMipsConversionRType():
    machineCode = "00000001010010110100100000100000"

<<<<<<< HEAD
    assert machine_to_mips(machineCode) == "add t1 t2 t3"

    machineCode = "00000010101010111000100000100100"

    assert machine_to_mips(machineCode) == "and s1 s5 t3"
=======
    assert checkForOpcode(machineCode) == "add t1 t2 t3"

    machineCode = "00000010101010111000100000100100"

    assert checkForOpcode(machineCode) == "and s1 s5 t3"
>>>>>>> 6425afd4ec4e5044a93ceaf42d2ff3191f48cdf1


def test_machineToMipsConversionIType():
    machineCode = "00100010011110000000000000100101"

<<<<<<< HEAD
    assert machine_to_mips(machineCode) == "addi t8 s3 37"
=======
    assert checkForOpcode(machineCode) == "addi t8 s3 37"
>>>>>>> 6425afd4ec4e5044a93ceaf42d2ff3191f48cdf1


def test_machineToMipsConversionJType():
    machineCode = "00001000000000000010000000000000"

<<<<<<< HEAD
    assert machine_to_mips(machineCode) == "j 0x2000"
=======
    assert checkForOpcode(machineCode) == "j 0x2000"
>>>>>>> 6425afd4ec4e5044a93ceaf42d2ff3191f48cdf1
