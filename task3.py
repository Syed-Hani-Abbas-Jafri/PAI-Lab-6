import numpy as np

print("TASK 3: Grayscale Image")

rng = np.random.default_rng(13)
image = rng.integers(0, 256, size=(6, 6))
threshold = 128

print("Grayscale image:\n", image)
print("Minimum intensity:", np.min(image))
print("Maximum intensity:", np.max(image))
print("Mean intensity:", np.mean(image))

pixel_mask = image > threshold
thresholded_image = np.where(pixel_mask, 255, 0)

print("Mask for pixels above", threshold, ":\n", pixel_mask)
print("Thresholded image (255 = above threshold, 0 = otherwise):\n",
      thresholded_image)
