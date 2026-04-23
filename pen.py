import cv2
import os
# Step 1: Read image
image = cv2.imread('input.jpg')

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Invert grayscale
inverted = 255 - gray

# Step 4: Blur the inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Step 5: Invert blurred image
inverted_blur = 255 - blur

# Step 6: Create pencil sketch (divide)
sketch = cv2.divide(gray, inverted_blur, scale=256)

# Save result
cv2.imwrite('sketch.png', sketch)
