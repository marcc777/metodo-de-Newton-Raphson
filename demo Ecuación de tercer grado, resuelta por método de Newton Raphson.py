# funcion f(x) = x^3 - 2x - 5
def f(x):
    return x**3 - 2*x - 5

# derivada de f(x) : f'(x) = 3x^2 - 2
def f_(x):
    return 3*x**2 - 2

# aproximacion inicial
a = 2

# nro de iteraciones
n = 10

for _ in range(n):
    # Calcular el siguiente valor de x usando el metodo de Newton-Raphson
    x = a - f(a) / f_(a)
    
    # Imprimir el valor de x en la iteracion actual
    print(f"valor aproximado: {x}")
    
    # Actualizar 'a' para la siguiente iteracion
    a = x



"""

Factores a considerar
 Si la aproximacion inicial esta cerca de la raiz, es mas probable que el metodo
 converga rapidamente a la solucion correcta.

 si la aproximacion inicial esta lejos de la raiz, el metodo puede converger lentamente
 o incluso divergir (no encontrar la solucion).

"""
