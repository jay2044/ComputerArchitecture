from mips_to_machine import assemble_mips_instruction
from control import control


def program_counter(address):
    printf('Address: {address}\n program passed the pc')


def regdst_mux(control_signals, instruction):
    print("MUX 1 RegDst:")

    if control_signals['RegDst'] == 1:
        write_register = instruction[16:21]
    elif control_signals['RegDst'] == 0:
        write_register = instruction[11:16]
    else:
        write_register = None

    return write_register


def register_file(read_register1, read_register2, write_register, control_signals):
    print("Register File:")
    read_data1 = "Value from " + read_register1
    print(f"{read_data1} passed to ALU")

    if control_signals["ALUSrc"] == 0:
        read_data2 = "Value from " + read_register2
        print(f"{read_data2} passed to ALU")
        alu(read_data1, read_data2, control_signals)


def alu(read_data1, read_data2, control_signals):
    print("ALU:")
    print(f"ALU performs operation with ALUOp: {control_signals['ALUOp']}")


def pc_adder():
    pass


def instruction_memory(instruction):
    print("Entered Instruction Memory")
    # Convert the instruction to machine code (not what an IM does)
    machine_code = assemble_mips_instruction(instruction)
    return machine_code


def main(instruction):
    print("Starting the visualizer")

    # Also returns the instruction as machine code
    machine_code = instruction_memory(instruction)
    print(f"machine_code = {machine_code}")

    opcode = machine_code[0:6]
    control_signals = control(opcode)

    write_register = regdst_mux(control_signals, machine_code)
    print(f"write_register = {write_register}")

    register_file(machine_code[7:11], machine_code[12:16], write_register, control_signals)


main("add, t1, t2, t3")
