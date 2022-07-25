import os
import time

data = ' custom/lumby.data'
cfg = ' custom/yolov3-tiny.cfg'
init = ' backup/yolov3-tiny_final.weights data/custom/5.png'
dark = './darknet'
function = ' detector demo'
#flags = ' -dont_show -map'

arg = dark + function + data + cfg + init

print(arg)

initial = time.time()
os.system(arg)
print(time.time() - initial)
