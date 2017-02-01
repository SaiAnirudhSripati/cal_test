import unittest

class test_cal(unittest.TestCase):
	def test_cal_functions(self):
		cal=Calculator(self)
		result=cal.add(2,2)
		self.assertEqual(4,result)
		result=cal.mul(2,3)
		self.assertEqual(6,result)
		result=cal.sub(4,2)
		self.assertEqual(2,result)

if __name__=='__main__':
	unittest.main()

			

