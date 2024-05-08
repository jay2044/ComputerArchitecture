"""
File: mips_instructions.py
Description: Defines classes and functions for MIPS instructions.

Instructions are represented by objects of RType, IType, and JType classes.

instruction_dictionary: Dictionary mapping MIPS instruction mnemonics to their opcode and function code.
named_registers: Dictionary mapping register names to their corresponding numbers.

RType: Class representing R-Type MIPS instructions.
IType: Class representing I-Type MIPS instructions.
JType: Class representing J-Type MIPS instructions.

r_type_instruction: Constructs an R-Type MIPS instruction object.
i_type_instruction: Constructs an I-Type MIPS instruction object.
j_type_instruction: Constructs a J-Type MIPS instruction object.
get_register_name: Retrieves the name of a register based on its number.
type_of_instruction: Determines the type of MIPS instruction ('rtype', 'itype', or 'jtype').
"""

instruction_dictionary = {
    'add': ['0', '20'],
    'addu': ['0', '21'],
    'and': ['0', '24'],
    'jr': ['0', '8'],
    'nor': ['0', '27'],
    'or': ['0', '25'],
    'slt': ['0', '2a'],
    'sltu': ['0', '2b'],
    'sll': ['0', '00'],
    'srl': ['0', '02'],
    'sub': ['0', '22'],
    'subu': ['0', '23'],
    'div': ['0', '1a'],
    'divu': ['0', '1b'],
    'mfhi': ['0', '10'],
    'mflo': ['0', '12'],
    'mult': ['0', '18'],
    'multu': ['0', '19'],
    'mfc0': ['10', '0'],
    'sra': ['0','3'],
    'addi': '8',
    'addiu': '9',
    'andi': 'c',
    'beq': '4',
    'bne': '5',
    'lbu': '24',
    'lhu': '25',
    'll': '30',
    'lui': 'f',
    'lw': '23',
    'ori': 'd',
    'slti': 'a',
    'sltiu': 'b',
    'sb': '28',
    'sc': '38',
    'sh': '29',
    'sw': '2b',
    'j': '2',
    'jal': '3'
}

named_registers = {
    "0": 0,
    "zero": 0,
    "at": 1,
    "v0": 2,
    "v1": 3,
    "a0": 4,
    "a1": 5,
    "a2": 6,
    "a3": 7,
    "t0": 8,
    "t1": 9,
    "t2": 10,
    "t3": 11,
    "t4": 12,
    "t5": 13,
    "t6": 14,
    "t7": 15,
    "s0": 16,
    "s1": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "t8": 24,
    "t9": 25,
    "k0": 26,
    "k1": 27,
    "gp": 28,
    "sp": 29,
    "fp": 30,
    "ra": 31
}


class RType:
    def __init__(self, opcode, rs, rt, rd, shamt, funct):
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct
        self.type = __class__.__name__


class IType:
    def __init__(self, opcode, rs, rt, immediate):
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.immediate = immediate
        self.type = __class__.__name__


class JType:
    def __init__(self, opcode, address):
        self.opcode = opcode
        self.address = address
        self.type = __class__.__name__


def r_type_instruction(mnemonic, rs, rt, rd, shamt):
    """
    Constructs an R-Type MIPS instruction object.

    Args:
        mnemonic (str): The mnemonic code of the instruction.
        rs (str): The source register.
        rt (str): The target register.
        rd (str): The destination register.
        shamt (str): The shift amount.

    Returns:
        RType: An R-Type MIPS instruction object.
    """
    instruction_opcode_and_funct = instruction_dictionary.get(mnemonic)
    opcode = bin(int(instruction_opcode_and_funct[0], 16))[2:]
    funct = bin(int(instruction_opcode_and_funct[1], 16))[2:]
    return RType(opcode, rs, rt, rd, shamt, funct)


def i_type_instruction(mnemonic, rs, rt, immediate):
    """
    Constructs an I-Type MIPS instruction object.

    Args:
        mnemonic (str): The mnemonic code of the instruction.
        rs (str): The source register.
        rt (str): The target register.
        immediate (str): The immediate value.

    Returns:
        IType: An I-Type MIPS instruction object.
    """
    opcode = bin(int(instruction_dictionary[mnemonic], 16))[2:].zfill(6)
    return IType(opcode, rs, rt, immediate)


def j_type_instruction(mnemonic, address):
    """
    Constructs a J-Type MIPS instruction object.

    Args:
        mnemonic (str): The mnemonic code of the instruction.
        address (str): The target address.

    Returns:
        JType: A J-Type MIPS instruction object.
    """
    instruction_opcode = instruction_dictionary.get(mnemonic)
    opcode = bin(int(instruction_opcode[0], 16))[2:]
    return JType(opcode, address)


def get_register_name(register_number):
    """
    Retrieves the name of a register based on its number.

    Args:
        register_number (int): The register number.

    Returns:
        str: The name of the register.
    """
    for name, value in named_registers.items():
        if value == register_number:
            return name


def type_of_instruction(instruction):
    """
    Determines the type of MIPS instruction.

    Args:
        instruction (str): The MIPS instruction.

    Returns:
        str: The type of instruction ('rtype', 'itype', or 'jtype').
    """
    instruction = instruction.lower()

    r_type = ["add", "addu", "and", "jr", "nor", "or", "slt", "sltu", "sll", "srl", "sub", "subu", "div", "divu", "mfhi", "mflo", "mfc0", "mult", "multu", "sra"]
    i_type = ["addi", "addiu", "andi", "beq", "bne", "lbu", "lhu", "ll", "lui", "lw", "ori", "slti", "sltiu", "sb", "sc", "sh", "sw"]
    j_type = ["j", "jal"]

    if instruction in r_type:
        return 'rtype'

    if instruction in i_type:
        return 'itype'

    if instruction in j_type:
        return 'jtype'
