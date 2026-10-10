import numpy as np

rng = np.random.default_rng(14)
readings = rng.normal(25, 5, size=(4, 8))
threshold = 30

print("Sensor readings (rows are sensors, columns are time points):\n", readings)
print("Mean for each sensor:", np.mean(readings, axis=1))
print("Minimum for each sensor:", np.min(readings, axis=1))
print("Maximum for each sensor:", np.max(readings, axis=1))
print("Standard deviation for each sensor:", np.std(readings, axis=1))

sensor_averages = np.mean(readings, axis=1)
best_sensor = np.argmax(sensor_averages)
print("Sensor with highest average:", best_sensor + 1)

above_threshold = readings > threshold
print("Mask for readings above", threshold, ":\n", above_threshold)
print("Readings above threshold:", readings[above_threshold])
print("Sensor/time positions (zero-based):\n", np.argwhere(above_threshold))
