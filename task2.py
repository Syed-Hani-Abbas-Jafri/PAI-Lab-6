import numpy as np

rng = np.random.default_rng(12)
features = rng.normal(50, 10, size=(10, 4))
print("Original feature matrix:\n", features)

feature_means = np.mean(features, axis=0)
feature_stds = np.std(features, axis=0)
standardized_features = (features - feature_means) / feature_stds

print("Mean of each original feature:", feature_means)
print("Standard deviation of each original feature:", feature_stds)
print("Standardized matrix:\n", standardized_features)
print("Means after standardization (should be close to 0):",
      np.mean(standardized_features, axis=0))
print("Standard deviations after standardization (should be close to 1):",
      np.std(standardized_features, axis=0))

print("Means close to 0:", np.allclose(np.mean(standardized_features, axis=0), 0))
print("Standard deviations close to 1:", np.allclose(np.std(standardized_features, axis=0), 1))

print("Broadcasting: feature_means and feature_stds each have shape (4,).")
print("NumPy applies these four values to every row of the (10, 4) matrix, so")
print("each feature column is standardized without using a loop.")
