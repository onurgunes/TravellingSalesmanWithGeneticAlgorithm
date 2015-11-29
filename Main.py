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
               Gene("ankara", 20, 30),
               Gene("izmir", 0, 20),
               Gene("antalya", 0, 50),
               Gene("erzurum", 70, 30),
               Gene("trabzon", 50, 0),
               Gene("gaziantep", 20, 45),
               Gene("bursa", 10, 15),
               Gene("artvin", 0, 80)]

    # keep bests
    ELITISM = True
    ELITISM_OFFSET = 3
    
    # other constants
    GENERATION = 1000
    MUTATION_RATE = 0.05
    POPULATION_SIZE = 100
    CHROMOSOME_SIZE = len(cities) + 1

    population = []

    # evolve
    generation_count = 0
    while generation_count < GENERATION:
        
        generation_count += 1

main()