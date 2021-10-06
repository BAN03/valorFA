from math import sqrt as raiz
print("Varianza\n"
    + "1. Desordenada_1\n"
    + "2. Desordenada_2\n"
    + "3. Ordenada_1\n"
    + "4. Ordenada_2\n")
opcion = int(input("Opcion: "))
n = int(input("Total de valores (n): "))
x = []
s = []
y = []
for i in range(n):
    x.append(float(input(f"Valor de x {i+1}: ")))
promedio = (sum(x))/n
promedio2 = promedio**2
def Desordenada_1(s,x):
    for i in range(n):
        s.append(((x[i] - promedio)**2))
    s = (sum(s))/n
    s = round(s,2)
    print("S2: ", s)
    print("S: ", raiz(s))

def Desordenada_2(s,x):
    for i in range(n):
        s.append(x[i]**2)

    s = (sum(s))/n
    s = s - promedio2
    s = round(s,2)
    print("S2: ", s)
    print("S: ", raiz(s))

def Ordenada_1(s,x,y):
    total=sum(x)
    for i in range(n):
        y.append(float(input(f"Marca de clase {i+1}: ")))
    promedio = (sum(y))/n
    for i in range(n):
        s.append(((y[i]-promedio)**2)*x[i])
    s = (sum(s))/total
    s = round(s,2)
    print("S2: ", s)
    print("S: ", raiz(s))

def Ordenada_2(s,x,y):
    total=sum(x)
    for i in range(n):
        y.append(float(input(f"Marca de clase {i+1}: ")))
    promedio = (sum(y))/n
    for i in range(n):
        s.append((y[i]**2)*x[i])
    s = (sum(s))/total
    s = round(s,2)
    print("S2: ", s)
    print("S: ", raiz(s))

if opcion == 1:
    Desordenada_1(s,x)
elif opcion == 2:
    Desordenada_2(s,x)
elif opcion == 3:
    Ordenada_1(s,x,y)
elif opcion == 4:
    Ordenada_2(s,x,y)
else:
    print("Opcion incorrecta")
