import numpy as np

print("TASK 6: Random Measurements")

for seed in (21, 32):
    rng = np.random.default_rng(seed)
    measurements = rng.normal(loc=100, scale=15, size=1000)

    average = np.mean(measurements)
    standard_deviation = np.std(measurements)
    lower_limit = average - standard_deviation
    upper_limit = average + standard_deviation
    within_one_std = (measurements >= lower_limit) & (measurements <= upper_limit)
    percentage = np.mean(within_one_std) * 100

    print("\nSeed:", seed)
    print("Mean:", np.mean(measurements))
    print("Median:", np.median(measurements))
    print("Standard deviation:", standard_deviation)
    print("Minimum:", np.min(measurements))
    print("Maximum:", np.max(measurements))
    print("Percentage within one standard deviation:", percentage)

print("The seeds produce different samples, so their statistics will differ.")
