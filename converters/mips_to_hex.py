import random
import os
import sys
from mips_to_machine import *

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))

from mips_instructions import *


instructions = {
    'add': 1,
    'addu': 2,
    'and': 3,
    'jr': 4,
    'nor': 5,
    'or': 6,
    'slt': 7,
    'sltu': 8,
    'sll': 9,
    'srl': 10,
    'sub': 11,
    'subu': 12,
    'div': 13,
    'divu': 14,
    'mfhi': 15,
    'mflo': 16,
    'mult': 17,
    'multu': 18,
    'mfc0': 19,
    'sra': 20,
    'addi': 21,
    'addiu': 22,
    'andi': 23,
    'beq': 24,
    'bne': 25,
    'lbu': 26,
    'lhu': 27,
    'll': 28,
    'lui': 29,
    'lw': 30,
    'ori': 31,
    'slti': 32,
    'sltiu': 33,
    'sb': 34,
    'sc': 35,
    'sh': 36,
    'sw': 37,
    'j': 38,
    'jal': 39
}

def mips_instruction_generator(instructionType):
    instructionType = instructionType.lower()
    mnemonic = ""

    rs = get_register_name(random.randint(8,25)) 
    rt = get_register_name(random.randint(8,25)) 
    rd = get_register_name(random.randint(8,25)) 


    if instructionType in ['rtype']:
        num = random.randint(1,20)
        for name, value in instructions.items():
            if value == num:
                mnemonic = name

                if mnemonic in ["add", "addu", "and", "slt", "sltu", "sub", "subu", "nor", "or"]:
                    return f"{mnemonic} ${rd}, ${rs}, ${rt}"

                if mnemonic in ["sll", "srl"]:
                    shamt = random.randint(0,31)
                    return f"{mnemonic} ${rd}, ${rt}, {shamt}"
                
                if mnemonic in ["div", "divu", "mult", "multu"]:
                    return f"{mnemonic} ${rs}, ${rt}"
                
                if mnemonic in ["mfhi", "mflo"]:
                    return f"{mnemonic} ${rd}"
                
                if mnemonic in ["mfc0"]:
                    return f"{mnemonic} ${rd}, ${rs}"
                
                if mnemonic in ["sra"]:
                    shamt = random.randint(0,31)
                    return f"{mnemonic} ${rd}, ${shamt}"
                
    elif instructionType in ["itype"]:
        num = random.randint(21,37)
        for name, value in instructions.items():
            if value == num:
                mnemonic = name
                immediate = random.randint(0, 65535)
                if mnemonic in ["addi", "addiu", "andi", "slti", "sltiu", "ori"]:
                    return f"{mnemonic} ${rt}, ${rs}, {immediate}"

                if mnemonic in ["sb", "sc", "sh", "sw", "lbu", "lhu", "ll", "lw"]:
                    immediate = random.randint(0,32)
                    return f"{mnemonic} ${rs}, {immediate}(${rt})"
                
                if mnemonic in ["bne", "beq"]:
                    return f"{mnemonic} ${rs}, {rt}, {immediate}"
                
                return f"{mnemonic} ${rt}, {immediate}" # lui
    
    elif instructionType in ["jtype"]:
        num = random.randint(38,39)
        for name, value in instructions.items():
            if value == num:
                mnemonic = name

                if mnemonic in ["jr"]:
                    return f"{mnemonic} $ra"
                
                return f"{mnemonic}"
    

def mips_to_hex():
    instruction_type = input("which instruction type do you want to convert? ")
    instruction = mips_instruction_generator(instruction_type)

    instruction_in_binary = mips_to_machine(instruction)

    try: 
        assert int(input(f"Enter the hex for this instruction: {instruction}\n"), 16) == int(instruction_in_binary,2)
        print("CORRECT!!!")
    except AssertionError:
        print("INCORRECT LOSA!")



mips_to_hex()
