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
            rs = '00000'
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = bin(int(instruction[3]))[2:].zfill(5)
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["add", "addu", "and", "slt", "sltu", "sub", "subu", "nor", "or"]:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[3]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"
        
        if mnemonic in ["div", "divu", "mult", "multu"]:
            rs = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rd = '00000'
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["mfhi", "mflo"]:
            rs = '00000'
            rt = '00000'
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"
        
        if mnemonic in ["mfc0"]:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = '00000'
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{rd}{shamt}{machine.funct.zfill(6)}"

        if mnemonic in ["sra"]:
            rs = '00000'
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = bin(int(instruction[3]))[2:].zfill(5)
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
        if mnemonic in ['lw', 'lbu', 'lhu', 'll', 'sw', 'sb', 'sc', 'sh']:
            # Splitting the offset(base) part for lw and sw instructions
            offset, base = instruction[2].split('(')
            base = base[:-1]  # Remove the closing parenthesis
            rs = bin(named_registers[base])[2:].zfill(5)
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            immediate = bin(int(offset, 0))[2:].zfill(16)
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"

        if mnemonic in ["addi", "addiu", "andi", "slti", "sltiu", "ori"]:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            immediate = int(instruction[3], 0)
            immediate = bin(immediate & 0xFFFF)[2:].zfill(16) # needs this so this can work with negative numbers.
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"
        
        if mnemonic in ["bne","beq"]:
            rs = bin(named_registers[instruction[1]])[2:].zfill(5)
            rt = bin(named_registers[instruction[2]])[2:].zfill(5)
            immediate = bin(int(instruction[3], 0))[2:].zfill(16)
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"
        
        if mnemonic in ["lui"]:
            rs = '00000'
            rt = bin(named_registers[instruction[1]])[2:].zfill(5)
            immediate = int(instruction[2], 0)
            immediate = bin(immediate & 0xFFFF)[2:].zfill(16) # needs this so this can work with negative numbers.
            machine = i_type_instruction(mnemonic, rs, rt, immediate)
            return f"{machine.opcode.zfill(6)}{rs}{rt}{immediate}"

    elif instruction_type == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = j_type_instruction(mnemonic, address)
        return f"{machine.opcode.zfill(6)}{machine.address}"
