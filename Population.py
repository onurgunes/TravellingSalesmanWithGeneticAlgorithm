__author__ = 'OnurGunes'

import Chromosome

class Population(object):

	population = []
	gene = []
	
	def __init__(self, gene):
		"""
		"""
		self.gene = gene

	def get_fittest(self):
		"""
		"""

	def add_individual(self, chromosome):
		"""
		add individual to population
		"""
		self.population.append(chromosome)
		
	def delete_individual(self, index):
		"""
		deleete individual from population
		"""
		self.population.remove(chromosome)

	def populate(self, limit):
		"""
		populate population with new chromosomes
		"""
		for i in xrange(limit):
			self.population.append(Chromosome.generate_chromosome(self.gene))

	def order_by_fittest(self):
		"""
		"""

	def print_population(self):
		for genes in self.population:
			for gene in genes:
				print gene.name
			print "------------"

	def delete_unfit_individuals(self, limit):
		for index in xrange(limit, len(self.population)):
			del self.population[index]