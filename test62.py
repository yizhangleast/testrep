import math

def linepoints(x1,y1,x2,y2):
    width = x2-x1
    height = y2-y1
    d = max(abs(width), abs(height))
    linepoint = []
    for i in range(d+1):
        x = math.floor(i*1.0/d*width+x1+0.5)
        y = math.floor(i*1.0/d*height+y1+0.5)
        linepoint.append((x,y))
    return linepoint

x1=5
x2=1
y1=10
y2=15
print (linepoints(x1,y1,x2,y2))
