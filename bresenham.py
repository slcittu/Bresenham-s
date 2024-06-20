import matplotlib.pyplot as plt

def draw_circle(xc, yc, x, y, points):
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))
    points.append((xc + y, yc + x))
    points.append((xc - y, yc + x))
    points.append((xc + y, yc - x))
    points.append((xc - y, yc - x))

def bresenham_circle(xc, yc, radius):
    x = 0
    y = radius
    p = 3 - 2 * radius
    points = []
    draw_circle(xc, yc, x, y, points)
    
    while y >= x:
        x += 1
        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6
        draw_circle(xc, yc, x, y, points)
    
    return points

def draw_circle(xc, yc, radius):
    points = bresenham_circle(xc, yc, radius)
    
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

