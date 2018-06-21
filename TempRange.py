from PIL import Image
import glob
import pandas as pd
import math

#data=pd.read_excel('Portland Greening.xlsx',sheetname='Landsat Data')
#ML=data['ML10'].tolist()
files=[]
for i in glob.glob('*.tif'):
	files.append(i)
ML=0.0003342
AL=0.1
k1=774.8853
k2=1321.0789
def radiance(Intensity):
	return(ML*Intensity+AL)
def Temp(Radiance):
	return(k2/(math.log(k1/Radiance+1)))
#print(files)

for file in files:
	
	im=Image.open(file)
	pix=im.load()
	w,h=im.size
	low=Temp(radiance(pix[w/2,h/2]))
	high=Temp(radiance(pix[0,0]))
	poshigh=0
	poslow=0
	for x in range(w):
		for y in range(h):
			if Temp(radiance(pix[x,y]))<low and int(Temp(radiance(pix[x,y])))!=147:
				low=Temp(radiance(pix[x,y]))
				poslow=[x,y]
			if Temp(radiance(pix[x,y]))>high:
				high=Temp(radiance(pix[x,y]))
				poshigh=[x,y]
	print([poslow,poshigh])
	#print([file,low,high])
	