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
            print(f"{machine.opcode.zfill(6)} {rs} {rt} {rd} {shamt} {machine.funct.zfill(6)}")

        else:
            rs = bin(named_registers[instruction[2]])[2:].zfill(5)
            rt = bin(named_registers[instruction[3]])[2:].zfill(5)
            rd = bin(named_registers[instruction[1]])[2:].zfill(5)
            shamt = '00000'
            machine = r_type_instruction(mnemonic, rs, rt, rd, shamt)
            print(f"{machine.opcode.zfill(6)} {rs} {rt} {rd} {shamt} {machine.funct.zfill(6)}")

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
        print(f"{machine.opcode.zfill(6)} {rs} {rt} {immediate}")

    elif instruction_type == 'jtype':
        address = bin(int(instruction[1], 16))[2:].zfill(26)
        machine = j_type_instruction(mnemonic, address)
        print(f"{machine.opcode.zfill(6)} {machine.address}")


mips_to_machine("j 0x3c")


# Test examples:
'''
Instruction: add $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100000

Instruction: sub $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100010

Instruction: and $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100100

Instruction: or $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100101

Instruction: slt $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 101010

Instruction: sll $t1, $t2, 2
Machine Code: 000000 00000 01010 01001 00010 000000

Instruction: sw $t1, 32($t2)
Machine Code: 101011 01010 01001 00000 00000 100000

Instruction: lw $t1, 32($t2)
Machine Code: 100011 01010 01001 00000 00000 100000

Instruction: beq $t1, $t2, label
Machine Code: 000100 01001 01010 label offset

Instruction: j target
Machine Code: 000010 target address

Instruction: jr $t1
Machine Code: 000000 01001 00000 00000 00000 001000

Instruction: jal target
Machine Code: 000011 target address

Instruction: nor $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100111

Instruction: xor $t1, $t2, $t3
Machine Code: 000000 01010 01011 01001 00000 100110

Instruction: srl $t1, $t2, 2
Machine Code: 000000 00000 01010 01001 00010 000010

Instruction: sra $t1, $t2, 2
Machine Code: 000000 00000 01010 01001 00010 000011

Instruction: lui $t1, imm
Machine Code: 001111 00000 01001 immediate

Instruction: bne $t1, $t2, label
Machine Code: 000101 01001 01010 label offset

Instruction: addi $t1, $t2, 10
Machine Code: 001000 01010 01001 0000 0000 0000 1010

Instruction: slti $t1, $t2, -5
Machine Code: 001010 01010 01001 1111 1111 1111 1011

Instruction: andi $t1, $t2, 15
Machine Code: 001100 01010 01001 0000 0000 0000 1111

Instruction: ori $t1, $t2, 255
Machine Code: 001101 01010 01001 0000 0000 1111 1111

Instruction: xori $t1, $t2, 16
Machine Code: 001110 01010 01001 0000 0000 0001 0000

Instruction: lb $t1, 100($t2)
Machine Code: 100000 01010 01001 0000 0110 0100 0000

Instruction: sb $t1, 100($t2)
Machine Code: 101000 01010 01001 0000 0110 0100 0000

Instruction: lh $t1, 2($t2)
Machine Code: 100001 01010 01001 0000 0000 0000 0010

Instruction: sh $t1, 2($t2)
Machine Code: 101001 01010 01001 0000 0000 0000 0010

Instruction: bgtz $t1, 8
Machine Code: 000111 01001 00000 0000 0000 0000 1000

Instruction: blez $t1, -4
Machine Code: 000110 01001 00000 1111 1111 1111 1100

Instruction: lui $t1, 1024
Machine Code: 001111 00000 01001 0000 0100 0000 0000
'''

