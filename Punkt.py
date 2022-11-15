import math  
class Point(object):
    
    COUNT = 0

    def __init__(self, x, y, z):
        
        self.X = x
        self.Y = y
        self.Z = z
    
   
    def distance(self):
        d = 0.0
        d = math.sqrt((self.X)**2 + ( - self.Y)**2 + ( - self.Z)**2)
        return d
        
    def wypisz(self):
        print(str(self.X)+","+str(self.Y)+","+str(self.Z))
