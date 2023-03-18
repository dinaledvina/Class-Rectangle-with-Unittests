from polygon import EquilateralPolygon

class Square(EquilateralPolygon):
    def __init__(self, side_length):
        super().__init__(4, side_length)
        self.corners = ((0,0), (self.side_length, 0), (self.side_length, self.side_length), (0, self.side_length))



    def set_length(self, length):
        self.side_length = length
        self.corners = ((0,0), (self.side_length, 0), (self.side_length, self.side_length), (0, self.side_length))


    def set_corners(self, corner1, corner2):
        (x1, y1), (x2, y2) = corner1, corner2
        self.length = x2 - x1
        self.length = y2 - y1
        self.corners = (corner1, (x2, y1), corner2, (x1, y2))



    def get_corners(self):
    	
    	return self.corners










