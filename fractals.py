#-*- coding: utf-8 -*-
# Serpinski Triangle with random and matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['ggplot','seaborn-talk'])
plt.gcf().canvas.set_window_title('Fractals chaos method demo. Press [ESC] to the next figure...')

# --- Globals
plot_width = 65536
plot_height = plot_width
IterationsPerFrame = 4096
MaxIterations = 65536
CurrentIteration = 0
Show = True

def onkeypressed(event):			
	global Show
	if event.key == 'escape':
		Show = False

class Point2D:
	def __init__(self, p2d):
		self.x = p2d[0]
		self.y = p2d[1]
		
class Triangle:		
	def __init__(self):
		self.p1 = Point2D((0, 0))
		self.p2 = Point2D((plot_width, 0))
		self.p3 = Point2D((plot_width // 2, plot_width*np.sqrt(3)//2))
		self.points = [self.p1, self.p2, self.p3]
	
class Rectangle:
	def __init__(self, base):
		self.p1 = Point2D((0,0))
		self.p2 = Point2D((base,0))
		self.p3 = Point2D((base,base))
		self.p4 = Point2D((0,base))
		self.points = [self.p1, self.p2, self.p3, self.p4]
		
triangle  = Triangle()
rectangle = Rectangle(plot_width)

for p in rectangle.points:
	print("x={}, y={}".format(p.x,p.y))
exit

xticks = np.zeros(IterationsPerFrame)
yticks = np.zeros(IterationsPerFrame)
plt.yticks([])
plt.xticks([]) 

# --- Serpinski randomised Triangle
plt.subplots_adjust(bottom=0.01, top=0.96, left=0.01, right=0.99)
# Randomly plot first pixel
x0 = np.random.randint(plot_width)
y0 = np.random.randint(plot_height)
while Show and CurrentIteration < MaxIterations:
	points = np.random.randint(0, 3, IterationsPerFrame)
	for i,p in enumerate(points):
		xticks[i] = (x0 + triangle.points[p].x) // 2
		yticks[i] = (y0 + triangle.points[p].y) // 2
		x0, y0 = xticks[i], yticks[i]
	CurrentIteration += IterationsPerFrame
	plt.plot(xticks, yticks, 'r.')
	plt.title("Serpinski randomised Triangle. Iterations: {}".format(CurrentIteration))
	plt.connect('key_press_event', onkeypressed)
	plt.pause(0.01)
plt.gcf().canvas.set_window_title('Fractal paint finished. Press [ESC] to the next one.')
Show = True	
while Show:
	plt.connect('key_press_event', onkeypressed)
	plt.pause(0.1)
plt.cla()
plt.gcf().canvas.set_window_title('Fractals chaos method demo. Press [ESC] to the next one...')
plt.style.use(['ggplot','seaborn-talk'])
plt.subplots_adjust(bottom=0.01, top=0.96, left=0.01, right=0.99)
plt.yticks([])
plt.xticks([]) 

# --- Serpinski randomised Rectangle
CurrentIteration = 0
Show = True
# Randomly plot first pixel
x0 = np.random.randint(plot_width)
y0 = np.random.randint(plot_height)
while Show and CurrentIteration < MaxIterations:
	points = np.random.randint(0, 4, IterationsPerFrame)
	for i,p in enumerate(points):
		xticks[i] = (x0 + rectangle.points[p].x) // 3
		yticks[i] = (y0 + rectangle.points[p].y) // 3
		x0, y0 = xticks[i], yticks[i]
	CurrentIteration += IterationsPerFrame
	plt.plot(xticks, yticks, 'r.')
	plt.title("Serpinski randomised Rectangle. Iterations: {}".format(CurrentIteration))
	plt.connect('key_press_event', onkeypressed)
	plt.pause(0.01)
plt.gcf().canvas.set_window_title('Fractal paint finished. Just close this window.')
plt.show()


