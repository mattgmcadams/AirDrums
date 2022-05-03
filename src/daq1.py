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
serR = serial.Serial('/dev/ttyACM1', 9600)
print(serR.name)

# set path in which you want to save images
path = 'data/raw'
dt = datetime.now().strftime("%m%d%Y-%H%M%S")

img_path = os.path.join(path, dt)
os.mkdir(img_path)


# changing directory to given path
os.chdir(img_path)

# i variable is to give unique name to images
# i = 1

# dataframe to save timestamps to the saved image
metadf0 = pd.DataFrame(columns=['timestamp', 'b_0', 'b_1', 'b_2', 'b_3', 'axL', 'ayL', 'azL', 'gxL', 'gyL', 'gzL', 'mxL', 'myL', 'mzL', 'tbsL', 'axR', 'ayR', 'azR', 'gxR', 'gyR', 'gzR', 'mxR', 'myR', 'mzR', 'tbsR', 'trash'])
# metadf1 = pd.DataFrame(columns=['filename', 'timestamp', 'b_0', 'b_1', 'b_2', 'b_3', 'axL', 'ayL', 'azL', 'gxL', 'gyL', 'gzL', 'mxL', 'myL', 'mzL', 'tbsL', 'axR', 'ayR', 'azR', 'gxR', 'gyR', 'gzR', 'mxR', 'myR', 'mzR', 'tbsR', 'trash'])
ts1 = time.time()


# Open the camera
video0 = cv2.VideoCapture(0)
# video4 = cv2.VideoCapture(4)

#set up the drums
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

while gamepad.isConnected():

	# Wait for the next event
	eventType, control, value = gamepad.getNextEvent()

	if control == buttonStart:
		if value:
			start = True
			sleep(2)
			break

while True:

	if start:

		# Read video, extract and return the frame
		# ret0, img0 = video0.read()
		# ret4, img4 = video4.read()

		# concatenate images Vertically
		# Verti = np.concatenate((img0, img4), axis=0)

		# Display the image
		cv2.imshow('live video', img0)


		# wait for user to press any key
		key = cv2.waitKey(5)

		binL = serL.readline()
		binR = serR.readline()

		dataL = str(binL).split(':')
		dataR = str(binR).split(':')

		try:
			[axL, ayL, azL, gxL, gyL, gzL, mxL, myL, mzL, tbsL] = str(binL).split(':')
			[axR, ayR, azR, gxR, gyR, gzR, mxR, myR, mzR, tbsR] = str(binR).split(':')
			trash = 'none'
			axL = axL[2:]
			axR = axR[2:]
			tbsL = tbsL[:-5]
			tbsR = tbsR[:-5]
		except:
			[axL, ayL, azL, gxL, gyL, gzL, mxL, myL, mzL, tbsL] = None, None, None, None, None, None, None, None, None, None
			[axR, ayR, azR, gxR, gyR, gzR, mxR, myR, mzR, tbsR] = None, None, None, None, None, None, None, None, None, None
			trash = f'{dataL}::{dataR}'




		# try:
		# 	ax = float(_ax)
		# 	ay = float(_ay)
		# 	az = float(_az)
		# except:
		# 	ax, ay, az = None, None, None
		#
		# try:
		# 	gx = float(_gx)
		# 	gy = float(_gy)
		# 	gz = float(_gz)
		# except:
		# 	gx, gy, gz = None, None, None
		#
		# try:
		# 	mx = float(_mx)
		# 	my = float(_my)
		# 	mz = float(_mz)
		# except:
		# 	mx, my, mz = None, None, None


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


		# Determine the type
		# if eventType == 'BUTTON':
		# 	# Button changed
		# 	if control == button0:
		# 		# Trigger
		# 		if value:
		# 			print('b0 hit')
		# 			b0 = 1
		#
		# 	elif control == button1:
		# 		# Left
		# 		if value:
		# 			print('b1 hit')
		# 			b1 = 1
		#
		# 	elif control == button3:
		# 		if value:
		# 			print('b3 hit')
		# 			b2 = 1
		#
		# 	elif control == button2:
		# 		if value:
		# 			print('b2 hit')
		# 			b3 = 1
		#
		# 	elif control == buttonExit:
		# 		# Exit
		# 		if value:
		# 			start = False
		# 			break


		# filename0 = f'cam0_{str(i)}.jpg'
		# filename1 = f'cam1_{str(i)}.jpg'

		ts2 = time.time()# - ts1

		# Save the images in given path
		# cv2.imwrite(filename0, img0)
		# cv2.imwrite(filename1, img4)
		# i = i+1

		metadf0.loc[len(metadf0.index)] = [ts2, b0, b1, b2, b3, axL, ayL, azL, gxL, gyL, gzL, mxL, myL, mzL, tbsL, axR, ayR, azR, gxR, gyR, gzR, mxR, myR, mzR, tbsR, trash]
		# metadf1.loc[len(metadf1.index)] = [ts2, b0, b1, b2, b3, axL, ayL, azL, gxL, gyL, gzL, mxL, myL, mzL, tbsL, axR, ayR, azR, gxR, gyR, gzR, mxR, myR, mzR, tbsR, trash]

# # close the camera
video0.release()
# video4.release()

# close open windows
cv2.destroyAllWindows()

# save meta to csv
# metadf_all = pd.concat([metadf0, metadf1], ignore_index=True)
metadf0.to_csv('meta.csv', index=False)
# metadf1.to_csv('meta_cam1.csv', index=False)
# metadf_all.to_csv('meta.csv', index=False)

