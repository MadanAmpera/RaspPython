## - url: https://projects.raspberrypi.org/en/projects/push-button-stop-motion

## - command to test the camera

raspistill -k

## - Program to capture images

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

## - Program using buttons

from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
sleep(3)
camera.capture('/home/pi/image3.jpg')
camera.stop_preview()

## - Images for stop motion video

from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
