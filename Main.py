__author__ = 'OnurGunes'

from Chromosome import *
from Gene import *
from Fitness import *
from Population import *
import random

def main():
    # alphabet
    cities = [ Gene("istanbul", 0, 0),
               Gene("ankara", 20, 30),
               Gene("izmir", 0, 20),
               Gene("antalya", 0, 50),
               Gene("erzurum", 70, 30),
               Gene("trabzon", 50, 0),
               Gene("gaziantep", 20, 45),
               Gene("bursa", 10, 15),
               Gene("artvin", 0, 80)]

    GENERATION = 1000
    MUTATION = 0.05
    POPULATION_SIZE = 100
    CHROMOSOME_SIZE = len(cities) + 1

    generation_count = 0
    while generation_count < GENERATION:
        generation_count += 1

main()