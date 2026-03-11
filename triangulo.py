
def checkTriangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < b + c):
        if(a == b and a == c and b == c):
            return "Triangulo equilatero"
        elif (a == b) or (b == c) or (a == c):
            return "Triangulo isosceles"
        else:
            return "Triangulo escaleno"
    else:
        return "No es un triangulo"

