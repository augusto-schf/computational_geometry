from src.geometry.Point2D import Point2D
from random import uniform

def random_points2D(n = 1, min_x = -100, max_x = 100, min_y = -100, max_y = 100):
    '''Gera aleatoriamente um número n de pontos, dentre o intervalo ([min_x, max_x], [min_y, max_y])

    args:
        n (int) : Especifica o número de pontos a serem gerados
        min_x (float) : O valor mínimo para o eixo X
        max_x (float) : O valor máximo para o eixo X
        min_y (float) : O valor mínimo para o eixo Y
        max_y (float) : O valor máximo para o eixo Y

    returns:
        list [Point2D] : Retorna uma lista com todos os pontos gerados
    '''
    points = []
    for i in range(n):
        points.append(Point2D(uniform(min_x, max_x), uniform(min_x, max_x)))
    return points

def orientation(a : Point2D, b : Point2D, p : Point2D):
    '''Checa se um ponto esta a esquerda, direita ou em um
    segmento de reta orientado dada

    args:
        a (Point2D) : A primeira extremidade do segmento de reta
        b (Point2D) : A segunda extremidade do segmento de reta
        p (Point2D) : O ponto em questão a ser avaliado

    returns:
        int : Representando o seguinte:
            > 0 : esquerda
            = 0 : dentro
            < 0 : direita
            e o seu módulo representa a distância da reta
    '''

    ab = b - a
    ap = p - a

    result = ab[0] * ap[1] - ab[1] * ap[0]
    return result