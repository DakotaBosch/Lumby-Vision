#import mss
import cv2
import numpy as np
import time
import mss
from pydarknet import Detector, Image

def detect(im):
	net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("backup/yolov3-tiny_final.weights", encoding="utf-8"), 0, bytes("custom/lumby.data",encoding="utf-8"))

	temp = cv2.imread(im)

	img = Image(temp)

	results = net.detect(img)

	return results

with mss.mss() as sct:
	while True:
		im = sct.grab()
		img = Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
		img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
		results = detect(img)

		for cat, score, bounds in results:
			x, y, w, h = bounds

			cv2.rectangle(img, (int(x - w/2), int(y -h/2)), (int(x + w/2), int(y + h/2)), (255,0,0), thickness =4)
			cv2.putText(img, cat, (int(x), int(y), cvs.FONT_HERSHEY_DUPLEX, 5, (0, 0, 255), thickness =2)

		cv2.imshow(img)
		cv2.waitKey()
