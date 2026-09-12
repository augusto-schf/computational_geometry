from numpy import arctan2

class Point2D:
    def __init__ (self, x : float, y : float):
        self.x, self.y = x, y

    # métodos especiais para definir operadores básicos
    def __add__ (self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point2D(self.x * other, self.y * other)
    def __rmul__(self, other):
        return self * other
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    def __len__(self):
        return self.squared_length() ** 0.5
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    # mais eficiente computacionalmente e muito útil
    def squared_length(self):
        return self.x**2 + self.y**2
    def distance_to(self,other):
        return Point2D.distance(self,other)
    def distance_to_squared(self,other):
        return Point2D.distance_squared(self,other)
    def to_polar_coord(self):
        return (len(self), arctan2(self.y,self.x))
    
    # métodos estáticos que funcionam sem instância
    @staticmethod
    def distance(p1,p2):
        return Point2D.distance_squared(p1,p2)
    @staticmethod
    def distance_squared(p1,p2): # mais eficiente
        return (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    @staticmethod
    def cross(v,u): 
        # retorna o equivalente ao terceiro componente caso fosse no R^3
        return v.x*u.y - v.y*u.x
    @staticmethod
    def dot(v,u):
        return v.x*u.x+v.y*u.y