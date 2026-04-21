from collections import defaultdict

n = int(input("Enter number of productions: "))
productions = []

print("Enter productions (use = and |, e.g., E=TR|a):")
for _ in range(n):
    productions.append(input().strip())

grammar = defaultdict(list)

for prod in productions:
    lhs, rhs = prod.split("=")
    for alt in rhs.split("|"):
        grammar[lhs].append(alt)

first = defaultdict(set)
follow = defaultdict(set)

def find_first(symbol):
    if not symbol.isupper():  # terminal
        return {symbol}

    result = set()
    for prod in grammar[symbol]:
        if prod == "$":  # epsilon
            result.add("$")
        else:
            for char in prod:
                temp = find_first(char)
                result.update(temp - {"$"})
                if "$" not in temp:
                    break
            else:
                result.add("$")
    return result

def find_follow(symbol):
    if symbol == start_symbol:
        follow[symbol].add("$")

    for lhs in grammar:
        for prod in grammar[lhs]:
            for i in range(len(prod)):
                if prod[i] == symbol:
                    # case 1: symbol followed by something
                    if i + 1 < len(prod):
                        next_sym = prod[i + 1]
                        first_next = find_first(next_sym)
                        follow[symbol].update(first_next - {"$"})
                        if "$" in first_next:
                            follow[symbol].update(find_follow(lhs))
                    else:
                        # case 2: symbol at end
                        if lhs != symbol:
                            follow[symbol].update(find_follow(lhs))
    return follow[symbol]

for non_terminal in grammar:
    first[non_terminal] = find_first(non_terminal)

# Start symbol
start_symbol = list(grammar.keys())[0]

# Compute FOLLOW sets
for non_terminal in grammar:
    find_follow(non_terminal)

# Output
print("\nFIRST sets:")
for nt in grammar:
    print(f"FIRST({nt}) = {{ {', '.join(first[nt])} }}")

print("\nFOLLOW sets:")
for nt in grammar:
    print(f"FOLLOW({nt}) = {{ {', '.join(follow[nt])} }}")