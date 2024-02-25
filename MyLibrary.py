class Circle():
    # Create our circle constructor
    def __init__(self):
        # Define the variables
        self.x = 0
        self.y = 0
        self.r = 0

    # Method to return the circumference
    def getCircumference(self):
        cir = 2 * 3.14 * self.r
        return cir
    
    def setR(self, newR):
        self.r = newR

class Sphere(Circle):
    def __init__(self):
        self.z = 0
        super().__init__()