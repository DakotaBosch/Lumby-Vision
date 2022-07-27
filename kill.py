import cv2
import numpy as np
import time
import mss
from pydarknet import Detector, Image
import WindMouse as wm
import random
import pyautogui
import mouse

x0 = 80
y0 = 250

mon = {'top': y0, 'left': x0, 'width':900, 'height':500}

count = 0
t = time.time()
xi=0
yi=0
t1=time.time()-10

net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("backup/yolov3-tiny_final.weights", encoding="utf-8"), 0,
               bytes("custom/lumby.data", encoding="utf-8"))


with mss.mss() as sct:
	while True:
		radius=5000
		count +=1
		im = sct.grab(mon)
		img = np.array(im)
		#print(img, img.shape)

		#img = PIL.Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
		img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
		#print(img, img.shape)

		im2 = Image(img)
		results = net.detect(im2)

		#print('\n\nRESULTS', results)
		#cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		count2=0
		for cat, score, bounds in results:
			x, y, w, h = bounds
			string = str(round(score*100)) + '%'
			cv2.rectangle(img, (int(x - w/2), int(y -h/2)), (int(x + w/2), int(y + h/2)), (0,255,0), thickness =1)
			#cv2.rectangle(img, (int(x-w/2), int(y-h/2)), (int(x-w/2+34), int(y-h/2-11)), (0,255,0), -1)
			#cv2.putText(img, string, (int(x-w/2), int(y-h/2-1)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), thickness =1)
			dist = ((x0-x)**2+(y0-y)**2)**.5
			if dist < radius:
				radius = dist
				target = results[count2][2]
			count2 +=1

		#cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)

		#if (time.time() % 8) == 0:
			#click in center of region, which region? random?

		#stop stream w/ user input 'q'
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

		if ( (round(t-time.time())%10 == 0) and len(results) > 0 and (time.time()-t1) >1):
			print('TARGET FOUND')
			t1 = time.time()
			#rand = round(time.time()) % len(results)
			#target = results[rand][2]
			#print(target, results[rand][2])
			randx = round(target[2]/2*7*(random.random()-0.5)**3)
			randy = round(target[3]/2*7*(random.random()-0.5)**3)
			xf=target[0] + randx
			yf=target[1] + randy
			#print('X and randx', target[0], randx,'Y and randy',target[1],randy)
			points = []
			wm.wind_mouse(xi, yi, xf, yf,  move_mouse=lambda x,y: points.append([x,y])) 
			xi = xf
			yi = yf

			for pos in range(0,len(points)):
				pyautogui.moveTo(points[pos][0]+x0,(points[pos][1]+y0), _pause=False)
				time.sleep(0.005)
			pyautogui.click()
		cv2.imshow('yoco',img)


print(round(count/(time.time()-t)), 'FPS')
