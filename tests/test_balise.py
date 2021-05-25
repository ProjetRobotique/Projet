from PIL import Image

d1= {"green":(0,150,0), "red":(150,0,0),"blue":(34, 54, 91), "yellow":(230,230,0), "cyan":(0,255,255),"purple":(255,0,255), "white":(255,255,255), "black":(0,0,0)}
d= {"green":(99,134,97), "red":(130,66,57),"blue":(34, 54, 91), "yellow":(221,214,129), "cyan":(0,255,255),"purple":(255,0,255), "white":(255,255,255), "black":(0,0,0)}

img= Image.open("Image/balise.jpg")
img.show()
def blue(doc):
	img= Image.open(doc)
	width = img.size[0] #largeur
	height= img.size[1] #longueur
	n=0
	R=0
	G=0
	B=0
	A=0
	for x in range(0, width):
		for y in range(0, height):
			pixel= img.getpixel((x,y))
			(r,g,b,a)=pixel;
			R+=r
			G+=g
			B+=b
			A+=a
			n+=1
	R/=n
	G/=n
	B/=n
	A/=n
	img.close()
	return (R,G,B,A)

def colorAffiche():
	img2= Image.new('RGB', (img.size[0],img.size[1]), color= 'white')
	pixels= img2.load()
	for x in range(0, 200):
		for y in range(0, 200):
			pixels[x, y]= d["green"]
	for x in range(200, 400):
		for y in range(0, 200):
			pixels[x, y]= d["blue"]
	for x in range(0, 200):
		for y in range(200, 400):
			pixels[x, y]= d["yellow"]
	for x in range(200, 400):
		for y in range(200, 400):
			pixels[x, y]= d["red"]
	img2.show()


def chercheBalise(img):
	pixels= img.load()
	width = img.size[0] #largeur
	height= img.size[1] #longueur
	for x in range(0, width, 10):
		for y in range(0, height, 10):
			if getColorName(img.getpixel((x,y)))=="green":
				v=estBalise(img, x, y)
				if v!=(-1,-1):
					print(v)
					for i in range(-5,5):
						for j in range(-5,5):
							pixels[v[0]+i, v[1]+j]= d["white"]
					img.show()
					return ((v[0]-width/2)/width*0.5)*100
	print("absent")
	return "Balise absent"

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
		if longueur>=15 and i<width and getColorName(img.getpixel((i,j)))=="blue":
			xc= i
			longueur=0
			for k in range(15):
				i+=1
				if i>=width-1: break
				if not getColorName(img.getpixel((i,j)))=="blue":
					return (-1,-1)
		else: return (-1,-1)
		i=x+5
		if i>width: i=x
		longueur=0
		while j<height and getColorName(img.getpixel((i,j)))=="green":
			j+=1
			longueur+=1
		if longueur>=15 and j<height and getColorName(img.getpixel((i,j)))=="yellow":
			yc= j
			longueur=0
			for k in range(15):
				j+=1
				if j>=height-1:
					break
				if not getColorName(img.getpixel((i,j)))=="yellow":
					return (-1,-1)
		longueur=0
		while i<width and j<height and getColorName(img.getpixel((i,j)))=="yellow":
			i+=1
			longueur+=1
		if longueur>=15 and i<width and getColorName(img.getpixel((i,j)))=="red":
			longueur=0
			for k in range(15):
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
	minimum = 40000
	cname=""
	d= {"green":(99,134,97), "red":(130,66,57),"blue":(34, 54, 91), "yellow":(221,214,129), "cyan":(0,255,255),"purple":(255,0,255), "white":(255,255,255), "black":(0,0,0)}
	for color, (r,g,b) in d.items():
		d = abs(R- int(r)) + abs(G- int(g))+ abs(B- int(b))
		if(d<=minimum):
			minimum = d
			cname = color
	return cname

def voir(img):
	img2= Image.new('RGB', (img.size[0],img.size[1]), color= 'white')
	pixels= img2.load()
	width = img.size[0] #largeur
	height= img.size[1] #longueur
	for x in range(0, width):
		for y in range(0, height):
			pixels[x,y] =d[getColorName(img.getpixel((x,y)))]
	img2.show()

def colorVal():
	b=blue("blue.jpg")
	g=blue("green.jpg")
	y=blue("yellow.jpg")
	r=blue("red.jpg")
	black=blue("black.jpg")
	print()
	print("green :", g)
	print("blue :", b)
	print("yellow :", y)
	print("red :", r)
	print("black :", black)

chercheBalise(img)
img.close()