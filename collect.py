import mss
import time
import cv2
import numpy as np
from PIL import Image


start_time = time.time()

#screenshot location
mon = {'top': 40, 'left': 60, 'width': 1800, 'height': 1000}

duration = np.empty((1,))
count =0

with mss.mss() as sct:
    while True:
        count += 1
        last_time = time.time()
        im = sct.grab(mon)

        #convert mss image to PIL image, BRG OR RGB
        img = Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
        
        scale = 0.1

        #compress PIL image to (X,Y)
        img = img.resize(img.shape*scale)
        
        wid, hgt = img.size

        duration = np.append(duration, time.time()*1000-last_time*1000)

        cv2.imshow('test', np.array(img))
        
        #why are blue and red opposite of the live output
        img.save("darknet/data/custom/" + str(count) + '.png')
        time.sleep(5)


        #break cycle w/ user input 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
    print(str(wid) + "x" + str(hgt))