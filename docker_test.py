from pydarknet import Detector, Image
import cv2
import os
import time

if __name__ == "__main__":
    net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("backup/yolov3-tiny_final.weights", encoding="utf-8"), 0,
                   bytes("custom/lumby.data", encoding="utf-8"))

    input_files = os.listdir("data/custom/")
    init = time.time()
    count=0
    for file_name in input_files:
        if not file_name.lower().endswith(".png"):
            continue

        print("File:", file_name)
        count +=1
        #cv2.imread reduces RBGX to rgb
        img = cv2.imread(os.path.join("data/custom/", file_name))
        img2 = Image(img)

        start_time = time.time()
        print('\n SHAPE: ', img.shape, type(img), img, '\n')
        results = net.detect(img2)
        print('\n Results', results, '\n')
        end_time = time.time()

        print("Elapsed Time:", end_time - start_time)

        for cat, score, bounds in results:
            x, y, w, h = bounds
            string = str(round(score*100)) + '%'
            print(f"{cat} at [{x},{y}]: Confidence: {score}")
            cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h/2)), (0, 255, 0),
                          thickness=1)
            cv2.rectangle(img,(int(x-w/2), int(y-h/2)), (int(x -w/2+35), int(y - h/2-11)), (0,255,0), -1)
            cv2.putText(img, string, (int(x-w/2), int(y-h/2-2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0,0), thickness=1)

        cv2.imwrite(os.path.join("results/", file_name), img)
    print( 'FPS : ', count / (time.time() - init) )
