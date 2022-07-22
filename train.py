import os

data = ' config/obj.data'
cfg = ' config/yolov3-tiny.cfg'
init = ' config/darknet53.conv.74'
dark = './darknet'
function = ' detector train'
flags = ' -dont_show -map'

arg = dark + function + data + cfg + init + flags

print(arg)
os.system(arg)
