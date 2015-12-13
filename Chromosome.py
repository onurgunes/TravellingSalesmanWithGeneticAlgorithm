__author__ = 'OnurGunes'

from random import random
from random import randint
from random import shuffle
from Fitness import *

class Chromosome(object):
	""" represent individual """

	fitness = 0
	genes = []

	def __init__(self, genes):
		self.genes = genes

	def get_fitness(self):
		"""
		get fitness value of chromosome
		"""
		self.fitness = Fitness().calculate_fitness(self)
		return self.fitness

def generate_chromosome(genes):
	"""
	generate new chromosomes
	"""
	temp = genes[1:]
	shuffle(temp)

	new_gene = []
	new_gene.append(genes[0])
	for i in range(len(temp)):
		new_gene.append(temp[i])

	return new_gene

def crossover(chromosome):
	"""
	crossover operation : swap a part of chromosome1 with a part of chromosome2
	Note: In the TSA problem, traveller must visit each city once but, with crossing over, it is hard to provide.
	Therefore, I preferred to use mutating operation three times instead of classic crossing over operation.
	"""
	return mutate(mutate(mutate(chromosome)))

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
