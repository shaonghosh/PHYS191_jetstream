# PHYS 191 Final Project 
# Group members: Marina Saburova, Harold Ortega, Ana Caicedo, Kelsey Nyman, Syrii Lewis
# Group 9 
# Due Date: 12/15/20 @ 11:59pm

# This program finds the total time for a collision of a sequence of masses
# and finds the ordering of masses that have the fastest total time
# -----------------------------------------------------------------------------

import math
import itertools

def main(): 
    
    # Masses are scanned in from user into list (array)
    print("Enter all mass values, in order (SI Units): ")
    masses = [float(x) for x in input().split()] 

    # Variables are scanned in from user
    springConstant = float(input("Enter spring constant: "))
    springDistance = float(input("Enter distance spring is compressed: "))
    distance = float(input("Enter distance between objects: "))
    print("All data entered. \n")
    
    # Calculates the initial velocity of the first object
    initVelocity = initialVelocity(springConstant, masses[0], springDistance)

    # Calls method to find total time with given values, prints result
    totalTime = calculateTotalTime(masses, distance, initVelocity)
    print("Total time for current order: ", round(totalTime, 2))
    
    # Calls method to find fastest order of collisions, prints result
    fastestOrder = fastestCollision(masses, distance, initVelocity)
    print("The fastest permutation is: ", fastestOrder)
    
    # Calls to method to find total time with the new order of masses, prints
    fastestOrderTime = calculateTotalTime(fastestOrder, distance, 
        initialVelocity(springConstant, fastestOrder[0], springDistance))
    print("The time for the fastest permutation is: ", round(fastestOrderTime, 2))
    

# Finds initial velocity provided by the spring
def initialVelocity (springConstant, mass1, springDistance): 
    return (springDistance * math.sqrt(springConstant / mass1))

# Finds the resulting velocities from collisions
def calculateVelocity (mass1, mass2, velocityInitial):
	return ((2 * mass1) / (mass1 + mass2) * velocityInitial) 

# Calculates time to travel distance using given velocity
def calculateTime (distance, velocity): 
    return (distance / velocity)

# Calculates the total time for all masses
def calculateTotalTime (masses, distance, velocity):
    time = 0.0
    time += calculateTime(distance, velocity) # Calculates initial time (from spring)
        
    # Calculates total time
    for i in range (len(masses) - 1):
        # Finds the velocity of object that was hit
        velocity = calculateVelocity(masses[i], masses[i+1], velocity)  
        # Calculates time, using updated velocity
        time += calculateTime(distance, velocity)   
    return time

# Finds the fastest orientation
def fastestCollision (masses, distance, velocity): 
    totalTime = calculateTotalTime(masses, distance, velocity)

    permutations = list(itertools.permutations(masses))
    totalTimeNew = 0.0 
    for x in permutations: 
        totalTimeNew = calculateTotalTime(x, distance, velocity)
        if (totalTimeNew < totalTime): 
            masses = x 
            totalTime = totalTimeNew
    return masses  

# Checks if the program is working 
def sanityCheck(): 
    print("Running sanity check...")
    print("Enter all SAME masses: ")
    equalMasses = [float(x) for x in input().split()] 
    
    distance = 10   # Set distance for testing purposes
    # Default spring constant and distance for testing purposes 
    initVelocity = initialVelocity(10, equalMasses[0], 1)
    
    # Expected time calculation: as if there were no other blocks
    expectedTime = calculateTime(distance, initVelocity) * len(equalMasses) 
    print("Expected time: ", round(expectedTime, 2))
    
    # Actyal time calculation, as per program
    totalTime = calculateTotalTime(equalMasses, distance, initVelocity)
    print("Calculated time: ", round(totalTime, 2))
    
    # Prints results
    if (totalTime == expectedTime):
        print("Program works as expected.")
    else:
        print("Values do no equal. Something is wrong.")
        
    print("---------------------------------------------------------")