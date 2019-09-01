print("Este programa le dara las raices de Ecuaciones de segundo grado")

a = int(input("Deme el valor de a: "))

b = int(input("Deme el valor de b: "))

c = int(input("Deme el valor de c: "))

print("La ecuacion de segundo grado es esta: " + str(a) + "x^2 + " + str(b) +  "x + "  + str(c) +  " = 0 ")

if b**2 > (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))

if b**2 < (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("Las raices son: ")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
