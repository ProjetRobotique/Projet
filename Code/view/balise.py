from PIL import Image

d= {"green":(0,200,0), "red":(200,0,0),"blue":(0,0,200), "yellow":(230,230,0), "cyan":(0,255,255),"purple":(255,0,255), "white":(255,255,255), "black":(0,0,0)}

def chercherBalise(img):
	print("cherche")
	width = img.size[0] #largeur
	height= img.size[1] #longueur
	for x in range(0, width, 30):
		for y in range(0, height, 30):
			if getColorName(img.getpixel((x,y)))=="green":
				v=estBalise(img, x+10, y+10)
				if v!=(-1,-1):
					return ((v[0]-width/2)/width*0.5)*100
	return "balise absent"

def estBalise(img, x, y):
	width = img.size[0] #largeur
	height= img.size[1] #longueur
	longueur=0
	xc=-1
	yc=-1
	i=x
	j=y
	if i>width or j>height: return (-1,-1)
	if getColorName(img.getpixel((i,j)))=="green":
		while i<width and getColorName(img.getpixel((i,j)))=="green":
			i+=1
			longueur+=1
		if longueur>=20 and i<width and getColorName(img.getpixel((i,j)))=="blue":
			xc= i
			longueur=0
			for k in range(20):
				i+=1
				if i>=width-1: break
				if not getColorName(img.getpixel((i,j)))=="blue":
					return (-1,-1)
		else: return (-1,-1)
		i=x+15
		longueur=0
		while j<height and getColorName(img.getpixel((i,j)))=="green":
			j+=1
			longueur+=1
		if longueur>=20 and j<height and getColorName(img.getpixel((i,j)))=="yellow":
			yc= j
			longueur=0
			for k in range(20):
				j+=1
				if j>=height-1:
					break
				if not getColorName(img.getpixel((i,j)))=="yellow":
					return (-1,-1)
		longueur=0
		while i<width and getColorName(img.getpixel((i,j)))=="yellow":
			i+=1
			longueur+=1
		if longueur>=10 and i<width and getColorName(img.getpixel((i,j)))=="red":
			longueur=0
			for k in range(20):
				i+=1
				if i>=width-1: 
					break
				if not getColorName(img.getpixel((i,j)))=="red":
					return (-1,-1)
		else: return (-1,-1)
		return (xc, yc)
	else: return (-1,-1)

def getColorName(pixel):
	R = pixel[0]
	G = pixel[1]
	B = pixel[2]
	d= {"green":(99,134,97), "red":(130,66,57),"blue":(34, 54, 91), "yellow":(221,214,129), "cyan":(0,255,255),"purple":(255,0,255), "white":(255,255,255), "black":(0,0,0)}
	minimum = 10000
	cname=""
	for color, (r,g,b) in d.items():
		d = abs(R- int(r)) + abs(G- int(g))+ abs(B- int(b))
		if(d<=minimum):
			minimum = d
			cname = color
	return cname
