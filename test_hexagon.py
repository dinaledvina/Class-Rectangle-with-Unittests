import unittest
from e_polygon import EquilateralPolygon
import math
from epolygon_hexagon import Hexagon



class TestHexagon(unittest.TestCase):

  


    def test_area(self):
        hexagon = Hexagon(5)
        self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

    



if __name__ == '__main__':
    unittest.main()





