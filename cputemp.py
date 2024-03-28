from gpiozero import CPUTemperature
from time import sleep
import datetime

while True:
    dateraw = datetime.datetime.now()
    date_format = dateraw.strftime('%Y%m%d')
    time_format = dateraw.strftime('%H%M%S')
    temp = str(CPUTemperature())
    print(temp[-6:-1])
    save_path = '/home/fofs/Desktop/camera_captures/' + date_format + 'cputemp.txt'
    f = open(save_path, 'a')
    f.write('CPU Temp: ' + temp[-6:-1] + ' at ' + time_format + '\n')
    f.close
    sleep(30)