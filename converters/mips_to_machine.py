from mips_instructions import *


def mips_to_machine(instruction):
    instruction = instruction.replace('$', '')
    instruction = instruction.replace(',', '').split()
    mnemonic = instruction[0]
    instruction_type = type_of_instruction(mnemonic)
    if instruction_type == 'rtype':
        if mnemonic in ['sll', 'srl']:
            rs = '00000'
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            if len(instruction) == 4:
                shamt = bin(int(instruction[3]))[2:].zfill(5)
            else:
                shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        else:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[3]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

    elif instruction_type == 'itype':
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
        machine = i_type_instruction(mnemonic, rs, rt, immediate)
        return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"

    elif instruction_type == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = j_type_instruction(mnemonic, address)
        return f"{machine.opcode.zfill(6)}{machine.address}"
