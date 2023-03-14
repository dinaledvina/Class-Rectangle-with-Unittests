
class Shape:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def set_position(self, x_value, y_value):
        self.__x = x_value
        self.__y = y_value
    
    def get_position(self):
        return (self.__x, self.__y)



my_shape = Shape()
my_shape.set_position(3, 4)
position = my_shape.get_position()
print(position)
 
