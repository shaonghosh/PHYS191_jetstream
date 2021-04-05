import numpy as np

def spherical_distribution(r=1.0, x0=0, y0=0, z0=0, N=1000):
    """Given a radius this function randomly distributes points
    inside a sphere of that radius.

    Parameters:
    -----------
    r = Radius of the shphere (default=1.0)
    (x0, y0, z0) = location of center of the sphere (default=(0, 0, 0))
    N = Total number of points to be distributed (default=1000)
    Output:
    -------
    A data file with three columns. Each row in that data file
    will have the coordinates of the points
    """
   
    x = (x0 - r) + 2*r*np.random.random(N)
    y = (y0 - r) + 2*r*np.random.random(N)
    z = (z0 - r) + 2*r*np.random.random(N)

    # Pruning things that fall outside the sphere
    keep = np.sqrt((x-x0)**2 + (y-y0)**2 + (z-z0)**2) <= r
    x = x[keep]
    y = y[keep]
    z = z[keep]

    return (x, y, z)


def create_mass_distribution(r=1.0, x0=0, y0=0, z0=0, N=1000):
    """Created the mass distribution based on user-supplied
    data
    """

    x_values = np.array([])
    y_values = np.array([])
    z_values = np.array([])
    while len(x_values) < N:
        x, y, z = spherical_distribution(r, x0, y0, z0, N)
        x_values = np.append(x_values, x)
        y_values = np.append(y_values, y)
        z_values = np.append(z_values, z)
    x_values = x_values[:N]
    y_values = y_values[:N]
    z_values = z_values[:N]
    output = np.vstack((x_values, y_values, z_values)).T

    np.savetxt("spherical_distribution.txt", output, fmt="%f\t%f\t%f")


def plotter(filename):
    """
    Plots the distribution of objects

    Parameters:
    -----------
    filename = name of the file which has the data to plot
    """
    import pylab as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = np.loadtxt(filename, unpack=True)
    ax.scatter(x, y, z, marker='.')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

