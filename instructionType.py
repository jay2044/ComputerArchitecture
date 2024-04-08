# all in hex, format: opcode funct
instruction_dictionary = {
    'add':      ['0','20'], # start of r-type instructions
    'addu':     ['0','21'],
    'and':      ['0','24'],
    'jr':       ['0','8'],
    'nor':      ['0','27'],
    'or':       ['0','25'],
    'slt':      ['0','2a'],
    'sltu':     ['0','2b'],
    'sll':      ['0','00'],
    'srl':      ['0','02'],
    'sub':      ['0','22'],
    'subu':     ['0','23'],
    'addi':     '8', # start of i-type instructions
    'addiu':    '9',
    'andi':     'c',
    'beq':      '4',
    'bne':      '5',
    'lbu':      '24',
    'lhu':      '25',
    'll':       '30',
    'lui':      'f',
    'lw':       '23',
    'ori':      'd',
    'slti':     'a',
    'sltiu':    'b',
    'sb':       '28',
    'sc':       '38',
    'sh':       '29',
    'sw':       '2b',
    'j':        '2', # start of j-type instructions
    'jal':      '3'
}

named_registers = {
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



# not used in machine_to_mips but can be used to convert mips to machine : )
########################################################################################################################
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


# can use these to convert mips to machine code?
def rTypeInstruction(mnemonic, rs, rt, rd):
    instructionOpcodeAndFunct = instruction_dictionary.get(mnemonic)
    # converts to binary and gets rid of 0b in front of the string
    opcode = bin(int(instructionOpcodeAndFunct[0], 16))[2:]
    funct =  bin(int(instructionOpcodeAndFunct[1], 16))[2:]
    return RType(opcode,rs,rt,rd,00000,funct)    

def iTypeInstruction(mnemonic, rs, rt, immediate):
    instructionOpcode = instruction_dictionary.get(mnemonic)
    # converts to binary and gets rid of 0b in front of the string
    opcode = bin(int(instructionOpcode[0], 16))[2:]
    return IType(opcode,rs,rt,immediate)

def jTypeInstruction(mnemonic, address):
    instructionOpcode= instruction_dictionary.get(mnemonic)
    # converts to binary and gets rid of 0b in front of the string
    opcode = bin(int(instructionOpcode[0], 16))[2:]
    return JType(opcode,address)



##########################################################################################


def getRegisterName(registerNumber):
    for name, value in named_registers.items():
        if value == registerNumber:
            return name

def typeOfInstruction(instruction):
    instruction = instruction.lower()

    rtype = ["add", "addu", "and", "jr", "nor", "or", "slt", "sltu", "sll", "srl", "sub", "subu"]
    itype = ["addi", "addiu", "andi", "beq", "bne", "lbu", "lhu", "ll", "lui", "lw", "ori", "slti", "sltiu", "sb", "sc", "sh", "sw"]
    jtype = ["j", "jal"]

    if instruction in rtype:
        return 'rtype'

    if instruction in itype:
        return 'itype'

    if instruction in jtype:
        return 'jtype'
    



def selectsAnInstructionType(instruction):
    instruction = instruction.replace(',', '').split()
    mnemonic = instruction[0]
    instructionType = typeOfInstruction(mnemonic)
    if instructionType == 'rtype':
        register1 = bin(named_registers.get(instruction[1]))[2:].zfill(5)
        register2 = bin(named_registers.get(instruction[2]))[2:].zfill(5)
        register3 = bin(named_registers.get(instruction[3]))[2:].zfill(5)
        machine = rTypeInstruction(mnemonic,register1,register2,register3)
        # unsure on how to do the shamt of an RTYPE instruction
        print(f"{machine.opcode.zfill(6)} {machine.rs} {machine.rd} {machine.rt} {machine.shamt} {machine.funct}")

    if instructionType == 'itype':
        register1 = bin(named_registers.get(instruction[1]))[2:].zfill(5)
        register2 = bin(named_registers.get(instruction[2]))[2:].zfill(5)
        immediate = bin(int(instruction[3]))[2:].zfill(16)
        machine = iTypeInstruction(mnemonic,register1,register2,immediate)
        print(f"{machine.opcode.zfill(6)}{machine.rs}{machine.rt}{machine.immediate}")

    if instructionType == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = jTypeInstruction(mnemonic, address)
        print(f"{machine.opcode.zfill(6)}{machine.address}")
        
    
selectsAnInstructionType("j, 0x2000")