from math import log
import pandas as pd
pd.set_option('display.max_rows', None)

def tabular(datos:int, rounded:int):
    intervalos, frecuencia_absoluta, marca_clase, frecuencia_absoluta_acumulada, frecuencia_relativa_acumulada = [[],[],[],[],[]]
    contador = 0
    intervalo = round(1 + (3.3 * log(len(datos),10)))
    minimo = min(datos)
    maximo = max(datos)
    rango = maximo - minimo
    c = round((rango/intervalo), 4)
    intervalo = round((rango/c))

    for indice in range(intervalo):
        limite_superior = minimo+c*(indice+1)
        limite_inferior= minimo+c*(indice)
        if indice == 0:
            intervalos.append(f"{round(minimo,rounded)} - {round(limite_superior,rounded)}")
            marca_clase.append(round((minimo + limite_superior)/2, rounded))
        else:
            intervalos.append(f"{round(limite_inferior,rounded)} - {round(limite_superior,rounded)}")
            marca_clase.append(round((limite_inferior + limite_superior)/2, rounded))

        for numero in range(len(datos)):
            if (limite_superior > datos[numero] and limite_superior - c <= datos[numero]) and not (indice == intervalo-1):
                contador += 1
            elif (indice == intervalo-1) and (limite_superior - c <= datos[numero]):
                contador += 1
        frecuencia_absoluta.insert(indice,contador)
        contador = 0

    frecuencia_relativa = [round(frecuencia/len(datos), 4) for frecuencia in frecuencia_absoluta]

    # ASIGNAR ACUMULADORES
    for indice in range(intervalo):
        frecuencia_absoluta_acumulada.append(frecuencia_absoluta[indice] if indice == 0 else frecuencia_absoluta[indice] + frecuencia_absoluta_acumulada[indice - 1])
        frecuencia_relativa_acumulada.append(frecuencia_relativa[indice] if indice == 0 else frecuencia_relativa[indice] + frecuencia_relativa_acumulada[indice - 1])

    df = pd.DataFrame({'Intervalos' : intervalos, 'MC' : marca_clase, 'FA' : frecuencia_absoluta, 'FAA' : frecuencia_absoluta_acumulada,
                        'FR' : frecuencia_relativa, 'FRA' : frecuencia_relativa_acumulada})
    
    print("\n valor minimo: ",minimo)
    print(" valor maximo: ",maximo)
    print(" rango: ",round(rango,2))
    print(" intervalo = ",round(intervalo,2))
    print(" amplitud = ",c,"\n")
    print(df)


alturas = [1.87, 1.70, 1.70, 1.72, 1.73, 1.66, 1.63, 1.72, 1.75, 1.65, 1.57, 1.85, 1.79, 1.73, 1.58, 1.75, 1.73, 1.66, 1.74, 1.60, 1.70, 1.88, 1.56, 1.67, 1.54, 1.70, 1.67]
peso = [100, 56, 70, 62, 72, 60, 63, 50, 70, 80, 56, 75, 75, 75, 57, 72, 73, 66, 76, 55, 60, 77, 50, 64, 50, 50, 54]
edad = [22, 19, 18, 20, 18, 19, 19, 20, 18, 38, 18, 19, 18, 18, 18, 22, 21, 18, 18, 19, 18, 18, 18, 18, 18, 18, 19]
tabular(alturas, 2)
tabular(peso, 2)
tabular(edad, 0)