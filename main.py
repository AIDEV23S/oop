#Läsa in klassdef för klassen Point
from cls_point import Point

#Skapa två point objekt
p1 = Point()
p2 = Point()

#Flyta point p1 till koord. 10,20
p1.move(10.0,20.0)

#Flyta point p2 till koord. -5.0,-5.0
p2.move(-5.0,-5.0)

#Skriv ut x-koord på punkt p1
print(p1.get_y())

#Kopiera punkt p1 till punkt p2
p2.copy(p1)

#Skriv ut koord på punkt p2
print(p2)