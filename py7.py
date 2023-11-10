import os

if os.path.exists('iot2.txt') :
    os.remove('iot2.txt')
else :
    print('ไม่มีไฟล์')