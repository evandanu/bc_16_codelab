import unittest
from tdd import solution

class TestSolution(unittest.Testcase):
	"""docstring for TestSolution"""
	def test_addition(self):
		self.assertTrue(solution(23,45,'+'),68)
    def test_subtraction(self):
		self.assertTrue(solution(45,23,'-'),22)
	def test_multiplication(self):
		self.assertTrue(solution(5,10,'*'),50)
	def test_division(self):
		self.assertTrue(solution(16,4,'/'),4)
	def test_modulus(self):
		self.assertTrue(solution(6,2,'%'),0)

if __name__ == '__main__':
	unittest.main()
