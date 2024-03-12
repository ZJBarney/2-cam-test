 # importing libraries 
import os 
import cv2
import re
from PIL import Image

path1 = '/home/fofs/Desktop/camera_captures/cam1/'
path2 = '/home/fofs/Desktop/camera_captures/cam2/'
path3 = '/home/fofs/Desktop/camera_captures/cam3/'
uppath ='/home/fofs/Desktop/camera_captures/'

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir(path3)) 
print(num_of_images)

# Video Generating function 
def generate_video():
    video_name = 'testvid.avi'
    images = [img for img in os.listdir(path3) 
            if img.endswith(".jpg") or
                img.endswith(".jpeg") or
                img.endswith("png")]
    print(images)
    sorted_images = sorted(images)
    print(sorted_images)

    frame = cv2.imread(os.path.join(path3, sorted_images[0])) 

    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape 

    video = cv2.VideoWriter(video_name, 0, 24, (width, height))
    i = 0

    # Appending the images to the video one by one 
    for image in sorted_images:
        print("Image", i, "of", num_of_images)
        i += 1
        video.write(cv2.imread(os.path.join(path3, image))) 
        
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows() 
    video.release() # releasing the video generated 


# Calling the generate_video function 
generate_video() 
