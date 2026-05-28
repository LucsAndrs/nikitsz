import os #lo utilizamos para poder buscar carpetas destro de el directorio
import matplotlib.pyplot as plt #utilizado para graficar las funciones
import math
from matplotlib.widgets import Button #sirve para poder crear los botones dentro de la ventana del grafico
import numpy as np #utilizado para realizar las operaciones matematicas

def buscar_archivos(): #definimos una funcion para buscar archivos npy
    archivos = [] #creamos una lista vacia para luego agregar archivos

    for archivo in os.listdir(): #aqui le decimos que recorra en el directorio
        if archivo.endswith(".npy"): #si el archivo termina con .npy
            archivos.append(archivo) #se agrega el archivo a la lista archivo
    return archivos  #decimos que se muestre la lista archivos

def imprimir_opciones(lista_archivos): #definimos una funcion para imprimir opciones con el valor de entrada lista_archivos
    for i in range(len(lista_archivos)): #decimos que cuente la posicion de un valor, haciendo lo mismo para los valores restantes
        numero = i+1 #aqui se le suma 1 a la posicion porque python comienza a contar desde el 0 no desde el 1
        print(f"{numero}. {lista_archivos[i]}") #aqui le decimos que imprima el numero y el archivo
    while True:  #creamos un bucle que siempre es verdadero, por ende siempre entra dentro del bucle
        elegir = int(input("elija el archivo a trabajar: ")) #aqui debe ingresar un numero (el int es para convertirlo aa entero)
        if elegir < 1 or elegir > len(lista_archivos): #condicion que dice: si el numero elegido es menor a 1 o mayor al numero maximo del archivo
            print("Error, vuelva a ingresar un numero") #imprime un mensaje de error
            continue #vuelve al inicio del bucle
        else: #si no se cumple ninguna condicion
            break #se acaba el bucle
    return lista_archivos[elegir-1]  #aqui decimos que devuelva el valor del numero elegido restando 1 (esto para que pueda leerlo en el orden correcto)

def cargar_senal(nombre_archivo): #definimos funcion para cargar una señal
    senal = np.load(nombre_archivo) #guarda la informacion de el archivo en la variable senal en matriz
    return senal.tolist() #transforma la informacion de una matriz a una lista normal
#calcular mediana
def calcular_mediana(datos_senal): #definimos una funcion para calcular la mediana
    resultados = [] #creamos lista vacia para guardar datos
    for i in range(len(datos_senal)): #recorremos el valor, mientras la variable i va tomando el valor de las posiciones
        ventana = datos_senal[i:i+7] #aqui le decimos que tome los datos desde que empieza hasta 7
        resultados.append(np.median(ventana)) #aqui calcula la mediana, y luego agrega los resultados a la lista resultados
    return resultados #decimos que devuelva los datos de la lista resultados
#calcular media
def calcular_media(datos_senal): #definimos una funcion para calcular la media
    resultados = []
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        resultados.append(np.mean(ventana))
    return resultados
archivos_encontrados = buscar_archivos()
archivo_elegido = imprimir_opciones(archivos_encontrados)
datos_senal = cargar_senal(archivo_elegido)
datos_mediana = calcular_mediana(datos_senal)
datos_media = calcular_media(datos_senal)

def senal_original(event):
    linea.set_ydata(datos_senal)
    linea.set_label("Señal original")
    texto_box.set_text("Original")
    ax.legend()
    plt.draw()

def mostrar_mediana(event):
    linea.set_ydata(datos_mediana)
    linea.set_label("Mediana móvil")
    texto_box.set_text("Mediana")
    ax.legend()
    plt.draw()

def mostrar_media(event):
    linea.set_ydata(datos_media)    
    linea.set_label("Media móvil")  
    texto_box.set_text("Media")     
    ax.legend()                       
    plt.draw()

def calcular_promedio_global(datos):
    suma_total = sum(datos)
    cantidad_datos = len(datos)
    promedio = suma_total / cantidad_datos
    return promedio

def calcular_desviacion_global(datos):
    promedio = calcular_promedio_global(datos)
    suma_diferencias = 0
    for x in datos:
        diferencia = x - promedio
        suma_diferencias += diferencia ** 2
    varianza = suma_diferencias / len(datos)
    desviacion = math.sqrt(varianza)
    return desviacion

def mostrar_estadisticas(event):
    datos_actuales = linea.get_ydata()
    promedio_actual = calcular_promedio_global(datos_actuales)
    desviacion_actual = calcular_desviacion_global(datos_actuales)
    texto_estadisticas = f"Promedio: {promedio_actual:.2f}\nDesv. Estándar: {desviacion_actual:.2f}"
    texto_box.set_text(texto_estadisticas)
    plt.draw()



fig, ax = plt.subplots()

linea, = ax.plot(datos_senal, label="Señal Original")


ax.set_title("grafico señal") 
ax.grid(True)
ax.legend()
print("¡Preparando ventana del gráfico!")

ax_btn1 = plt.axes([0.5, 0.02, 0.2, 0.07])
ax_btn2 = plt.axes([0.75, 0.02, 0.2, 0.07])
ax_btn3 = plt.axes([0.25, 0.02, 0.2, 0.07])
ax_btn4 = plt.axes([0.02, 0.02, 0.2, 0.07])

btn_estadisticas = Button(ax_btn4, "Estadísticas")
btn_estadisticas.on_clicked(mostrar_estadisticas)

btn_mediana = Button(ax_btn1, "Mediana móvil")
btn_media = Button(ax_btn2, "Media móvil")
btn_original = Button(ax_btn3, "Señal original")

btn_mediana.on_clicked(mostrar_mediana)
btn_media.on_clicked(mostrar_media)
btn_original.on_clicked(senal_original)
texto_box = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.4)
    )
plt.show()