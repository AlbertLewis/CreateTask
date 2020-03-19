import random
import math
import string

GENES = '''udlr'''

population_size = 50

map = [ [0,0,0,1,'x'], 
        [1,1,0,0,0],        
        [0,1,1,0,1],
        ['s',0,0,0,1]]

target_path = 'rrruuru'

class Individual(object):

    def __init__(self, chromosome = 'empty'):

        self.chromosome = list(chromosome)
        if chromosome == 'empty':
            self.chromosome = self.create_chromosome()

        # Find starting spot "s"
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 's':
                    self.positionX = j
                    self.positionY = i     
        self.fitness = 10

    # Returns the individual's fitness (closest distance to ending point)
    def calculate_fitness(self):

        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'x':
                    
                    goalY = i
                    goalX = j

        difference = math.sqrt((goalX - self.positionX)**2 + (goalY-self.positionY)**2)
        return difference

    # Creates a chromosome
    def create_chromosome(self):  
        chromosome = []

        while len(chromosome) != len(target_path):
            chromosome += random.choice(GENES)

        return chromosome
      
    # Chance to add random gene into chromosome
    def mutate(self):
        self.chromosome[random.randint(0, len(self.chromosome)-1)] = random.choice(GENES)

    def move(self):

        map[self.positionY][self.positionX] = 0

        for movement in self.chromosome:
            print('Position x: ' + str(self.positionX))
            print('Position y: ' + str(self.positionY))
            print()

            if 0 <= self.positionX <= 4 and 0 <= self.positionY <= 3:  
                moveX = self.positionX
                moveY = self.positionY

                if movement == 'u':
                    moveY -= 1
                elif movement == 'd':
                    moveY += 1
                elif movement == 'l':
                    moveX -= 1
                elif movement == 'r':
                    moveX += 1

                if 0 <= moveX <= 4 and 0 <= moveY <= 3 and map[moveY][moveX] != 1:
                    self.positionX = moveX
                    self.positionY = moveY

        map[self.positionY][self.positionX] = 's'


def mate(individual1, individual2):

    child_chromosome = []

    for gene_index in range(len(individual1.chromosome)):
        if random.randint(1,100) <= 50:
            child_chromosome.append(individual1.chromosome[gene_index])
        else:
            child_chromosome.append(individual2.chromosome[gene_index])

    return child_chromosome

def main():

    # create initial population
    population = []

    for _ in range(population_size):
        population.append(Individual())

    for individual in population:
        individual.move()
    
    population.sort(key=lambda individual: individual.fitness)
    
    print("Generation 0")
    for individual in population:
            print(individual.fitness)


    # while the best member of the population does not reach the goal, keep mating
    gen = 0
    while population[0].fitness != 0:
     
        gen += 1
        # if gen > 3:
        #     break

        print('Generation', gen)
        new_population = []

        for top_individual in population[0:int(population_size/10)]:  
                new_population.append(top_individual)

        while len(new_population) <= population_size:
            new_population.append(Individual(mate(population[0],population[1])))

        for individual in new_population:

            if random.randint(1,10) <= 2: # mutation chance 30%
                individual.mutate()

            individual.move()
            individual.fitness = individual.calculate_fitness()

        population = new_population
        population.sort(key=lambda individual: individual.fitness)

        for individual in population:
            print(individual.fitness)

    print('done')
    print('winning fitness', population[0].fitness)
    print('winning chromosome', population[0].chromosome)
    
    print('Map:')
    for i in range(len(map)):     
        for j in range(len(map[0])):
            print('[' + str(map[i][j]) + ']', end =' ')
        print()
    

if __name__ == "__main__":
    main()
