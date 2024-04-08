def control(opcode):
    # Default control signals, assuming a 'do nothing' state
    control_signals = {
        "RegDst": 0,
        "ALUSrc": 0,
        "MemToReg": 0,
        "RegWrite": 0,
        "MemRead": 0,
        "MemWrite": 0,
        "Branch": 0,
        "ALUOp": "00"  # "00" for R-type, "10" for beq, others could be "01" for I-type etc.
    }

    if opcode == "000000":  # R-type instructions
        control_signals.update({
            "RegDst": 1,
            "RegWrite": 1,
            "ALUOp": "10",
        })
    elif opcode == "100011":  # lw
        control_signals.update({
            "ALUSrc": 1,
            "MemToReg": 1,
            "RegWrite": 1,
            "MemRead": 1,
            "ALUOp": "00",
        })
    elif opcode == "101011":  # sw
        control_signals.update({
            "ALUSrc": 1,
            "MemWrite": 1,
            "ALUOp": "00",
        })
    elif opcode == "000100":  # beq
        control_signals.update({
            "Branch": 1,
            "ALUOp": "01",
        })
    else:
        print("Unsupported opcode.")

    return control_signals
