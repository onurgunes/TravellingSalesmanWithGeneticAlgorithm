__author__ = 'OnurGunes'

from Chromosome import *
from Gene import *
from Fitness import *
from Population import *
import random

def main():
    
    # alphabet
    # first item of cities array is start and end point.
    cities = [ Gene("istanbul", 0, 0),
               Gene("ankara", 0, 1),
               Gene("izmir", 0, 2),
               Gene("antalya", 0, 3),
               Gene("erzurum", 0, 4),
               Gene("trabzon", 0, 5),
               Gene("gaziantep", 0, 6),
               Gene("bursa", 0, 7),
               Gene("artvin", 0, 8)]

    # keep bests
    ELITISM = True
    ELITISM_OFFSET = 3
    
    # other constants
    GENERATION = 50
    MUTATION_RATE = 0.05
    POPULATION_SIZE = 50
    CHROMOSOME_SIZE = len(cities) + 1

    # create population instance
    traveling_salesman = Population(cities)
    
    # create initial population
    traveling_salesman.populate(POPULATION_SIZE)

    # evolve
    generation_count = 0
    while generation_count < GENERATION:
      
      index = 0
      new_generation = []
      
      for individual in traveling_salesman.population:
        
        new_individual = crossover(individual)
        
        if random.uniform(0.0, 100.0) <= MUTATION_RATE:
          mutate(new_individual)
        
        new_generation.append(new_individual)

        index += 1
      
      # append new individuals to the population
      for x in new_generation:
        traveling_salesman.add_individual(x)

      traveling_salesman.order_by_fit()
      traveling_salesman.delete_unfit_individuals(POPULATION_SIZE)

      generation_count += 1
      print traveling_salesman.get_fittest().fitness

    best = traveling_salesman.get_fittest()

    for i in best.genes:
      print i.name

    print "Shortest path : " + str(best.fitness)
main()