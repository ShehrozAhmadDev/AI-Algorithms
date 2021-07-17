#Shehroz Ahmad
#SP19-BCS-032

import random

# Create a random solution for cities so that we can optimize it using hill climbing algo
#Cities will be 0 to 3 and their distance is given in 2d list

def randomSolution(distance):
    cities = list(range(len(distance)))
    sol = []

    for i in range(len(distance)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        sol.append(randomCity)
        cities.remove(randomCity)

    return sol

 # Calculate the distance of solutions that we generated to find the best route length    

def routeLen(distance, sol):
    routeLen = 0
    for i in range(len(sol)):
        routeLen += distance[sol[i - 1]][sol[i]]
    return routeLen

# Find the neighbouring solutions that are possible if we only visit one city at time

def getNeighbours(sol):
    neighbours = []
    for i in range(len(sol)):
        for j in range(i + 1, len(sol)):
            neighbour = sol.copy()
            neighbour[i] = sol[j]
            neighbour[j] = sol[i]
            neighbours.append(neighbour)
    return neighbours


# To find best neighbour by calculating the route length of all neighbours

def getBestNeighbour(distance, neighbours):
    bestRoute = routeLen(distance, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRoute = routeLen(distance, neighbour)
        if currentRoute < bestRoute:
            bestRoute = currentRoute
            bestNeighbour = neighbour
    return bestNeighbour, bestRoute



def hillClimbing(distance):
    currentSolution = randomSolution(distance)
    print("Random generated sol is: ")
    print(currentSolution)
    currentRoute = routeLen(distance, currentSolution)    
    print("Route length: ")
    print(currentRoute)
    neighbours = getNeighbours(currentSolution)
    print("Generated neighbours are: ")
    print(neighbours)
    bestNeighbour, bestNeighbourRoute = getBestNeighbour(distance, neighbours)
    
#Compare best neighbour with current until we find the best solution until best neighbor route < current route
    while bestNeighbourRoute < currentRoute:
        currentSolution = bestNeighbour
        currentRoute = bestNeighbourRoute
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRoute = getBestNeighbour(distance, neighbours)

    return currentSolution, currentRoute


# Create 2d list to store distance between different cities

def main():
    distance = [
        [0, 160, 200, 120],
        [160, 0, 120, 200],
        [200, 120, 0, 160],
        [120, 200, 160, 0]
    ]

    bestSol, solRoute=hillClimbing(distance)
    print("Best Solution and its route will be:")
    print(bestSol, solRoute)
    
main()