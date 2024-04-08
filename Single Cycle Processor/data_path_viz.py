from converters.mips_to_machine import assemble_mips_instruction
from control import control

current_pc = 0


def program_counter(next_address=None):
    global current_pc
    if next_address is not None:
        current_pc = next_address
    else:
        current_pc += 4
    print(f'Address: {current_pc}\nProgram passed the PC')


def regdst_mux(control_signals, instruction):
    print(f"MUX 1 RegDst: {control_signals['RegDst']}")

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
    global current_pc
    return current_pc + 4


def instruction_memory(instruction):
    print("Entered Instruction Memory")
    # Convert the instruction to machine code (not what an IM does)
    machine_code = assemble_mips_instruction(instruction)
    return machine_code


def data_memory(address, write_data=None, mem_write=False, mem_read=False):
    print("Data Memory Access:")
    if mem_read:
        print(f"Reading data from address {address}")
        read_data = "data"
        return read_data
    if mem_write:
        print(f"Writing {write_data} to address {address}")


def sign_extend(immediate):
    if immediate[0] == '1':
        extended = '1111111111111111' + immediate
    else:
        extended = '0000000000000000' + immediate
    print(f"Sign-Extended Immediate: {extended}")
    return extended


def start_data_path_visualizer(instruction):
    print("Starting the visualizer")

    # Also returns the instruction as machine code
    machine_code = instruction_memory(instruction)
    print(f"machine_code = {machine_code}")

    opcode = machine_code[0:6]
    control_signals = control(opcode)

    write_register = regdst_mux(control_signals, machine_code)
    print(f"write_register = {write_register}")

    register_file(machine_code[7:11], machine_code[12:16], write_register, control_signals)


start_data_path_visualizer("add, t1, t2, t3")

