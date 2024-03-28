from picamera2 import Picamera2, Preview
from os import system
from time import sleep
import datetime
import os.path
import socket

## Picamera configuration #############################################
# configure and set configuration for cameras with specified resoultion
#######################################################################
picam0 = Picamera2(0)
picam1 = Picamera2(1)
config0 = picam0.create_still_configuration({"size": (4056, 3040)})
config1 = picam1.create_still_configuration({"size": (4056, 3040)})
picam0.configure(config0)
picam1.configure(config1)

sleep(300)  #Time delay to allow system to boot and update time/date
#######################################################################
'''
def add_log(log_info, x):
    save_path = '/home/fofs/Desktop/camera_captures/' + date_time_format + '.txt'
    if x == 0:
        f = open(save_path, 'a')
        f.write(log_info + '\n')
        f.close
    if x == 1:
        f = open(save_path, 'r')
        lines = f.readlines()[:-2]
        lines.append(log_info + '\n\n')
        f.close()
        f = open(save_path, 'w')
        f.writelines(lines)
    if x == 2:
        f2 = open(path + '/' + time_format + 'gps_log.txt', 'a')
        f2.write(log_info)
        f2.close
        '''

### Function to take the photos ###################################################
# 
def take_pic():
    dateraw = datetime.datetime.now()
    date_format = dateraw.strftime('%Y%m%d')
    time_format = dateraw.strftime('%H%M%S')
    # Put images into the folder corresponding to the day
    if not os.path.isdir(path1 + date_format + '/'):
        os.makedirs(path1 + date_format + '/')
        print('Created date folder')
    if not os.path.isdir(path2 + date_format + '/'):
        os.makedirs(path2 + date_format + '/')
        print('Created date folder')
    picture_filename1 = path1 + date_format + '/' + time_format +'.jpg'
    picture_filename2 = path2 + date_format + '/' + time_format +'.jpg'
    picam0.start()
    picam1.start()
    picam0.capture_file(picture_filename1)
    picam1.capture_file(picture_filename2)
    picam0.stop()
    picam1.stop()
    print('Images captured as', picture_filename1[-10:], picture_filename2[-10:])
    save_path = '/home/fofs/Desktop/camera_captures/' + date_format + '.txt'
    f = open(save_path, 'a')
    f.write('Images captured as ' + picture_filename1[-10:] + picture_filename2[-10:] + '\n')
    f.close

##################################################################################
#add_log('RPi started taking photos for your timelapse at: ' + date_time_format + ':' + time_format, 0)

### Create directories for the camera captures if they don't exist ############
path1 = '/home/fofs/Desktop/camera_captures/cam1/'
path2 = '/home/fofs/Desktop/camera_captures/cam2/'

isdir1 = os.path.isdir(path1)
isdir2 = os.path.isdir(path2)
if not isdir1:
    os.makedirs(path1)
    print('Created directory for cam 1')
if not isdir2:
    os.makedirs(path2)
    print('Created directory for cam 2')
################################################################################
'''
isdir1 = os.path.isdir(path1)
isdir2 = os.path.isdir(path2)

if isdir1 is True:
    for i in range(1000):
        path1 = '/home/fofs/Desktop/camera_captures/cam1/' + date_time_format + '_' + str(i)
        isdir_new = os.path.isdir(path1)
        if not isdir_new:
            os.mkdir(path1)
            add_log('Additional directory for current date created:' + path1, 0)
            break
else: os.mkdir(path1)

if isdir2 is True:
    for i in range(1000):
        path1 = '/home/fofs/Desktop/camera_captures/cam2/' + date_time_format + '_' + str(i)
        isdir_new = os.path.isdir(path2)
        if not isdir_new:
            os.mkdir(path2)
            add_log('Additional directory for current date created:' + path2, 0)
            break

else: os.mkdir(path2)

add_log('Photo Directory: ' + path1, 0)
add_log('Photo Directory: ' + path2, 0)
'''
#print('path = ' + path)

#camera = PiCamera()
#add_log('Pictures starting', 0)

###########################################################################
### Taking photos faster than ~1 per second lead to blurry photos
### The Pi camera needs time to focus and adjust exposure and white balance
pic_count = 1
while True:
    dateraw = datetime.datetime.now()
    date_format = dateraw.strftime('%Y%m%d')
    time_int = int(dateraw.strftime('%S'))
    if time_int % 3 == 0: #takes photos every 3 seconds
        take_pic()
        pic_count += 1
        #add_log('Picture count: ' + str(pic_count), 1)
###########################################################################

