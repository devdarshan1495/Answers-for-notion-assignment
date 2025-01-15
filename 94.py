class Shape:
    def draw(self):
        print("Drawing a shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle.")

shapes = [Shape(), Circle(), Triangle()]
for shape in shapes:
    shape.draw()
