import numpy as np
import matplotlib.pyplot as plt

# mean = 0  and sigma = 1

# Define parameters for the normal distribution
mu = 0       # Mean
sigma = 1    # Standard deviation

# Sample from the normal distribution
for n_samples in [10, 20, 50, 100, 1000, 5000, 10000]:
    samples = np.random.standard_cauchy(size=n_samples) # sample from the distribution
    average = np.mean(samples)
    
    print(f"Average of {n_samples} = {average}")