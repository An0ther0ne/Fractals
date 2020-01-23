# Fractals
Few experiments with chaos, fractals, and Python...

## Serpinski Randomised Triangle

![Serpinski Randomised Triangle fig 1](img/Serpinski3.png)

You can zoom In and Out of this figure.

### Algorithm

1. Start with equilateral triangle and number its vertices 1,2,3
2. Plot a random dot point
3. Calculate a random integer number in range from 1 to number of triangle vertices (3)
4. Find a middle point from a random point (see para.2) to triangle vertice with number, calculated in para. 3, and plot a new dot point at them.
5. Store coordinates of dot point as new random instead of para 2.
6. Repeat steps 3-5 as many times as you wish. 

## Serpinski Randomised 4-point Rectangle

In the next figure shown rectangle, filled with similar chaos algorithm. But in this case we have four vertices and are looking for 1/3 of distance instead of middle.

![Serpinski Randomised Triangle fig 2](img/Serpinski41.png)

## Serpinski Randomised 8-point Rectangle
In this case we add middle point for each edge of previous rectangle. So our attractor now has total of 8 points.

![Serpinski Randomised Triangle fig 3](img/Serpinski42.png)

## Serpinski Pentagon

![Serpinski Pentagon fig 4](img/serp5.png)

## Serpinski Hexagon 

![Serpinski Hexagon fig 5](img/serp6.png)

## Serpinski Heptagon

![Serpinski Heptagon fig 6](img/serp7.png)

## Serpinski Octagon

![Serpinski Octagon fig 7](img/serp8.png)

## Requirements:

* Python
* NumPy
* MatPlotLib

## AUTHOR
   An0ther0ne
