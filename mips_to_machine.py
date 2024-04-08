def register_to_bin(register):
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
    register_cleaned = register.lower().replace("$", "")
    if register_cleaned in named_registers:
        reg_num = named_registers[register_cleaned]
    else:
        try:
            reg_num = int(register_cleaned)
        except ValueError:
            return "Error: Invalid register name or number."
    return format(reg_num, '05b')


def r_type(opcode, rs, rt, rd, shamt, funct):
    funct_bin = format(int(funct, 16), '06b')
    print(f"{opcode}{register_to_bin(rs)}{register_to_bin(rt)}{register_to_bin(rd)}{format(shamt, '05b')}{funct_bin}")
    return f"{opcode}{register_to_bin(rs)}{register_to_bin(rt)}{register_to_bin(rd)}{format(shamt, '05b')}{funct_bin}"


def i_type(opcode, rs, rt, immediate):
    f"{opcode}{register_to_bin(rs)}{register_to_bin(rt)}{imm_to_bin(immediate)}"
    return f"{opcode}{register_to_bin(rs)}{register_to_bin(rt)}{imm_to_bin(immediate)}"


def j_type(opcode, address):
    address = int(address)
    return f"{opcode}{format(address, '026b')}"


def imm_to_bin(immediate, bits=16):
    immediate = int(immediate)
    if immediate < 0:
        immediate = (1 << bits) + immediate
    return format(immediate, f'0{bits}b')


def assemble_mips_instruction(instruction):
    components = instruction.replace(',', '').split()
    opcode = components[0]

    opcodes = {
        'add': ('000000', '20'),  # R-type: opcode, funct
        'sub': ('000000', '22'),  # R-type: opcode, funct
        'lw': ('100011',),  # I-type: opcode
        'sw': ('101011',),  # I-type: opcode
        'beq': ('000100',),  # I-type: opcode
        'and': ('000000', '24'),  # R-type: opcode, funct
        'or': ('000000', '25'),  # R-type: opcode, funct
        'slt': ('000000', '2A'),  # R-type: opcode, funct
        'addi': ('001000',),  # I-type: opcode
        'ori': ('001101',),  # I-type: opcode
        'sll': ('000000', '00'),  # R-type: opcode, funct
        'srl': ('000000', '02'),  # R-type: opcode, funct
        'j': ('000010',),  # J-type: opcode
        'jal': ('000011',),  # J-type: opcode
    }

    if opcode in ['add', 'sub', 'and', 'or', 'slt', 'sll', 'srl']:
        opcode_bin, funct = opcodes[opcode]
        return r_type(opcode_bin, components[2], components[3], components[1], 0, funct)
    elif opcode in ['lw', 'sw', 'beq', 'addi', 'ori']:
        opcode_bin = opcodes[opcode][0]
        if opcode in ['lw', 'sw']:
            offset, base = components[2].split('(')
            base = base[:-1]
            return i_type(opcode_bin, base, components[1], offset)
        elif opcode in ['beq', 'bne']:
            return i_type(opcode_bin, components[1], components[2], components[3])
        else:
            return i_type(opcode_bin, components[2], components[1], components[3])
    elif opcode in ['j', 'jal']:
        opcode_bin = opcodes[opcode][0]
        address = int(components[1])
        return j_type(opcode_bin, address)

    return "Instruction format not supported."


assemble_mips_instruction("add $t1, $t2, $t3")
