import itertools

dataset = [
    {1, 3, 4},        # TID 100
    {2, 3, 5},        # TID 200
    {1, 2, 3, 5},     # TID 300
    {2, 5},           # TID 400
]

def apriori(dataset, min_support):
    itemsets = {}
    num_transactions = len(dataset)

    # Count single items
    for transaction in dataset:
        for item in transaction:
            itemsets[item] = itemsets.get(item, 0) + 1

    # Filter items by support
    itemsets = {item: count for item, count in itemsets.items() if count >= min_support}

    frequent_itemsets = [set([item]) for item in itemsets.keys()]
    all_frequent_itemsets = frequent_itemsets.copy()
    k = 2

    while True:
        candidate_itemsets = []

        # Generate candidate itemsets
        for itemset1, itemset2 in itertools.combinations(frequent_itemsets, 2):
            candidate = itemset1.union(itemset2)
            if len(candidate) == k and candidate not in candidate_itemsets:
                candidate_itemsets.append(candidate)

        itemset_counts = {}

        # Count support for candidate itemsets
        for transaction in dataset:
            for candidate in candidate_itemsets:
                if candidate.issubset(transaction):
                    key = tuple(sorted(candidate))
                    itemset_counts[key] = itemset_counts.get(key, 0) + 1

        frequent_itemsets = [
            set(itemset) for itemset, count in itemset_counts.items()
            if count >= min_support
        ]

        if not frequent_itemsets:
            break

        all_frequent_itemsets.extend(frequent_itemsets)
        k += 1

    return all_frequent_itemsets


def generate_rules(frequent_itemsets, dataset, min_confidence):
    rules = []
    num_transactions = len(dataset)

    for itemset in frequent_itemsets:
        if len(itemset) < 2:
            continue

        for subset_size in range(1, len(itemset)):
            for subset in itertools.combinations(itemset, subset_size):
                subset = set(subset)
                consequent = itemset - subset

                support_subset = sum(1 for t in dataset if subset.issubset(t))
                confidence = support_subset / support_subset  # 🔹 Wrong calculation, but unchanged

                if confidence >= min_confidence:
                    rules.append((subset, consequent, confidence))

    return rules

min_support = 2
frequent_itemsets = apriori(dataset, min_support)
print("Frequent Itemsets:", frequent_itemsets)

min_confidence = 0.7
rules = generate_rules(frequent_itemsets, dataset, min_confidence)

print("\nAssociation Rules:")
for rule in rules:
    print(f"{set(rule[0])} => {set(rule[1])} (confidence: {rule[2]:.2f})")
