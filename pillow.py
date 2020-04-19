from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("/Users/kataokakenta/Desktop/大原優乃/e2a63ece-347a-4332-bc39-4d8779ba9984.jpeg")
gray_image = image.convert("L")
color_image = np.array(image)
hist_c, bins_c = np.histogram(color_image[:,:,2].flatten(), bins=256)
# plt.plot(hist_c)
color_pil = Image.fromarray(np.uint8(color_image))
# plt.imshow(color_pil)
half_image = color_image // 2
plt.imshow(half_image)
# print(type(image))
# plt.imshow(image)
# plt.imshow(gray_image, cmap="gray")
plt.show()
# print(color_image.shape)

