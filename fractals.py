#-*- coding: utf-8 -*-
# Serpinski Triangle with random and matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['ggplot','seaborn-talk'])
plt.gcf().canvas.set_window_title('Fractals chaos method demo. Press [ESC] to the next figure...')

# --- Globals
CanvasSize  = 65536
MaxIterations = 65536

def onkeypressed(event):			
	global Show
	if event.key == 'escape':
		Show = False

class Point2D:
	def __init__(self, p):
		self.x = p[0]
		self.y = p[1]
	def GetDistancePart(self, p2, part):
		x = (self.x + p2.x) // part
		y = (self.y + p2.y) // part
		return (x,y)		
	def GetMidpoint(self, p2):
		return self.GetDistancePart(p2, 2)

class Attractor:
	def __init__(self, title):
		self.title = title
		self.numpoints = 0
		
class Triangle(Attractor):
	def __init__(self, title, base):
		Attractor.__init__(self, title)
		self.numpoints = 3
		self.p1 = Point2D((0, 0))
		self.p2 = Point2D((base, 0))
		self.p3 = Point2D((base // 2, base*np.sqrt(3)//2))
		self.points = [self.p1, self.p2, self.p3]
	
class Rectangle(Attractor):
	def __init__(self, title, base):
		Attractor.__init__(self, title)
		self.numpoints = 4
		p1 = Point2D((0,0))
		p2 = Point2D((base,0))
		p3 = Point2D((base,base))
		p4 = Point2D((0,base))
		self.points = [p1, p2, p3, p4]
		
class Rectangle8p(Rectangle):
	def __init__(self, title, base):
		Rectangle.__init__(self, title, base)
		for i in range(len(self.points)):
			j = i << 1
			k = (j+1) % len(self.points)
			p1 = self.points[j]
			p2 = self.points[k]
			self.points.insert(j+1, Point2D(p1.GetMidpoint(p2)))
		self.numpoints = len(self.points)
		
class FractalsCollection:
	def __init__(self, canvassize, maxiterations):
		self.collection = []
		self.dividers = []
		self.canvassize = canvassize
		self.maxiterations = maxiterations
	def additem(self, item, divider):
		self.collection.append(item)
		self.dividers.append(divider)
	def WaitForKeyPressed(self):
		global Show
		plt.gcf().canvas.set_window_title('Fractal paint finished. Press [ESC] to the next one.')
		Show = True	
		while Show:
			plt.connect('key_press_event', onkeypressed)
			plt.pause(0.1)
		plt.cla()
	def showfractal(self, itemnum, divider):
		global Show
		x0 = np.random.randint(self.canvassize)
		y0 = np.random.randint(self.canvassize)
		plt.yticks([])
		plt.xticks([]) 
		plt.subplots_adjust(bottom=0.01, top=0.96, left=0.01, right=0.99)
		IterationsPerFrame = self.maxiterations >> 4
		CurrentIteration = 0 
		fractal = self.collection[itemnum]
		xticks = np.empty(IterationsPerFrame)
		yticks = np.empty(IterationsPerFrame)
		Show = True
		while Show and CurrentIteration < MaxIterations:
			points = np.random.randint(0, fractal.numpoints, IterationsPerFrame)
			for i,p in enumerate(points):
				xticks[i] = (x0 + fractal.points[p].x) // divider
				yticks[i] = (y0 + fractal.points[p].y) // divider
				x0, y0 = xticks[i], yticks[i]
			CurrentIteration += IterationsPerFrame
			plt.plot(xticks, yticks, 'r.')
			plt.title(fractal.title + " Iterations: {}".format(CurrentIteration))
			plt.connect('key_press_event', onkeypressed)
			plt.pause(0.01)
	def ShowCollection(self):
		totalitems = len(self.collection)
		for itemnum, fractal in enumerate(self.collection):
			self.showfractal(itemnum, self.dividers[itemnum])
			if itemnum + 1 < totalitems:
				myfractals.WaitForKeyPressed()
		plt.gcf().canvas.set_window_title('Fractal paint finished. Just close this window.')
		plt.show()
		
myfractals = FractalsCollection(CanvasSize, MaxIterations)
myfractals.additem(Triangle("Serpinski 3-point Triangle.", CanvasSize), 2)
myfractals.additem(Rectangle("Serpinski 4-point Rectangle.", CanvasSize), 3)
myfractals.additem(Rectangle8p("Serpinski 8-point Rectangle.", CanvasSize), 3)
myfractals.ShowCollection()
