import math
def is_terminal(state):
    return len(state["children"]) == 0
def utility(state):
    return state["value"]
def actions(state):
    return state["children"]
def result(state, action):
    return action

def minmax(state, depth, maximizing_player):
    if is_terminal(state) or depth == 0:
        return utility(state)
    if maximizing_player:
        max_eval = -math.inf
        for action in actions(state):
            eval = minmax(result(state, action), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for action in actions(state):
            eval = minmax(result(state, action), depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def build_tree(values):
    nodes = [{"value": v, "children": []} for v in values]
    while len(nodes) > 1:
        temp = []
        for i in range(0, len(nodes), 2):
            parent = {
                "value": None,
                "children": [nodes[i], nodes[i + 1]]
            }
            temp.append(parent)
        nodes = temp
    return nodes[0]  # root

if __name__ == "__main__":
    n = int(input("Enter number of leaf nodes (power of 2): "))
    values = list(map(int, input("Enter leaf node values: ").split()))
    if len(values) != n:
        print("Error: Number of values must match n")
        exit()
    root = build_tree(values)
    depth = int(math.log2(n))
    result_value = minmax(root, depth, True)
    print("Optimal value:", result_value)

Enter number of leaf nodes (power of 2): 4
Enter leaf node values: 3 5 2 9
Optimal value: 3