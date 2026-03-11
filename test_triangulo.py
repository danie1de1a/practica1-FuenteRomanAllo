import pytest
from triangulo import checktriangle

def test_case1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_case2_equilatero():
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"

def test_case3_isosceles():
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"

def test_case4_no():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_case5_no():
    assert checktriangle(8, 2, 4) == "No es un triangulo"

def test_case6_isosceles_a():
    # Caso 6: Triángulo isósceles a
    assert checktriangle(5, 3, 3) == "Triangulo isosceles"

def test_case7_isosceles_b():
    # Caso 7: Triángulo isósceles b
    assert checktriangle(3, 5, 3) == "Triangulo isosceles"

def test_case8_negativo_a():
    # Caso 8: No es un triángulo (negativo a)
    assert checktriangle(-1, 5, 6) == "No es un triangulo"

def test_case9_negativo_b():
    # Caso 9: No es un triángulo (negativo b)
    assert checktriangle(5, -1, 6) == "No es un triangulo"

def test_case10_negativo_c():
    # Caso 10: No es un triángulo (negativo c)
    assert checktriangle(5, 6, -1) == "No es un triangulo"

def test_case11_suma_igual_tercero():
    # Caso 11: No es un triángulo (suma de dos lados igual al tercero)
    assert checktriangle(2, 3, 5) == "No es un triangulo"