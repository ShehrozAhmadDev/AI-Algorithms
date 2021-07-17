# from collections import defaultdict
import random
import operator

class Genetic:
    def __init__(self,length):
        self.length = length # N for N queens problem
        self.attack = (self.length*self.length-1)/2 # No. of attacking pairs
        self.population = {} # population of solutions
        self.sample_size = 100 # population size
        self.mutation_rate = 0.1 # used for mutating solutions
        
        self.generate_sample(self.sample_size) # generating population
        self.fitness() # calculating fitness of population

        self.selection(self.attack/1.5) #selecting solutions with a score higher than 1.5 or less times the perfect score
        self.crossover() # crossing over parents of better fitness
        self.mutation()  # mutating population based on mutation rate
    
    def generate_sample(self,size):
        for i in range(size):
            individual = ""
            for j in range(self.length):
                individual += str(random.randint(1,self.length))
            self.population[individual] = 0

    def fitness(self):
        for individual in self.population.keys():
            count = self.attack
            for j in range(self.length):
                sum = int(individual[j])+j
                sum3 = int(individual[j])+ (self.length-j)
                for k in range(j+1,self.length):
                    # check = j
                    sum1 = int(individual[k])+k
                    sum2 = int(individual[k])+ (self.length-k)
                    if(individual[k]==individual[j] or sum==sum1 or sum3==sum2):
                        # print(individual," ",individual[j]," ",individual[k]," ",sum," ",sum1," ",sum2," ",sum3)
                        count-=1

                    # if(int(individual[j])+k==int(individual[k])):
                    #     count-=1
                    # if(j>0):
                    #     if(int(individual[j])-k==int(individual[k])):
                    #         count-=1
            self.population[individual] = count

    def fitness1(self,individual):
        count = self.attack
        for j in range(self.length):
            sum = int(individual[j])+j
            sum3 = int(individual[j])+ (self.length-j)
            for k in range(j+1,self.length):
                # check = j
                sum1 = int(individual[k])+k
                sum2 = int(individual[k])+ (self.length-k)
                if(individual[k]==individual[j] or sum==sum1 or sum3==sum2):
                    # print(individual," ",individual[j]," ",individual[k]," ",sum," ",sum1," ",sum2," ",sum3)
                    count-=1
        return count

    def selection(self,size):
        # sorting population by highest fitness score
        self.population = dict( sorted(self.population.items(), key=operator.itemgetter(1),reverse=True))
        new = {}
        for key,value in self.population.items():
            if(value>size):
                new[key] = value
        self.population = new
        # print('Dictionary in descending order by value : ',self.population)

    def crossover(self):
        parent = random.choice(list(self.population.keys()))
        parent1 = random.choice(list(self.population.keys()))
        for i in range(self.sample_size-len(self.population)):
            child = ""
            for j in range(self.length):
                if random.randint(0,1)>0.5:
                    child += parent[j]
                else:
                    child += parent1[j]
            self.population[child] = self.fitness1(child) # Have to calculate fitness of childs

    def mutation(self):
        new = {}
        for individual in self.population.keys():
            mutated=''
            for i in individual:
                if random.randint(0,1)<self.mutation_rate:
                    mutated+= str(random.randint(1,self.length))
                else:
                    mutated+=i
            new[mutated]= self.fitness1(mutated) # Have to calculate fitness of childs
        self.population = new

    def run(self):
        generation = 0
        while True:
            generation+=1
            if(generation%50==0 or generation==1):
                print("Generation ",generation)
                # print()
            try:
                solution = self.get_key(self.attack)
                score = self.population[solution]
                # if solution is not None:
                return solution,score
            except KeyError:
                # print(KeyError)
                continue
            finally:
                if generation>1000:
                    return None
                self.selection(self.attack/1.5) #selecting solutions with a score higher than 1.5 or less times the perfect score
                self.crossover() # crossing over parents of better fitness
                self.mutation()  # mutating population based on mutation rate

    def get_key(self,val):
        for key, value in self.population.items():
            if val == value:
                return key
        return "key doesn't exist"

def main():
    # size = int(input("Enter n for NxN Queens Board: "))
    # Genetic(size)
    print("Intializing Genetic Algortihm for N Queens Problem with n=7.")
    n=7
    algo = Genetic(n)
    solution = algo.run()
    print()
    print(solution[0]," is solution in string form with heuristic score of ",solution[1]," out of ", algo.attack)
    print()
    print("In chess Board form, the solution is represented as: ")
    board(solution[0],n)

def board(sol,length):
    
    print("_____________________")
    for i in range(0,length):
        for j in range(0,length):
            if int(sol[j])==i+1 and j==0:
                print("|",sol[j],"|",end="")
            elif int(sol[j])==i+1:
                print(sol[j],"|",end="")
            elif j==0:
                print("|  |",end="")
            else:
                print("  |",end="")
        print()
        print("_____________________")

main()