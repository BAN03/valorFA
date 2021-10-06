from math import log
arango = []
n = []
h = []
f = 0

def tabular():
    g = 0
    intervalo = round(1 + (3.3 * log(total,10)))
    minimo = min(arango)
    maximo = max(arango)
    rango = maximo - minimo
    c = round((rango/intervalo),5)
    interv = round((rango/c))
    print("\n valor minimo: ",minimo)
    print(" valor maximo: ",maximo)
    print(" rango: ",round(rango,2))
    print(" intervalo = ",round(intervalo,2))
    print(" c = ",c,"\n")

    for l in range(interv):
        y = minimo+c*(l+1)
        ye= minimo+c*(l)
        if l == 0:
            n.append(str(l+1) + ": " + str(round(minimo,2)) + " - " + str(round(y,2)) )
        else:
            n.append(str(l+1) + ": " + str(round(ye,2)) + " - " + str(round(y,2)) )

    for k in range(interv):
        y = minimo+c*(k+1)
        for j in range(total):
            if (y > arango[j] and y - c <= arango[j]) and not (k == interv-1):
                g += 1
            elif (k == interv-1) and (y - c <= arango[j]):
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
        f += 1
        x = float(input("valor " + str(f) + ": "))
        arango.append(x)

    correct()

except Exception as e:
    print("\n     SE ESPERABA UN VALOR NUMERICO")
