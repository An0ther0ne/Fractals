#-*- coding: utf-8 -*-
# Serpinski Triangle with random and matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['ggplot','seaborn-talk'])
plt.gcf().canvas.set_window_title('Fractals demo with random. Press [ESC] to Exit...')

# --- Globals
plot_width = 500
plot_height = plot_width
CurrentIteration = 0
IterationsPerFrame = 1000
MaxIterations = 20000
Show = True

# Randomly plot first pixel
x0 = np.random.randint(plot_width)
y0 = np.random.randint(plot_height)

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
		self.p3 = Point2D((x0, plot_width*np.sqrt(3)//2))
		self.points = [self.p1, self.p2, self.p3]

triangle = Triangle()

xticks = np.zeros(IterationsPerFrame)
yticks = np.zeros(IterationsPerFrame)
plt.yticks([])
plt.xticks([]) 

while Show and CurrentIteration < MaxIterations:
	points = np.random.randint(0,3,IterationsPerFrame)
	for i,p in enumerate(points):
		xticks[i] = (x0 + triangle.points[p].x) // 2
		yticks[i] = (y0 + triangle.points[p].y) // 2
		x0, y0 = xticks[i], yticks[i]
	CurrentIteration += IterationsPerFrame
	plt.plot(xticks, yticks, 'r.')
	plt.title("Serpinski randomised Triangle. Iterations: {}".format(CurrentIteration))
	plt.connect('key_press_event', onkeypressed)
	plt.pause(0.01)
	
plt.gcf().canvas.set_window_title('Fractal Paint finished. Just close this window.')	
if 	CurrentIteration >= MaxIterations:
	plt.show()
