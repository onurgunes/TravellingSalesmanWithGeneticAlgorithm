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
        last_gene_index = len(chromosome.genes) - 1
        distance = 0.0
        for index in range(last_gene_index):
        	# calculate distance between i. gene and i+1. gene
        	distance += math.sqrt((chromosome.genes[index].latitude - chromosome.genes[index + 1].latitude)**2 
        		+ (chromosome.genes[index].longitude - chromosome.genes[index + 1].longitude)**2)
        distance += math.sqrt((chromosome.genes[0].latitude - chromosome.genes[last_gene_index].latitude)**2 
                + (chromosome.genes[0].longitude - chromosome.genes[last_gene_index].longitude)**2)
        return distance