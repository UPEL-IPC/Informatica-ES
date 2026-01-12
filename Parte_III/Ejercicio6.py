# Ejemplo 2.6

# Se requiere obtener el área de una figura. Para resolver este problema se puede 
# partir de que está formada por tres figuras: 2 triángulos rectángulos,
# con H como hipotenusa y R como uno de los catetos, que también es el radio
# de la otra figura, una semicircunferencia que forma la parte circular. 
# Programe el siguiente algoritmo en Python:

# ALGORITMO

# Variable      Descripción                             Tipo
# R             Base del triángulo rectángulo y radio   Real
# H             Hipotenusa del triángulo rectángulo     Real
# C             Cateto faltante                         Real
# AT            Área triangular                         Real
# AC            Área circular                           Real
# PI            El valor de 3.1416                      Real
# Area          Área de la figura                       Real
# SQRT          Indica obtener la raíz cuadrada         -

# Inicio
# Leer R, H
# Hacer C = SQRT (H * H - R * R)
# Hacer AT = 2 * (R * C) / 2
# Hacer AC = (PI * R * R) / 2
# Hacer Area = AT + AC
# Escribir Area
# Fin
