# Two Pass Assembler (Corrected)

OPTAB = {
    "MOVER": "01",
    "ADD": "02",
    "SUB": "03",
    "MOVEM": "04",
    "JMP": "05"
}

REGISTERS = {
    "AREG": "1",
    "BREG": "2",
    "CREG": "3"
}

symbol_table = {}
intermediate_code = []
machine_code = []


def pass1(lines):
    lc = 0

    for line in lines:
        # Remove commas and split
        parts = line.strip().replace(",", "").split()

        if not parts:
            continue

        # START directive
        if parts[0] == "START":
            lc = int(parts[1])
            intermediate_code.append(("AD", "START", lc))
            continue

        # END directive
        if parts[0] == "END":
            intermediate_code.append(("AD", "END", None))
            continue

        # Check if first word is opcode or label
        if parts[0] in OPTAB:
            # No label
            opcode = parts[0]
            operands = parts[1:]
        else:
            # Label present
            label = parts[0]
            symbol_table[label] = lc
            opcode = parts[1]
            operands = parts[2:]

        operand_str = ",".join(operands) if operands else None

        # Add to intermediate code
        if opcode in OPTAB:
            intermediate_code.append(("IS", opcode, operand_str))
            lc += 1

    # Display Pass 1 Output
    print("\n--- PASS 1 OUTPUT ---")
    print("Intermediate Code:")
    for ic in intermediate_code:
        print(ic)

    print("\nSymbol Table:")
    for sym, addr in symbol_table.items():
        print(sym, ":", addr)


def pass2():
    for entry in intermediate_code:
        type_, opcode, operand = entry

        # Skip assembler directives
        if type_ == "AD":
            continue

        if type_ == "IS":
            op = OPTAB[opcode]

            reg = "0"
            addr = "000"

            if operand:
                parts = [p.strip() for p in operand.split(",")]

                if len(parts) == 2:
                    reg = REGISTERS.get(parts[0], "0")
                    sym = parts[1]
                else:
                    sym = parts[0]

                addr = str(symbol_table.get(sym, 0)).zfill(3)

            machine_code.append((op, reg, addr))

    # Display Pass 2 Output
    print("\n--- PASS 2 OUTPUT ---")
    print("Machine Code:")
    for code in machine_code:
        print(" ".join(code))


# Sample Assembly Program
program = [
    "START 100",
    "MOVER AREG, A",
    "ADD BREG, B",
    "A MOVEM AREG, B",
    "END"
]

# Run assembler
pass1(program)
pass2()