__author__ = 'OnurGunes'

from random import randint
from Fitness import *

class Chromosome(object):
	""" represent individual """

	fitness = 0
	genes = []
	
	def __init__(self, genes):
		"""
		"""
		self.genes = genes

	def get_fitness(self):
		fitness = Fitness().calculate_fitness(self)
		return fitness

def generate_chromosome(genes):
    """
    generate new chromosomes
    """

def crossover(chromosome1, chromosome2):
	"""
	crossover operation : swap a part of chromosome1 with a part of chromosome2
	"""
	randint(0, len(chromosome1.genes))

def mutate(chromosome):
	"""
	mutation operation : swap two genes in chromosome
	"""
	mutation_point_1 = 0
	mutation_point_2 = 0

	while mutation_point_1 == mutation_point_2:
		mutation_point_1 = randint(1, len(chromosome.genes) - 1)
		mutation_point_2 = randint(1, len(chromosome.genes) - 1)
		
	temp = chromosome.genes[mutation_point_1]
	chromosome.genes[mutation_point_1] = chromosome.genes[mutation_point_2]
	chromosome.genes[mutation_point_2] = temp
	
	return chromosome
