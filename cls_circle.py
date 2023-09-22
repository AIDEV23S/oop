from cls_point import Point
class Circle(Point):
    #Ärver klassen Point med dess egenskper och metoder
    def __init__(self, x=0.0, y=0.0, r=1.0):
        #Kör __init på Point (Klass vi ärver)
        super().__init__(x, y)
    #lägg till egenskap för raie r
        self.__r = r

    def set_r(self, r):
        self. r = r

    def get_r(self):
        return self. r

    def copy(self, c):
        self.r = c.r

    def __str__(self):
        return "Circle("+str(self.x)+", "+str(self.y)+", "+str(self._r)+")"

    r = property(get_r, set_r)