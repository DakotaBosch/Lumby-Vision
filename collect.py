#Collect a series of pngs and resize
import mss
import time
import cv2
import numpy as np
from PIL import Image


start_time = time.time()

#screenshot location
mon = {'top': 30, 'left': 60, 'width': 1800, 'height': 1000}

duration = np.empty((1,))
count = 15

with mss.mss() as sct:
    while True:
        count += 1
        im = sct.grab(mon)

        #convert mss image to PIL image, BRG OR RGB
        img = Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
        
        scale = 0.5
        wid, hgt = img.size
        wid = int(scale*wid)
        hgt = int(scale*hgt)

        #compress PIL image to (X,Y)
        img = img.resize((wid,hgt))
        
        cvim = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        cv2.imshow('test', cvim)
        
        img.save("custom/" + str(count) + '.png')
        time.sleep(6)


        #break cycle w/ user input 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
    print(str(wid) + "x" + str(hgt))