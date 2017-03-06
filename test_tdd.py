import unittest
from tdd import solution

class TestSolution(unittest.Testcase):
	"""docstring for TestSolution"""
	def test_addition(self):
		self.assertTrue(solution(23,45,'+'),68)


if __name__ == '__main__':
	unittest.main()

		