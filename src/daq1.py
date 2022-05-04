# Import necessary libraries
import cv2
import os
from datetime import datetime
import pandas as pd
import numpy as np
import time
import Gamepad
import time
from time import sleep
import serial
# from google.colab.patches import cv2_imshow

serL = serial.Serial('/dev/ttyACM0', 9600) # open serial port
print(serL.name)     #check which port was really used
#serR = serial.Serial('/dev/ttyACM1', 9600)
#print(serR.name)

# series path in which you want to save images
path = 'data/raw'
dt = datetime.now().strftime("%m%d%Y-%H%M%S")

img_path = os.path.join(path, dt)
os.mkdir(img_path)


# changing directory to given path
os.chdir(img_path)

# i variable is to give unique name to images
# i = 1

# dataframe to save timestamps to the saved image
metadf0 = pd.DataFrame(columns=['timestamp', 'b_0', 'b_1', 'b_2', 'b_3', 'ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz', 'tbs', 'trash'])
# metadf1 = pd.DataFrame(columns=['filename', 'timestamp', 'b_0', 'b_1', 'b_2', 'b_3', 'axL', 'ayL', 'azL', 'gxL', 'gyL', 'gzL', 'mxL', 'myL', 'mzL', 'tbsL', 'axR', 'ayR', 'azR', 'gxR', 'gyR', 'gzR', 'mxR', 'myR', 'mzR', 'tbsR', 'trash'])
ts1 = time.time()


# Open the camera
#video0 = cv2.VideoCapture(0)
# video4 = cv2.VideoCapture(4)

#series up the drums
gamepadType = Gamepad.PS4
button0 = 'CROSS'
button1 = 'CIRCLE'
buttonExit = 'SHARE'
buttonStart = 'OPTIONS'
button2 = 'TRIANGLE'
button3 = 'SQUARE'

if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

start = False
img0 = cv2.imread('/home/matt/Documents/Drummers/sticks02.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

series = 'train'

while True:
	while gamepad.isConnected():

		# Wait for the next event
		eventType, control, value = gamepad.getNextEvent()

		if control == buttonStart:
			if value:
				start = True
				sleep(2)
				break

		if control == buttonExit:
			if value:
				exit()

	if series == 'test':
		rng = 5000
	elif series == 'train':
		rng = 20000

	for _ in range(rng):

		if start:

			cv2.imshow('inspirational image', img0)

			# wait for user to press any key
			key = cv2.waitKey(2)
			binary = serL.readline()
			data = str(binary).split(':')
			try:
				[ax, ay, az, gx, gy, gz, mx, my, mz, tbs] = str(bin).split(':')
				trash = 'none'
				ax = ax[2:]
				tbs = tbs[:-5]
			except:
				[ax, ay, az, gx, gy, gz, mx, my, mz, tbs] = None, None, None, None, None, None, None, None, None, None
				trash = data

			b0, b1, b2, b3 = 0, 0, 0, 0

			if key == ord('q'):
				start = False
				break
			if key == ord('v'):
				start = False
				break
			if key == ord('a'):
				print(' ~~  ~~ |||| ~~ ')
				b0 = 1
			if key == ord('s'):
				print(' ~~  ~~  ~~ ||||')
				b1 = 1
			if key == ord('d'):
				print('|||| ~~  ~~  ~~ ')
				b2 = 1
			if key == ord('f'):
				print(' ~~ |||| ~~  ~~')
				b3 = 1


			ts2 = time.time()# - ts1

			metadf0.loc[len(metadf0.index)] = [ts2, b0, b1, b2, b3, ax, ay, az, gx, gy, gz, mx, my, mz, tbs, trash]

	# close open windows
	cv2.destroyAllWindows()

	# save meta to csv
	metadf0.to_csv(f'{series}_meta.csv', index=False)

