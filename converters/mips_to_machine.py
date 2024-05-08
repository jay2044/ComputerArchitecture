import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))

from mips_instructions import *


def mips_to_machine(instruction):
    instruction = instruction.replace('$', '')
    instruction = instruction.replace(',', '').split()
    mnemonic = instruction[0]
    instruction_type = type_of_instruction(mnemonic)

    if instruction_type == 'rtype':
        if mnemonic in ['sll', 'srl']:
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rs = '00000'
            if len(instruction) == 4:
                shamt = bin(int(instruction[3]))[2:].zfill(5)
            else:
                shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["add", "addu", "and", "slt", "sltu", "sub", "subu", "nor", "or"]:
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[3]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"
        
        if mnemonic in ["div", "divu", "mult", "multu", "sra"]:
            rd = '00000'
            rs = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["mfhi", "mflo"]:
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = '00000'
            rt = '00000'
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"
        
        if mnemonic in ["mfc0"]:
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = '00000'
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["sra"]:
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rs = '00000'
            shamt = bin(named_registers[instruction[3]])[2:].zfill(5)
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"
        
        if mnemonic in ["jr"]:
            rs = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = '00000'
            rd = '00000'
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
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"

        if mnemonic in ["addi", "addiu", "andi", "lbu", "lhu", "ll", "lw", "slti", "sltiu", "ori"]:
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            immediate = bin(int(instruction[3], 0))[2:].zfill(16) # this is wrong for 2's comp for slti -10
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"
        
        if mnemonic in ["sb", "sc", "sh", "sw", "bne","beq"]:
            rs = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            immediate = bin(int(instruction[3], 0))[2:].zfill(16)

            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"
        
        if mnemonic in ["lui"]:
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            immediate = bin(int(instruction[3], 0))[2:].zfill(16)

            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"

    elif instruction_type == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = j_type_instruction(mnemonic, address)
        return f"{machine.opcode.zfill(6)}{machine.address}"
