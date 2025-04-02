import cv2

# Load the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
# Pixels >127 become 255 (white), else 0 (black)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Save or display the result
cv2.imwrite("output_binary.jpg", binary_image)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
