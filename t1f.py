import numpy as np
#import matplotlib.pyplot as plt
import random
import sys

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Point({},{})".format(self.x, self.y)


def Distancia(a, b, c):
	ABx = b.x - a.x
	ABy = b.y - a.y
	num = ABx * (a.y - c.y) - ABy * (a.x - c.x)
	return abs(num)

def location(a, b, p):
	loc = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)
	if loc > 0:
		return 1
	else:
		return -1


def qhull(point):
	arr_sol = []
	if len(point) < 3:
		return point
	A = min(point, key=lambda t : t.x)
	B = max(point, key=lambda t : t.x)
	arr_sol.append(A)
	arr_sol.append(B)#arr_sol+=B
	point.remove(A)
	point.remove(B)

	Izquierda = []
	Derecha = []

	for i in range(len(point)):
		p = point[i]
		if location(A, B, p) == -1:
			Izquierda.append(p)
		else:
			Derecha.append(p)
	if Izquierda==[] or Derecha ==[]:
		print("peor caso, probar otro arreglo")
		return
	hullset(A, B, Derecha, arr_sol)
	hullset(B, A, Izquierda, arr_sol)

	return arr_sol


def hullset(A, B, part, covex):
	pos = covex.index(B)
	if len(part) == 0:
		return

	if len(part) == 1:
		p = part[0]
		part.remove(p)
		covex.insert(pos, p)
		return

	dist = 0
	fpoint = -1

	for i in range(len(part)):
		distancia = Distancia(A, B, part[i])
		if distancia > dist:
			dis = distancia
			fpoint = i

	P = part[fpoint]
	part.remove(P)
	covex.append(P)

	leftAP = []
	for i in range(len(part)):
		m = part[i]
		if location(A, P, m) == 1:
			leftAP.append(m)

	leftPB = []

	for i in range(len(part)):
		m = part[i]
		if location(P, B, m) == 1:
			leftPB.append(m)
	
	hullset(A, P, leftAP, covex)
	hullset(P, B, leftPB, covex)





points_rand = np.random.rand(500000,2)
x_rand = points_rand[:, 0]
y_rand = points_rand[:, 1]

arr = [Point(-1,0.5),Point(2,0.5),Point(-1.5,0.5),Point(2.5,0.5)]

for i in range(len(x_rand)):
	arr.append(Point(x_rand[i], y_rand[i]))
	
'''
for i in range (10000+2): #n×2 es la cantidad de enteros en el arreglo, si esq el rango es desde negativos a positivos
		arr.append(Point(random.randint(0,9000000),random.randint(0,9000000)))
'''
#print(arr)
#a0=Point(1,1)
#a1=Point(2,2)
#a2=Point(4,1)
#a3=Point(4,3)
#a4=Point(1,3)
#a5=Point(3,4)
#arr=[a0,a1,a2,a3,a4,a5]
#quick = qhull(arr)
#print("Done")

if __name__=='__main__':
	from timeit import Timer
 
	samples = 1
	t = Timer("qhull(arr)", "from __main__ import qhull, arr")
	took = t.timeit(samples)/samples # average of 10 executions
	print( "qhull for {} integers took {} secs".format(len(arr), took))

#print(quick)
#plt.plot(x_rand, y_rand, 'o')
#plt.show()

