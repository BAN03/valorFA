from math import log
import pandas as pd
pd.set_option('display.max_rows', None)

def tabular(datos:int):
    intervalos, frecuencia_absoluta, marca_clase, frecuencia_absoluta_acumulada, frecuencia_relativa_acumulada = [[],[],[],[],[]]
    g = 0
    intervalo = round(1 + (3.3 * log(total,10)))
    minimo = min(datos)
    maximo = max(datos)
    rango = maximo - minimo
    c = round((rango/intervalo),3)
    interv = round((rango/c))
    print("\n valor minimo: ",minimo)
    print(" valor maximo: ",maximo)
    print(" rango: ",round(rango,2))
    print(" intervalo = ",round(intervalo,2))
    print(" amplitud = ",c,"\n")

    # asignacion de limite inferior y superior
    for l in range(interv):
        limite_superior = minimo+c*(l+1)
        limite_inferior= minimo+c*(l)
        if l == 0:
            intervalos.append(f"{round(minimo,2)} - {round(limite_superior,2)}")
            marca_clase.append(round((minimo + limite_superior)/2, 4))
        else:
            intervalos.append(f"{round(limite_inferior,2)} - {round(limite_superior,2)}")
            marca_clase.append(round((limite_inferior + limite_superior)/2, 4))

    # ASIGNADOR DE FRECUENCIA ABSOLUTA
    for k in range(interv):
        limite_superior = minimo+c*(k+1)
        for j in range(total):
            if (limite_superior > datos[j] and limite_superior - c <= datos[j]) and not (k == interv-1):
                g += 1
            elif (k == interv-1) and (limite_superior - c <= datos[j]):
                g += 1
        frecuencia_absoluta.insert(k,g)
        g = 0

    frecuencia_relativa = [round(frecuencia/total, 4) for frecuencia in frecuencia_absoluta]

    # ASIGNAR ACUMULADORES
    for m in range(interv):
        if m == 0:
            frecuencia_absoluta_acumulada.append(frecuencia_absoluta[m])
            frecuencia_relativa_acumulada.append(frecuencia_relativa[m])
        else:
            frecuencia_absoluta_acumulada.append(frecuencia_absoluta[m] + frecuencia_absoluta_acumulada[m - 1])
            frecuencia_relativa_acumulada.append(frecuencia_relativa[m] + frecuencia_relativa_acumulada[m - 1])

    df = pd.DataFrame({'Intervalos' : intervalos, 'MC' : marca_clase, 'FA' : frecuencia_absoluta, 'FAA' : frecuencia_absoluta_acumulada,
                        'FR' : frecuencia_relativa, 'FRA' : frecuencia_relativa_acumulada})
    print(df)
    intervalos, frecuencia_absoluta, marca_clase, frecuencia_absoluta_acumulada, frecuencia_relativa_acumulada = [[],[],[],[],[]]



total = 27
alturas = [1.87, 1.70, 1.70, 1.72, 1.73, 1.66, 1.63, 1.72, 1.75, 1.65, 1.57, 1.85, 1.79, 1.73, 1.58, 1.75, 1.73, 1.66, 1.74, 1.60, 1.70, 1.88, 1.56, 1.67, 1.54, 1.70, 1.67]
peso = [100, 56, 70, 62, 72, 60, 63, 50, 70, 80, 56, 75, 75, 75, 57, 72, 73, 66, 76, 55, 60, 77, 50, 64, 50, 50, 54]
edad = [22, 19, 18, 20, 18, 19, 19, 20, 18, 38, 18, 19, 18, 18, 18, 22, 21, 18, 18, 19, 18, 18, 18, 18, 18, 18, 19]
tabular(alturas)
tabular(peso)
tabular(edad)