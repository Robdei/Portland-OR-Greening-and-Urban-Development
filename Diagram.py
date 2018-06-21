from PIL import Image
im=Image.open('20170714Natural.jpg')
Positions=[3022,5830]
Direction=['E','NE','N','NW','W','SW','S','SE']
pix=im.load()

for d in Direction:
	

	if d=='E':
		count=-1
		for x in range(Positions[0],Positions[0]+2001):
			count=count+1
			pix[x,Positions[1]]=(255,0,30)
		#im.save(files[i][:-4]+d+'.tif')
	if d=='NE':
		count=1
		for x in range(Positions[0],Positions[0]+1415):
			count=count-1
			pix[x,Positions[1]+count]=(150,0,55)
			#im.save(files[i][:-4]+d+'.tif')
	if d=='N':
		count=-1
		for y in range(0,2001):
			count=count+1
			pix[Positions[0],Positions[1]-count]=(0,255,0)
		#im.save(files[i][:-4]+d+'.tif')
	if d=='NW':
		count=1
		for x in range(Positions[0],Positions[0]+1415):
			count=count-1
			pix[Positions[0]+count,Positions[1]+count]=(250,0,0)
		#im.save(files[i][:-4]+d+'.tif')
	if d=='W':
		count=1
		for x in range(Positions[0],Positions[0]+1415):
			count=count-1
			pix[Positions[0]+count,Positions[1]]=(0,0,255)
		#im.save(files[i][:-4]+d+'.tif')
	if d=='SE':
		count=1
		for x in range(Positions[0],Positions[0]+1415):
			count=count-1
			pix[Positions[0]-count,Positions[1]-count]=(250,30,30)
im.save('diagram.jpg')
