import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()
        
        shape.x = 10
        shape.y = 10
        
        shape.set_position(shape.x, shape.y)
        
        self.assertEqual(shape.get_position(), (shape.x, shape.y))

        
        
        

