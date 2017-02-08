import cv2
import numpy as np
import moviepy.editor as mpy
#Read Image
filename = input("Enter filename: ")


width = 20
height = 20
channels = 3
colors = [[]]
fps = 20

bit_list = ''
with open(filename, "rb") as f:
	byte = f.read(1)
	while(byte):
		bit_list+='{0:08b}'.format(ord(byte))
		byte=f.read(1)

cc = 0
for b in bit_list:
    print(b)
    colors[cc].append(int(b)*255)
    if len(colors[cc])>=3:
    	colors.append([]) 
    	cc+=1

while(len(colors[-1])<3):
	colors[-1].append(127)

filename = ''.join('{0:08b}'.format(ord(x)) for x in filename)
print(filename)

cc+=1
colors.append([])
for b in filename:
    colors[cc].append(int(b)*255)
    if len(colors[cc])>=3:
    	colors.append([]) 
    	cc+=1

while(len(colors[-1])<3):
	colors[-1].append(127)

print(colors)

frames = len(colors)
duration = frames/fps
def make_frame(t):
	print(t*fps)
	ts = np.zeros(shape=(height,width,channels))
	for i in range(height):
		for j in range(width):
			for k in range(channels):
				ts[i][j][k]=colors[int(t*fps)][k]
	return ts

clip = mpy.VideoClip(make_frame, duration=duration) # 2 seconds
clip.write_videofile("movie.mp4",fps=fps)