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

    def squared_length(self):
        '''Retorna o comprimento do vetor ao quadrado

        returns:
            float : Valor do comprimento ao quadrado, minimizando
            o custo computacional da raiz quadrada
        '''
        # mais eficiente computacionalmente e muito útil
        return self.x**2 + self.y**2
    def distance_to(self,other):
        '''Retorna a distância euclidiana com outro ponto

        args:
            other (Point2D) : Outro vetor a ser utilizado
        
        returns:
            float : Representa a distância euclidiana entre o p1
            e o p2
        '''
        return Point2D.distance(self,other)
    def distance_to_squared(self,other):
        '''Retorna a distância euclidiana ao quadrado com outro ponto

        args:
            other (Point2D) : Outro vetor a ser utilizado
        
        returns:
            float : Representa a distância euclidiana entre o p1
            e o p2 ao quadrado, para maior eficiência computacional
        '''
        return Point2D.distance_squared(self,other)
    def to_polar_coord(self):
        '''Converte e retorna o ponto/vetor em coordenadas polares

        returns:
            Point2D (r, theta) : Um ponto/vetor 2D que representa
            o comprimento e o ângulo respectivamente.
        '''
        return (len(self), arctan2(self.y,self.x))
    
    # métodos estáticos que funcionam sem instância
    @staticmethod
    def distance(p1,p2):
        '''Determina a distância euclidiana entre dois pontos

        args:
            p1 (Point2D) : Primeiro ponto
            p2 (Point2D) : Segundo ponto

        returns:
            float : Equivale a distância entre os dois pontos no plano
        '''
        return Point2D.distance_squared(p1,p2)
    @staticmethod
    def distance_squared(p1,p2): # mais eficiente
        '''Determina a distância euclidiana ao quadrado entre dois pontos

        args:
            p1 (Point2D) : Primeiro ponto
            p2 (Point2D) : Segundo ponto

        returns:
            float : Equivale a distância ao quadrado entre os dois pontos
            no plano. É mais eficiente que a distância convencional pois
            não processa a raiz quadrada do valor
        '''
        return (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    @staticmethod
    def cross(v,u):
        '''Resolve o produto vetorial entre dois pontos/vetores 2D

        args:
            v (Point2D) : Primeiro vetor
            u (Point2D) : Segundo vetor

        returns:
            float : Transforma os vetores 2D em 3D, resolve o produto
            vetorial e retorna o terceiro valor, representando sentido
        '''
        # retorna o equivalente ao terceiro componente caso fosse no R^3
        return v.x*u.y - v.y*u.x
    @staticmethod
    def dot(v,u):
        '''Resolve o produto escalar entre dois vetores

        args:
            u (Point2D) : Primeiro ponto
            v (Point2D) : Segundo ponto

        returns:
            float : O valor do produto escalar entre os dois vetores
        '''
        return v.x*u.x+v.y*u.y