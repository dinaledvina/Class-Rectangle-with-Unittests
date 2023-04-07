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
	
	
	def test_is_right_triangle(self):
	    with self.assertRaises(ValueError):
		t = RightTriangle(3, 4, 10)
		
	
	def test_is_right_triangle_with_two_sides(self):
	    t = RightTriangle(0, 0, 0) 
	    with self.assertRaises(ValueError):
	        self.assertAlmostEqual(t.is_right_triangle_with_two_sides(3, 7), 5.0)


	    
	    



if __name__ == '__main__':
    unittest.main()


