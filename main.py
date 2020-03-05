import random
import string

GENES = '''udlr'''

map = [ [0,0,0,1,'x'], 
        [1,1,0,0,0],        
        [0,1,1,0,1],
        ['s',0,0,1,1]]

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
        print(goalX)
        print(goalY)
        difference = (goalX - self.positionX, goalY-self.positionY)
        print(difference)

    # Creates a chromosome
    def create_chromosome(self):  
        chromosome = []

        while len(chromosome) != len(target_path):
            chromosome += random.choice(GENES)

        return chromosome

    # def mate(self):

        
    # Chance to add random gene into chromosome
    def mutate(self):
        self.chromosome[random.randint(0, len(self.chromosome)-1)] = random.choice(GENES)


    def move(self):

        # for movement in range(len(chromosome)):
        #     if movement == 'u':
        #         self.positiony -= 1
        #     if movement == 'd':
        #         self.positiony += 1
        #     if movement == 'l':
        #         self.positionx -= 1
        #     if movement == 'r':
        #         self.positionx += 1

        return "s"

def main():

    xd = Individual()
    xd.mutate()

    # Print map
    print('Map:')
    for i in range(len(map)):     
        for j in range(len(map[0])):
            print('[' + str(map[i][j]) + ']', end =' ')
        print()
    

if __name__ == "__main__":
    main()
    