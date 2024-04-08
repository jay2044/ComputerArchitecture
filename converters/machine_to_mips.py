from mips_instructions import *

# testing variable
string = "00110101010010010000000000100101"


# r type conversion
def rTypeConversion(machineCode, opcode, funct):
    for name, value in instruction_dictionary.items():
        if funct != -1 and funct == int(value[1], 16):
            rs = get_register_name(int(machineCode[6:11], 2))
            rt = get_register_name(int(machineCode[11:16], 2))
            rd = get_register_name(int(machineCode[16:21], 2))
            shamt = int(machineCode[21:26], 2)

            # instruction = rTypeInstruction(opcode,rs,rt,rd, funct)
            return f"{name} {rs} {rt} {rd}"


# i type and jtype conversion
def eitherITypeORJType(machineCode, opcode):
    for name, value in instruction_dictionary.items():
        if isinstance(value, str) and opcode == int(value, 16):
            type = type_of_instruction(name)

            if type == 'itype':
                rs = get_register_name(int(machineCode[6:11], 2))
                rt = get_register_name(int(machineCode[11:16], 2))
                immediate = int(machineCode[16:], 2)
                # instruction = iTypeInstruction(opcode,rs,rt,immediate)
                return f"{name} {rt} {rs} {immediate}"
            else:
                address = int(machineCode[5:], 2)
                # instruction = jTypeInstruction(opcode, address)
                return f"{name} {hex(address)}"

            # USE THIS FUNCTION TO USE THE FILE


def checkForOpcode(machinecode):
    opcode = int(machinecode[0:6], 2)
    funct = -1
    if opcode == 0:
        funct = int(machinecode[26:], 2)
        return rTypeConversion(machinecode, opcode, funct)
    else:
        return eitherITypeORJType(machinecode, opcode)