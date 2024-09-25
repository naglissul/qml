from spectral import *
import matplotlib.pyplot as plt

# Load the image
img = open_image('./data/92AV3C.lan')

# Display the image
view = imshow(img, (29, 19, 9))

# Show the image
plt.show()
