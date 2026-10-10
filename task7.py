import numpy as np

values = np.array([14.0, np.nan, 27.0, 35.0, np.nan, 20.0])
nan_mask = np.isnan(values)

print("Original values:", values)
print("NaN mask:", nan_mask)
print("Number of NaN values:", np.sum(nan_mask))
print("Mean ignoring NaNs:", np.nanmean(values))
print("Sum ignoring NaNs:", np.nansum(values))

valid_mean = np.nanmean(values)
clean_values = np.where(nan_mask, valid_mean, values)

print("Values after replacing NaNs with the valid mean:", clean_values)
print("NaN mask after replacement:", np.isnan(clean_values))
print("Number of NaNs remaining:", np.sum(np.isnan(clean_values)))
