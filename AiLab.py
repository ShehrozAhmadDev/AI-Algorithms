import random


# Create a solution for distance so that we can optimize it using hill climbing algo
def solution(distance):
    cities = list(range(len(distance)))
    solution = []

    for i in range(len(distance)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution



def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours



def routeLength(distance, solution):
    routeLength = 0
    for i in range(len(solution)):
        print(i-1)
        print(i)
        print(distance[solution[i - 1]][solution[i]])
        routeLength += distance[solution[i - 1]][solution[i]]
    return routeLength



# Create distance between 2 cities 
distance = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

print(solution(distance))
print(routeLength(distance, solution(distance)))
print(getNeighbours(solution(distance)))