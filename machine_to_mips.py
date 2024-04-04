import instructionType

# testing variable 
string = "00110101010010010000000000100101"


opcode = int(string[0:6],2)
funct = -1


# r type conversion

def rTypeConversion(opcode, funct):
    for name, value in instructionType.instruction_dictionary.items():
        if funct != -1 and funct == int(value[1],16):
            rs = instructionType.getRegisterName(int(string[6:11],2))
            rt = instructionType.getRegisterName(int(string[11:16],2))
            rd = instructionType.getRegisterName(int(string[16:21],2))
            shamt = int(string[21:26],2)
            
            instruction = instructionType.rTypeInstruction(opcode,rs,rt,rd,shamt,funct)
            print(f"{name} {rs} {rt} {rd}")
            break

# i type and jtype conversion
def eitherITypeORJType(opcode):
    for name, value in instructionType.instruction_dictionary.items():
        if isinstance(value, str) and opcode == int(value,16):
            type = instructionType.typeOfInstruction(name)
            if type == 'itype':
                rs = instructionType.getRegisterName(int(string[6:11],2))
                rt = instructionType.getRegisterName(int(string[11:16],2))
                immediate = int(string[16:],2)
                instruction = instructionType.iTypeInstruction(opcode,rs,rt,immediate)
                print(f"{name} {rt} {rs} {immediate}")
                break
            else:
                address = int(string[5:],2)
                instruction = instructionType.jTypeInstruction(opcode, address)
                print(f"{name} {hex(address)}")
                break


if opcode == 0:
    funct = int(string[26:],2)
    rTypeConversion(opcode, funct)
else:
    eitherITypeORJType(opcode)