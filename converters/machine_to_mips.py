from mips_instructions import *

# r type conversion
def rTypeConversion(machineCode, opcode, funct):
    for name, value in instruction_dictionary.items():
        if funct != -1 and funct == int(value[1], 16):
            rs = get_register_name(int(machineCode[6:11], 2))
            rt = get_register_name(int(machineCode[11:16], 2))
            rd = get_register_name(int(machineCode[16:21], 2))
            shamt = int(machineCode[21:26], 2)

            if name in ["add", "addu", "and", "slt", "sltu", "sub", "subu", "nor", "or"]:
                return f"{name} ${rd} ${rs} ${rt}"

            if name in ["sll", "srl"]:
                return f"{name} ${rd} ${rt} {shamt}"
            
            if name in ["div", "divu", "mult", "multu"]:
                return f"{name} ${rs} ${rt}"
            
            if name in ["mfhi", "mflo"]:
                return f"{name} ${rd}"
            
            if name in ["mfc0"]:
                return f"{name} ${rd} ${rs}"
            
            if name in ["sra"]:
                return f"{name} ${rd} ${rt}"
            


# i type and jtype conversion
def eitherITypeORJType(machineCode, opcode):
    for name, value in instruction_dictionary.items():
        if isinstance(value, str) and opcode == int(value, 16):
            type = type_of_instruction(name)

            if type == 'itype':
                rs = get_register_name(int(machineCode[6:11], 2))
                rt = get_register_name(int(machineCode[11:16], 2))
                immediate = int(machineCode[16:], 2)

                if name in ["addi", "addiu", "andi", "lbu", "lhu", "ll", "lw", "slti", "sltiu", "ori"]:
                    return f"{name} ${rt} ${rs} {immediate}"

                if name in ["bne", "beq", "sb", "sc", "sh", "sw"]:
                    return f"{name} ${rs} ${rt}"
                
                return f"{name} ${rt} {immediate}" # lui
            else:
                address = int(machineCode[5:], 2)
                return f"{name} {hex(address)}"



def checkForOpcode(machinecode):
    opcode = int(machinecode[0:6], 2)
    funct = -1
    if opcode == 0:
        funct = int(machinecode[26:], 2)
        return rTypeConversion(machinecode, opcode, funct)
    else:
        return eitherITypeORJType(machinecode, opcode)

def machine_to_mips(machine_code):
    mips_instruction = checkForOpcode(machine_code)
    return mips_instruction
