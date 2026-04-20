# Bayesian Network Example (Manual Probability Calculation)
# Probabilities
P_Cloudy = 0.5
P_Sprinkler_given_Cloudy = {
    True: 0.1,
    False: 0.5
}
P_Rain_given_Cloudy = {
    True: 0.8,
    False: 0.2
}
P_WetGrass_given_RS = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.90,
    (False, False): 0.0
}

def compute_probability():
    # Example: Compute P(WetGrass = True)
    total_prob = 0
    for cloudy in [True, False]:
        P_c = P_Cloudy if cloudy else (1 - P_Cloudy)
        for sprinkler in [True, False]:
            P_s = P_Sprinkler_given_Cloudy[cloudy] if sprinkler else (1 - P_Sprinkler_given_Cloudy[cloudy])
            for rain in [True, False]:
                P_r = P_Rain_given_Cloudy[cloudy] if rain else (1 - P_Rain_given_Cloudy[cloudy])
                P_w = P_WetGrass_given_RS[(sprinkler, rain)]
                total_prob += P_c * P_s * P_r * P_w
    return total_prob
# Run
result = compute_probability()
print("Probability of Wet Grass:", result)