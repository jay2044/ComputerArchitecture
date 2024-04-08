import instructionType

# testing variable 
string = "00110101010010010000000000100101"

# r type conversion
def rTypeConversion(machineCode, opcode, funct):
    for name, value in instructionType.instruction_dictionary.items():
        if funct != -1 and funct == int(value[1],16):
            rs = instructionType.getRegisterName(int(machineCode[6:11],2))
            rt = instructionType.getRegisterName(int(machineCode[11:16],2))
            rd = instructionType.getRegisterName(int(machineCode[16:21],2))
            shamt = int(machineCode[21:26],2)
            
            instruction = instructionType.rTypeInstruction(opcode,rs,rt,rd,shamt,funct)
            print(f"{name} {rs} {rt} {rd}")
            break

# i type and jtype conversion
def eitherITypeORJType(machineCode, opcode):
    for name, value in instructionType.instruction_dictionary.items():
        if isinstance(value, str) and opcode == int(value,16):
            type = instructionType.typeOfInstruction(name)
            
            if type == 'itype':
                rs = instructionType.getRegisterName(int(machineCode[6:11],2))
                rt = instructionType.getRegisterName(int(machineCode[11:16],2))
                immediate = int(machineCode[16:],2)
                instruction = instructionType.iTypeInstruction(opcode,rs,rt,immediate)
                print(f"{name} {rt} {rs} {immediate}")
                break
            else:
                address = int(machineCode[5:],2)
                instruction = instructionType.jTypeInstruction(opcode, address)
                print(f"{name} {hex(address)}")
                break

# USE THIS FUNCTION TO USE THE FILE
def checkForOpcode(machinecode):
    opcode = int(machinecode[0:6],2)
    funct = -1
    if opcode == 0:
        funct = int(machinecode[26:],2)
        rTypeConversion(machinecode, opcode, funct)
    else:
        eitherITypeORJType(machinecode, opcode)

checkForOpcode(string)