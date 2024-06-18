import matplotlib.pyplot as plt
import numpy as np


def plot_line(x1,y1,m1, side):  #side is left or right ( 'l' or 'r')
    if side == 'l':
        s,e= (x1-10), x1
    else:
        s,e= x1, (x1+10)
    x=np.linspace(s,e,21)
    y=[y1 + m1 * (i-x1) for i in x]
    plt.plot(x,y)

# two points and slope at that point
x1, y1 = (1, 6)
x2, y2 = (10, 30)
m1, m2 = (1, 2)


''' 
finding a cubic polynomial y = f(x) = ax^3 + bx^2 + cx + d
that somoothly connect both lines.
so here,  
f(x1) = y1
f(x2) = y2
f'(x1) = m1
f'(x2) = m2
which is solved by linear algebra using numpy library
'''
A = [
    [x1**3, x1**2, x1, 1],
    [x2**3, x2**2, x2, 1],
    [3 * x1**2, 2 * x1, 1, 0],
    [3 * x2**2, 2 * x2, 1, 0],
]


B = [y1, y2, m1, m2]

X = np.linalg.solve(A, B)

print("Solution:", X)

#plot 1 st line
plot_line(x1,y1,m1, 'l')

#plot 2 nd line
plot_line(x2,y2,m2, 'r')

#plot the smooth curve connector
x=np.linspace(x1,x2,100)
y= [np.polyval(X,i) for i in x]
plt.plot(x,y)

#show the plot
plt.show()
