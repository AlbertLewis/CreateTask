import random
import math
import string

GENES = '''udlr'''

map = [ [0,0,0,1,'x'], 
        [1,1,0,0,0],        
        [0,1,1,0,1],
        ['s',0,0,0,1]]

target_path = 'rruuru'

class Individual(object):

    def __init__(self):
        self.chromosome = self.create_chromosome()

        # Find starting spot 's'
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 's':
                    self.positionX = j
                    self.positionY = i     

        self.fitness = self.calculate_fitness()


    # Returns the individual's fitness (closest distance to ending point)
    def calculate_fitness(self):

        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'x':
                    goalX = j
                    goalY = i

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

    ''' create a set of individuals
    loop through the set of individuals
    get the best and have them mate until they reach the end
    print out the best individual from each generation
    '''

    bruh1 = Individual()
    bruh2 = Individual()
    print("bruh1" + str(bruh1.chromosome))
    print("bruh2" + str(bruh2.chromosome))
    print("child" + str(mate(bruh1,bruh2)))

    xd = Individual()
    xd.mutate()
    print(xd.chromosome)
    print(xd.calculate_fitness())
    xd.move()
    print(xd.calculate_fitness())

    # Print map
    print('Map:')
    for i in range(len(map)):     
        for j in range(len(map[0])):
            print('[' + str(map[i][j]) + ']', end =' ')
        print()
    

if __name__ == "__main__":
    main()
