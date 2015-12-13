__author__ = 'OnurGunes'

import Chromosome

class Population(object):

	population = []
	gene = []
	
	def __init__(self, gene):
		self.gene = gene

	def get_fittest(self):
		"""
		get fittest individual
		"""
		self.order_by_fit()
		return self.population[0]

	def add_individual(self, chromosome):
		"""
		add individual to population
		"""
		self.population.append(chromosome)
		
	def delete_individual(self, chromosome):
		"""
		delete individual from population
		"""
		self.population.remove(chromosome)

	def populate(self, limit):
		"""
		populate population with new chromosomes
		"""
		for i in xrange(limit):
			self.population.append(Chromosome.generate_chromosome(self.gene))

	def order_by_fit(self):
		"""
		sort individuals order by fit
		"""
		self.population.sort( key= lambda x: x.fitness , reverse=False)

	def print_population(self):
		for chromosome in self.population:
			for gene in chromosome.genes:
				print gene.name
			print "------------"

	def delete_unfit_individuals(self, limit):
		self.order_by_fit()
		for index in xrange(limit, len(self.population)):
			del self.population[index]