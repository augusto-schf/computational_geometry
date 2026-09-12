from src.geometry.Point2D import Point2D

def orientation(a : Point2D, b : Point2D, p : Point2D):
    '''Checa se um ponto esta a esquerda, direita ou em um
    segmento de reta orientado dada

    args:
        a (Point2D) : A primeira extremidade do segmento de reta
        b (Point2D) : A segunda extremidade do segmento de reta
        p (Point2D) : O ponto em questão a ser avaliado

    returns:
        int : Representando o seguinte:
            < 0 : esquerda
            = 0 : dentro
            > 0 : direita
            e o seu módulo representa a distância da reta
    '''

    ab = b - a
    ap = p - a

    result = ab[0] * ap[1] - ab[1] * ap[0]
    return result