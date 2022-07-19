import os

data = ' .\\config\\obj.data'
cfg = ' .\\config\\yolov3-tiny.cfg'
init = ' .\\config\\darknet53.conv.74'
dark = 'darknet\\darknet_no_gpu.exe'
function = ' detector train'
arg = dark + function + data + cfg + init

print(arg)
os.system(arg)
