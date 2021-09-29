from math import log
arango = []
n = []
h = []

def tabular():
    g = 0
    intervalo = round(1 + (3.3 * log(total,10)))
    minimo = min(arango)
    maximo = max(arango)
    rango = round(maximo - minimo,2)
    c = round(rango/intervalo,2)
    interv = round(rango/c)
    print("\n valor minimo: " + str(minimo))
    print(" valor maximo: " + str(maximo))
    print(" rango: " + str(rango))
    print(" intervalo = " + str(intervalo))
    print(" c = " + str(c) + "\n")

    for l in range(interv):
        y = round(minimo+c*(l+1),2)
        ye= round(minimo+c*(l),2)
        if l == 0:
            n.append(str(l+1) + ": " + str(minimo) + " - " + str(y) )
        else:
            n.append(str(l+1) + ": " + str(ye) + " - " + str(y) )

    for k in range(interv):
        y = round(minimo+c*(k+1),2)
        for j in range(total):
            if (y > arango[j] and y - c <= arango[j]) and not (k == interv-1):
                g += 1
            elif (k == interv-1) and (y >= arango[j] and y - c <= arango[j]):
                g += 1
        h.insert(k,g)
        g = 0

    print("____________________________")
    print("|        N        |   FA   |")
    print("|--------------------------|")

    for m in range(interv):
        print("| "+n[m]+"   |   "+ str(h[m])+"    |")
        print("|--------------------------|")


def cambiov(ncambio):
    print("Que valor quieres poner?")
    acambio = float(input("Valor: "))
    print("Se cambiara: ", arango[ncambio], " por: ", acambio, " es correcto?")
    aceptar = input("[si/no]: ")
    if aceptar == "no":
        cambiov(arango, ncambio)
    elif aceptar == "si":
        arango.pop(ncambio)
        arango.insert(ncambio, acambio)
        print("Valor",ncambio+1,": ",arango[ncambio])
        correct()
    else:
        print("\n     OPCION INCORRECTA")


def correct():
    print("Todos los valores son correctos?")
    cambio = input("[si/no]: ")
    if cambio == "no":
        print("Que valor quieres cambiar?")
        ncambio = int(input("Valor: "))-1
        print("Valor a cambiar: ", arango[ncambio])
        cambiov(ncambio)
    elif cambio == "si":
        tabular()
    else:
        print("\n     OPCION INCORRECTA")

try:
    total = int(input("Total de valores: "))
    for i in range(total):
        i += 1
        x = float(input("valor " + str(i) + ": "))
        arango.insert(i,x)

    correct()

except Exception as e:
    print("\n     SE ESPERABA UN VALOR NUMERICO")
