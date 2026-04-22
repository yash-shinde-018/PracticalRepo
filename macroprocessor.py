# Single Pass Macro Processor

MNT = {}   # Macro Name Table
MDT = []   # Macro Definition Table


def macro_processor(lines):
    i = 0
    output = []

    while i < len(lines):
        line = lines[i].strip()

        # MACRO definition
        if line == "MACRO":
            i += 1
            header = lines[i].strip().split()

            macro_name = header[0]
            params = header[1:]

            # Store in MNT
            MNT[macro_name] = {
                "mdt_index": len(MDT),
                "params": params
            }

            i += 1

            # Store body in MDT
            while lines[i].strip() != "MEND":
                MDT.append(lines[i].strip())
                i += 1

            MDT.append("MEND")

        else:
            parts = line.split()

            # Macro call
            if parts and parts[0] in MNT:
                macro_name = parts[0]
                actual_args = parts[1:]

                mdt_index = MNT[macro_name]["mdt_index"]
                formal_params = MNT[macro_name]["params"]

                # Argument mapping
                arg_map = {
                    formal_params[j]: actual_args[j]
                    for j in range(len(formal_params))
                }

                # Expand macro
                k = mdt_index
                while MDT[k] != "MEND":
                    expanded_line = MDT[k]

                    for param in arg_map:
                        expanded_line = expanded_line.replace(param, arg_map[param])

                    output.append(expanded_line)
                    k += 1

            else:
                # Normal line
                output.append(line)

        i += 1

    return output


# Sample Input
program = [
    "MACRO",
    "INCR &A &B",
    "LDA &A",
    "ADD &B",
    "STA &A",
    "MEND",
    "START",
    "INCR X Y",
    "END"
]

# Run macro processor
expanded_code = macro_processor(program)

# -------- PRINTING SECTION -------- #

print("\n--- MNT (Macro Name Table) ---")
for name, val in MNT.items():
    print(f"{name} -> MDT Index: {val['mdt_index']}, Parameters: {val['params']}")

print("\n--- MDT (Macro Definition Table) ---")
for i, line in enumerate(MDT):
    print(f"{i} -> {line}")

print("\n--- EXPANDED CODE ---")
for line in expanded_code:
    print(line)