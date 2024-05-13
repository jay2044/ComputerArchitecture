
### Calculator Heaven

This repo has all the tools and calculators you need to aikido that stupid class.

- **main.py**: The main script providing a user interface to convert between MIPS instructions and machine code.
- **mips_instructions.py**: Defines classes and functions for MIPS instructions, including RType, IType, and JType, and provides utilities for constructing instructions and determining their types.
- **converters**: Various conversion utilities and tools.
    - **machine_to_mips.py**: Provides functions for converting machine code to MIPS instructions. 
    - **mips_to_hex.py**: Contains utilities for converting MIPS instructions to hexadecimal format. 
    - **mips_to_machine.py**: Defines functions for converting MIPS instructions to machine code.
- **binaryArith.py**: Implements functions for performing binary arithmetic operations, including addition, subtraction, multiplication, and division, with support for signed and unsigned binary numbers.
- **Single Cycle Processor**: Contains files related to the implementation of a single-cycle processor.
  - **control.py**: Defines the control unit for the single-cycle processor, generating control signals based on the opcode of instructions.
  - **data_path_viz.py**: Visualizes the data path of the single-cycle processor, illustrating how data moves through the processor during instruction execution.
- **Unit Testing**: Unit tests to ensure the correctness of various functions and modules.
- **testFormatting.py**: Tests for binary multiplication and other formatting-related operations.
- **Cache**: Contains caching mechanisms and related files.
  - **direct_mapped.py**: Implements a direct-mapped cache, simulating cache operations and evaluating performance metrics.
  - **set_associative.py**: Implements a set-associative cache, allowing for multiple blocks per set and providing functions to simulate and analyze cache behavior.