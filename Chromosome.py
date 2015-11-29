__author__ = 'OnurGunes'

import random
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

def mutate(chromosome):
	"""
	mutation operation : swap two genes in chromosome
	"""
	
