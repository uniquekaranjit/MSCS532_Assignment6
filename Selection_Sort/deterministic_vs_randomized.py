import random
import time
import matplotlib.pyplot as plt

from Selection_Sort.deterministic_selection_algorithm import median_of_medians
from randomized_selection_algorithm import quickselect


# Function to generate different input distributions
def generate_input_data(size, distribution):
    if distribution == "random":
        return random.sample(range(size * 10), size)
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse_sorted":
        return list(range(size, 0, -1))

# Function to measure execution time of both algorithms
def measure_time(algorithm, arr, k):
    start_time = time.time()
    algorithm(arr, k)
    return time.time() - start_time

# Parameters
input_sizes = [100, 500, 1000, 5000, 10000]  # Different input sizes
distributions = ["random", "sorted", "reverse_sorted"]  # Different input distributions
k = 50  # The index to select (e.g., the 50th smallest element)

# Store execution times
results = {
    "random": {"quickselect": [], "median_of_medians": []},
    "sorted": {"quickselect": [], "median_of_medians": []},
    "reverse_sorted": {"quickselect": [], "median_of_medians": []}
}

# Measure execution times
for distribution in distributions:
    for size in input_sizes:
        arr = generate_input_data(size, distribution)
        
        # Measure Quickselect time
        qs_time = measure_time(quickselect, arr, k)
        results[distribution]["quickselect"].append(qs_time)
        
        # Measure Median of Medians time
        mom_time = measure_time(median_of_medians, arr, k)
        results[distribution]["median_of_medians"].append(mom_time)

# Plot results
plt.figure(figsize=(12, 8))

for i, distribution in enumerate(distributions, 1):
    plt.subplot(2, 2, i)
    plt.plot(input_sizes, results[distribution]["quickselect"], label="Randomized Quickselect", marker="o")
    plt.plot(input_sizes, results[distribution]["median_of_medians"], label="Deterministic Median of Medians", marker="x")
    
    plt.title(f"Runtime for {distribution.replace('_', ' ').capitalize()} Input")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
