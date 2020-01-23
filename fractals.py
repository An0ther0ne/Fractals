#-*- coding: utf-8 -*-
# Serpinski Triangle with chaos method and matplotlib

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
	def PrintPoint(self):
		print("x={}, y={}".format(self.x, self.y))

class Attractor:
	def __init__(self, title):
		self.title = title
		self.numpoints = 0
		
class FractalObject(Attractor):
	def __init__(self, title, base, numpoints, midpoints=False):
		Attractor.__init__(self, title)
		self.points=[]
		x0 = y0 = base // 2
		R = np.sqrt(base*base/2)
		for i in range(numpoints):
			A = np.pi
			A = 2*i*A/numpoints - A*(numpoints - 2)/2/numpoints
			x = np.round(x0 - R*np.cos(A))
			y = np.round(y0 + R*np.sin(A))
			p2 = Point2D((x, y))
			if midpoints and i>0:
				p1 = self.points[len(self.points)-1]
				self.points.append(Point2D(p1.GetMidpoint(p2)))
			self.points.append(p2)
		if midpoints:
			p1 = self.points[0]
			self.points.append(Point2D(p2.GetMidpoint(p1)))
		self.numpoints = len(self.points)
	def PrintPoints(self):
		for i,p in enumerate(self.points):
			print(i,'::', end='')
			p.PrintPoint()

class FractalsCollection:
	def __init__(self, canvassize, maxiterations):
		self.collection = []
		self.dividers = []
		self.canvassize = canvassize
		self.maxiterations = maxiterations
	def AddItem(self, item, divider):
		self.collection.append(item)
		self.dividers.append(divider)
	def GetItem(self, item):
		return self.collection[item]
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
myfractals.AddItem(FractalObject("Serpinski 3-point Triangle.", CanvasSize, 3), 2)
myfractals.AddItem(FractalObject("Serpinski 4-point Rectangle.", CanvasSize, 4), 3)
myfractals.AddItem(FractalObject("Serpinski 8-point Rectangle.", CanvasSize, 4, True), 3)
myfractals.AddItem(FractalObject("Serpinski Pentagon", CanvasSize, 5), 3)
myfractals.AddItem(FractalObject("Serpinski double points Pentagon", CanvasSize, 5, True), 3)
myfractals.AddItem(FractalObject("Serpinski Hexagon", CanvasSize, 6), 3)
myfractals.AddItem(FractalObject("Serpinski double points Hexagon", CanvasSize, 6, True), 4)
myfractals.AddItem(FractalObject("Serpinski Heptagon", CanvasSize, 7), 3)
myfractals.AddItem(FractalObject("Serpinski double points Heptagon", CanvasSize, 7, True), 4)
myfractals.AddItem(FractalObject("Serpinski Octagon", CanvasSize, 8), 3)
myfractals.AddItem(FractalObject("Serpinski double points Octagon", CanvasSize, 8, True), 4)
myfractals.ShowCollection()
