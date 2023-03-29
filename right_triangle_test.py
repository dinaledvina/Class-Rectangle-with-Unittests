import unittest
from right_triangle import RightTriangle

class TestRightTriangle(unittest.TestCase):

	def test_perimeter(self):
		t = RightTriangle(3, 4, 5)
		self.assertEqual(t.perimeter(), 12)

	def test_area(self):
		t = RightTriangle(3, 4, 5)
		self.assertEqual(t.area(), 6.0)

	def test_set_corners(self):
		t = RightTriangle(4, 3, 5)
		t.set_corners((0,0), (4,0), (0, 3))
		self.assertEqual(t.get_corners(), ((0,0), (4,0), (0, 3)))
		self.assertEqual(t.a, 4)
		self.assertEqual(t.b, 3)
		self.assertEqual(t.c, 5)

	def test_set_length(self):
		t = RightTriangle(6, 8, 10)
		self.assertEqual(t.a, 6)
		self.assertEqual(t.b, 8)
		self.assertEqual(t.c, 10)

		expected_corners = ((0,0), (6,0), (0,8))
		self.assertEqual(t.get_corners(), expected_corners)



if __name__ == '__main__':
    unittest.main()

