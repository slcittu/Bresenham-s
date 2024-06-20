import matplotlib.pyplot as plt

def plot_circl(xc, yc, x, y, points):
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
    plot_circl(xc, yc, x, y, points)
    
    while y >= x:
        x += 1
        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6
        plot_circl(xc, yc, x, y, points)
    
    return points

def draw_circle(xc, yc, radius):
    points = bresenham_circle(xc, yc, radius)
    
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def read_input():
    try:
        xc = int(input("Enter the x-coordinate of the center: "))
        yc = int(input("Enter the y-coordinate of the center: "))
        radius = int(input("Enter the radius of the circle: "))
        return xc, yc, radius
    except ValueError:
        print("Invalid input. Please enter integers for the coordinates and radius.")
        return None, None, None
    
def main():
    xc, yc, radius = read_input()
    if xc is not None and yc is not None and radius is not None:
        draw_circle(xc, yc, radius)

if __name__ == "__main__":
    main()


