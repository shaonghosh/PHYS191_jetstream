import numpy as np

def geo_radius(m1, T):
    G = 6.67e-11
    omega = 2*3.14159/T
    return (G*m1/omega**2)**(1/3)

    """
    This function calculates the radius of the planet
    
    PARAMETERS:
    ----------
    m1 = mass of the first object, in this instance a planet
    T = time period of rotation of planet
    
    RETURNS:
    --------
    Function returns the calculation of the radius of the planet
    """

def visibility_cone_angle(r, h):
    return np.arccos(r/(r+h))

    """
    This function calculates the "boundaries" which the satellite can reach
    
    PARAMETERS:
    ----------
    r = radius of planet (Default = 6.4e6)
    h = distance
    
    RETURNS:
    --------
    Function returns the calculation of said boundary
    """


def get_great_circle_distance(l1, l2, phi1, phi2, R=6.4e6):
    dsigma = np.arccos((np.sin(phi1))*(np.sin(phi2))+(np.cos(phi1))*(np.cos(phi2))*(np.cos(l2-l1)))
    return dsigma*R

    """
    This function calculates the equation for the great circle distance, which computes the distance between two points on a planet
    
    PARAMETERS:
    ----------
    l1 = longitude of the position of the first point on the planet
    l2 = longitude of the position of the second point on the planet
    phi1 = latitude of the position of the first point on the planet
    phi2 = latitude of the position of the second point on the planet
    
    RETURNS:
    --------
    Function returns the calculation of said boundary
    """

def is_accessible(m, T, l2, phi2, r=6.4e6):

    """ 
    This function tells whether a point is accessible to the geostationary satelitte or not. It
    returns a boolean True/False.
    
    PARAMETERS: 
    -----------
    m = mass of the planet
    T = time period of rotation of planet
    r = radius of planet (Default = 6.4e6)
    l2 = longitude of the position of the point on the planet
    phi2 = latitude of the position of the point on the planet
    
    RETURNS:
    --------
    Function returns True if the point is accessible and False otherwise. 
    """
    
    r_geo = geo_radius(m, T)
    phi_horizon = visibility_cone_angle(r, r_geo-r)
    l_horizon = 0
    l1 = 0
    phi1 = 0
    horizon_radius = get_great_circle_distance(l1, l_horizon, phi1, phi_horizon, R=r)
    gc_dist = get_great_circle_distance(l1, l2, phi1, phi2, R=r) # The distance of the second point from the center.
    if gc_dist > horizon_radius:
        return (False, gc_dist)
    else:
        return (True, gc_dist)