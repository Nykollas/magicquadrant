#The purpose of this script is to  generate a graph called MQA after the user
#provides a list of coordinates x,y, list of labels for each coordinate
#list of labels for each quadrant, and the meaning for the vertical/horizontal axis.

import matplotlib.pyplot as plt

def normalize(x,y):
	max_x = max(x)
	max_y = max(y)
	x_n = y_n = []
	for k  in  x:
		x_n.append(k/max_x)
	for l in y:
		y_n.append(l/max_y)
	return x_n, y_n

fig, ax = plt.subplots()

label_quadrant0 = 'hello1'
label_quadrant1 = 'hello2'
label_quadrant2 = 'hello3'
label_quadrant3 = 'hello4'

txt = ['a','b','c','d','e',]

x = [1,2,3,4,5]
y = [1,2,3,4,5]

x_n, y_n = normalize(x,y)
ratio = 0.5/29

x0 = 0.25 - (len(label_quadrant0) * ratio) / 2
x1 = 0.75 - (len(label_quadrant1) * ratio) / 2
x2 = 0.25 - (len(label_quadrant2) * ratio) / 2
x3 = 0.75 - (len(label_quadrant3) * ratio) / 2
ax.set_ylim(-0.1,1.1)
ax.set_xlim(-0.1,1.1)


#ax.arrow(0,y,0,2*y)
#ax.arrow(x, -0.01, 2*x, -0.01)

ax.set_xticks([0.5])
ax.set_yticks([0.5])
ax.tick_params(length=0)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_ylabel('Awesome')
ax.set_xlabel('Funny')

#ax.yaxis.set_label_coords(0,0.155)
#ax.xaxis.set_label_coords(0.09,-0.01)

ax.annotate("", xy = (-0.015, 0), xycoords = "axes fraction", xytext = (-0.015,1), arrowprops = dict(arrowstyle = "<-", color = "b"))
ax.annotate("", xy = (0, -0.021), xycoords = "axes fraction", xytext = (1, -0.021), arrowprops = dict(arrowstyle = "<-", color = "b"))

ax.annotate(label_quadrant0, xy = (x0, 0.95), xycoords = "axes fraction", xytext = (x0,0.95))
ax.annotate(label_quadrant1, xy = (x1, 0.95), xycoords = "axes fraction", xytext = (x1, 0.95))
ax.annotate(label_quadrant2, xy = (x2, 0.02), xycoords = "axes fraction", xytext = (x2, 0.02))
ax.annotate(label_quadrant3, xy = (x3, 0.02), xycoords = "axes fraction", xytext = (x3, 0.02))

for i, t in enumerate(txt):
	ax.annotate('  '+t,(x_n[i],y_n[i]))

plt.grid()
plt.scatter(x_n,y_n)
plt.show()

