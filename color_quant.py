# %%
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as image
from skimage import io

path = "screenshot.png"

img = io.imread(path)
original_shape = img.shape

img = np.array(img, dtype = np.float64) / 255


#calculating unique colors from original image
im = Image.open(path)
w, h = im.size
ucol = set()
for x in range(w):
    for y in range(h):
        pixel = im.getpixel((x, y))
        ucol.add(pixel)
 
sum_ucol = len(ucol)
print(sum_ucol)

n_colors = 64

imgr = np.reshape(img, (-1,3))

kmeans = KMeans(n_clusters=n_colors).fit(imgr)

labels = kmeans.predict(imgr)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.axis("off")
ax1.set_title(str(sum_ucol) + " colors)")
ax1.imshow(img)

k_img = kmeans.cluster_centers_[labels].reshape(h, w, -1)
ax2.axis("off")
ax2.set_title(f"({n_colors} colors, K-Means)")
ax2.imshow(k_img)

imgr = np.reshape(imgr, (original_shape))
image.imsave('test.png', k_img)


# %%
