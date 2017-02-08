import cv2
import numpy as np
import os

width = 640
height = 360
channels = 3
colors = []
fn = []
movie = input("Enter video filename:")
cap = cv2.VideoCapture(movie)
escape = 0
fntrig = False
while(cap.isOpened()):
	l = cap.read()[1][0][0][::-1].tolist()
	while(l[-1]>2 and l[-1]<250):
		if(fntrig==False):
			escape += 1
		fntrig = True
		l.pop(-1)
		if len(l)==1:
			break
	fntrig = False
	if escape==0:
		colors+=l
	elif escape==1:
		colors+=l
		escape+=1
	elif escape==2:
		fn+=l
	else: 
		fn+=l
		break

bit_list = ''
for c in range(len(colors)):
	colors[c]=int(colors[c]/200)
	bit_list+=str(colors[c])

filename_bits = ''
for f in range(len(fn)):
	filename_bits+=str(int(fn[f]/200))

def bitstring_to_bytes(s):
    return bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))

f = bitstring_to_bytes(filename_bits).decode()
f = os.path.abspath(f)
print(f)
r = bitstring_to_bytes(bit_list)
output_file = open(f, 'wb')
output_file.write(r)