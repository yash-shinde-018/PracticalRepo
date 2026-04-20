import random
def fitness(x):
    return x * x   # Example: maximize x^2

def initialize_population(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]

def evaluate_population(population):
    return [fitness(ind) for ind in population]

def select_parents(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) > fitness(b) else b   # Tournament selection

def crossover(p1, p2):
    return (p1 + p2) // 2   # Simple average crossover

def mutate(child, mutation_rate, lower, upper):
    if random.random() < mutation_rate:
        return random.randint(lower, upper)
    return child

def genetic_algorithm():
    pop_size = int(input("Enter population size: "))
    generations = int(input("Enter number of generations: "))
    mutation_rate = float(input("Enter mutation rate (0-1): "))
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    population = initialize_population(pop_size, lower, upper)
    for generation in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, lower, upper)
            new_population.append(child)
        population = new_population
        best = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best = {best}, Fitness = {fitness(best)}")
    best_solution = max(population, key=fitness)
    print("\nBest Solution:", best_solution)
    print("Best Fitness:", fitness(best_solution))

genetic_algorithm()

Enter population size: 5
Enter number of generations: 4
Enter mutation rate (0-1): 0.3
Enter lower bound: 1
Enter upper bound: 10
