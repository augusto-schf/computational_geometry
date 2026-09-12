import matplotlib.pyplot as plt

def plot_convex_hull(points, hull):
    x, y = zip(*[(p.x, p.y) for p in points])
    hx, hy = zip(*[(p.x, p.y) for p in hull] + [(hull[0].x, hull[0].y)])

    plt.scatter(x, y)

    for i, p in enumerate(points):
        plt.annotate(str(i), (p.x, p.y))

    plt.plot(hx, hy)

    for i, p in enumerate(hull):
        plt.annotate(str(i), (p.x, p.y))

    plt.axis("equal")
    plt.show()