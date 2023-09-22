class Point:
    #konstruktor för klassen
    #kör först när vi skapar objekt av klassen
    def __init__(self, x = 0.0, y = 0.0):
        #def egenskaper x, y
        self.__x = x
        self.__y = y
    
    #medlemsfunktioner för arr seta och läsa egenskaper
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

#medlem funktioner
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def copy(self, p):
        self.__x = p.x
        self.__y = p.y

    def __str__(self):
        return str(self.__x)  + "," + str(self.__y)
    