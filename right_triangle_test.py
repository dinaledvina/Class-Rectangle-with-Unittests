import unittest
from right_triangle import RightTriangle

class TestRightTriangle(unittest.TestCase):

	def test_perimeter(self):
	    t = RightTriangle(3, 4, 5)
	    self.assertEqual(t.perimeter(), 12)

	def test_area(self):
	    t = RightTriangle(3, 4, 5)
	    self.assertEqual(t.area(), 6.0)
		
	# test right triangle: setting sides length and asserting expected corners 
	def test_set_length_right(self):
	    t = RightTriangle(6, 8, 10)
		
	    self.assertEqual(t.a, 6)
	    self.assertEqual(t.b, 8)
	    self.assertEqual(t.c, 10)

	    expected_corners = ((0,0), (6,0), (0,8))
	    self.assertEqual(t.get_corners(), expected_corners)

		
	# test to assert this is not a right triangle: setting sides length, asserting expected corners, checking if trianglw is right
	def test_set_length(self):
            t = RightTriangle(20, 20, 20)
	    self.assertEqual(t.a, 20)
	    self.assertEqual(t.b, 20)
	    self.assertEqual(t.c, 20)
	    expected_corners = ((0,0), (20,0), (0,20))
	    self.assertEqual(t.get_corners(), expected_corners)
	    
	    if t.a ** 2 + t.b ** 2 != t.c ** 2:
	        raise ValueError("Not a right triangle")



if __name__ == '__main__':
    unittest.main()


