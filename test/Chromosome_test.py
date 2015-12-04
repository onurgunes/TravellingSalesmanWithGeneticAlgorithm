__author__ = 'OnurGunes'


import unittest
import sys
sys.path.append("..")
import Chromosome
 
class Chromosome_Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_mutation_change_a_gene(self):
		self.assertEqual(True, False)

	def test_crossing_over_change_one_or_more_genes(self):
		self.assertEqual(True, False)

	def test_generate_chromosome_generates_different_chromosome(self):
		self.assertEqual(True, False)

	def tearDown(self):
		pass
unittest.main()