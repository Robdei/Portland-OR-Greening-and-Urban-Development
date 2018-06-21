import os, sys, glob
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


for file in glob.glob('*.tif'):
	direc=[]
	im=Image.open(file)
	im.mode='I'
	print(file)
	pix=im.load()
	w,h=im.size
	for x in range(w):
		for y in range(h):
			direc.append(pix[x,y]/10000)
	direc=np.array(direc)
	plt.hist(direc,bins='auto',color='C0')
	plt.xlabel('NDVI')
	plt.ylabel('Frequency')
	axes = plt.gca()
	axes.set_xlim([-.2,1])
	axes.set_ylim([0,2200000])
	plt.title(file[:-4]+' NDVI Frequency')
	plt.savefig(file[:-4]+'.png')
	plt.clf()





