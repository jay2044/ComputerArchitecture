import instructionType

def assemble_mips_instruction(instruction):
    instruction = instruction.replace('$', '')
    instruction = instruction.replace(',', '').split()
    mnemonic = instruction[0]
    instructionType = typeOfInstruction(mnemonic)
    if instructionType == 'rtype':
        if mnemonic in ['sll', 'srl']:
            rs = '00000'
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            if len(instruction) == 4:
                shamt = bin(int(instruction[3]))[2:].zfill(5)
            else:
                shamt = '00000'
            machine = rTypeInstruction(mnemonic, rs, rt, rd, shamt)
            print(f"{machine.opcode.zfill(6)} {rs} {rt} {rd} {shamt} {machine.funct.zfill(6)}")

        else:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[3]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = rTypeInstruction(mnemonic, rs, rt, rd, shamt)
            print(f"{machine.opcode.zfill(6)} {rs} {rt} {rd} {shamt} {machine.funct.zfill(6)}")

    elif instructionType == 'itype':
        if mnemonic in ['lw', 'sw']:
            # Splitting the offset(base) part for lw and sw instructions
            offset, base = instruction[2].split('(')
            base = base[:-1]  # Remove the closing parenthesis
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = bin(named_registers[base])[2:].zfill(5)
            immediate = bin(int(offset, 0))[2:].zfill(16)
        else:
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            immediate = bin(int(instruction[3], 0))[2:].zfill(16)
        machine = iTypeInstruction(mnemonic, rs, rt, immediate)
        print(f"{machine.opcode.zfill(6)} {rs} {rt} {immediate}")

    elif instructionType == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = jTypeInstruction(mnemonic, address)
        print(f"{machine.opcode.zfill(6)} {machine.address}")


assemble_mips_instruction("lui $t1, 1024")