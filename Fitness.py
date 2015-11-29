__author__ = 'OnurGunes'
import Chromosome
import math

class Fitness(object):
    """
        Operations about fitness function
    """

    def calculate_fitness(self , chromosome):
        """
        Calculate chromosome' fitness
        """
        
        distance = 0.0
        for index in range( len(chromosome.genes) - 1):
        	# calculate distance between i. gene and i+1. gene
        	distance += math.sqrt((chromosome.genes[index].latitude - chromosome.genes[index + 1].latitude)**2 
        		+ (chromosome.genes[index].longitude - chromosome.genes[index + 1].longitude)**2)
        return distance
        

