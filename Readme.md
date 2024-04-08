
### General MIPS Data Path Components:

- **Program Counter (PC):** Holds the address of the current instruction.
- **Instruction Memory (IM):** Stores the program instructions.
- **Register File:** A set of registers that can be read or written to.
- **ALU (Arithmetic Logic Unit):** Performs arithmetic and logical operations.
- **Data Memory:** Stores and retrieves data.
- **Control Unit:** Generates control signals based on the instruction opcode.
- **Multiplexers (MUX):** Chooses between inputs based on control signals.

### Control Signals:

- **RegDst:** Chooses the register destination.
- **ALUSrc:** Chooses between register and immediate values for the ALU second operand.
- **MemToReg:** Selects between ALU result and memory data for writing back to the register.
- **RegWrite:** Enables writing to the register file.
- **MemRead:** Enables reading from data memory.
- **MemWrite:** Enables writing to data memory.
- **Branch:** Determines whether a branch should be taken.
- **ALUOp:** Determines the ALU operation based on the instruction type.

### R-type Instructions:

1. **IF:** Fetch the instruction from IM using PC.
2. **ID:**
   - Read registers specified in the instruction.
   - Control signals set: RegDst=1, ALUSrc=0, MemToReg=0, RegWrite=1, MemRead=0, MemWrite=0, Branch=0, ALUOp depends on the function field.
3. **EX:**
   - **ALU:** Performs operation specified by the function field on the two read register values.
   - **RegDst MUX:** Chooses the destination register based on the RegDst signal.
4. **MEM:** No operation, as R-type instructions do not involve data memory.
5. **WB:** Write the result of the ALU operation back to the register file using the destination register selected by the RegDst MUX.

### I-type Instructions:

1. **IF:** Instruction fetched from IM.
2. **ID:**
   - Read registers.
   - Control signals vary by specific instruction (e.g., load, store, immediate arithmetic).
   - **Sign-Extend:** The immediate field is sign-extended to 32 bits.
3. **EX:**
   - **ALUSrc MUX:** Selects between the second register and the sign-extended immediate value for the second ALU operand.
   - **ALU:** Executes operation (addition for loads, stores; specified operation for arithmetic).
4. **MEM:**
   - For load/store, access data memory.
   - Control signals set accordingly (MemRead for load, MemWrite for store).
5. **WB:**
   - **MemToReg MUX:** Chooses between ALU result and data memory value for loads.
   - Write result back to the register file.

### J-type Instructions (e.g., `j` and `jal`):

1. **IF:** Instruction fetched.
2. **ID:** No register reading. Control signals are mostly irrelevant, except for jumping-specific signals not detailed in basic control signal sets.
3. **EX:** Calculate jump target address.
4. **MEM:** No operation, as J-type instructions do not involve data memory.
5. **WB:** No traditional write-back phase, but for `jal`, the return address is written to a designated register.