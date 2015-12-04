__author__ = 'OnurGunes'


import unittest
import sys
sys.path.append("..")
import Fitness

class Fitness_Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_fitness_result_correct_3_and_4_equal_5(self):
		self.assertEqual(True, False)

	def tearDown(self):
		pass
unittest.main()