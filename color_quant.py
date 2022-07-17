import numpy as np
from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

img = plt.imread("Capture.jpg")

img = np.array(img, dtype = np.float64) / 255

w, h, d, = original_shape = tuple(img.shape)
assert d == 3
imgarr = np.reshape(img, (w*h,d))

kmeans = KMeans(n_clusters=16).fit(imgarr)

labels = kmeans.predict(imgarr)




plt.figure(1)
plt.clf()
plt.axis("off")
plt.title("Original image (96,615 colors)")
plt.imshow(img)

plt.figure(2)
plt.clf()
plt.axis("off")
plt.title(f"Quantized image ({16} colors, K-Means)")
plt.imshow(kmeans.cluster_centers_[labels].reshape(w, h, -1))
