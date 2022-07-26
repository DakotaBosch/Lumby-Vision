import cv2
import numpy as np
import time
import mss
from pydarknet import Detector, Image


def yoco(im):
	net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("backup/yolov3-tiny_final.weights", encoding="utf-8"), 0,
                       bytes("custom/lumby.data",encoding="utf-8"))

	#img = cv2.imread(im)

	img = pydarkImage(im)
	#print('\n\n SHAPE', im.shape, type(im), '\n')
	results = net.detect(img)
	#print(results)
	return results


mon = {'top':280, 'left': 80, 'width':900, 'height':500}

count = 0
t = time.time()


net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("backup/yolov3-tiny_final.weights", encoding="utf-8"), 0,
               bytes("custom/lumby.data", encoding="utf-8"))


with mss.mss() as sct:
	while True:
		count +=1
		im = sct.grab(mon)
		img = np.array(im)
		#print(img, img.shape)

		#img = PIL.Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
		img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
		#print(img, img.shape)

		im2 = Image(img)
		results = net.detect(im2)

		#print('RESULTS', results)
		#cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		for cat, score, bounds in results:
			x, y, w, h = bounds
			string = str(round(score*100)) + '%'
			cv2.rectangle(img, (int(x - w/2), int(y -h/2)), (int(x + w/2), int(y + h/2)), (0,255,0), thickness =1)
			cv2.rectangle(img, (int(x-w/2), int(y-h/2)), (int(x-w/2+34), int(y-h/2-11)), (0,255,0), -1)
			cv2.putText(img, string, (int(x-w/2), int(y-h/2-1)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), thickness =1)
		#cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
		cv2.imshow('yoco', img)

		#stop stream w/ user input 'q'
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

print(count/(time.time()-t), 'FPS')
