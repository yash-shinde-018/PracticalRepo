# Two Pass Assembler (Simplified)

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
        parts = line.strip().split()

        if not parts:
            continue

        # Handle START
        if parts[0] == "START":
            lc = int(parts[1])
            intermediate_code.append(("AD", "START", lc))
            continue

        # Label present
        if len(parts) == 3:
            label, opcode, operand = parts
            symbol_table[label] = lc
        else:
            label = None
            opcode = parts[0]
            operand = parts[1] if len(parts) > 1 else None

        if opcode in OPTAB:
            intermediate_code.append(("IS", opcode, operand))
            lc += 1

        elif opcode == "END":
            intermediate_code.append(("AD", "END", None))

    print("\n--- PASS 1 OUTPUT ---")
    print("Intermediate Code:")
    for ic in intermediate_code:
        print(ic)

    print("\nSymbol Table:")
    for sym, addr in symbol_table.items():
        print(sym, ":", addr)


def pass2():
    lc = 0

    for entry in intermediate_code:
        type_, opcode, operand = entry

        if type_ == "AD":
            continue

        if type_ == "IS":
            op = OPTAB[opcode]

            reg = "0"
            addr = "000"

            if operand:
                parts = operand.split(",")

                if len(parts) == 2:
                    reg = REGISTERS.get(parts[0], "0")
                    sym = parts[1]
                else:
                    sym = parts[0]

                addr = str(symbol_table.get(sym, 0)).zfill(3)

            machine_code.append((op, reg, addr))

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