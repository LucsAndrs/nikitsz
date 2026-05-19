import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
import numpy as np

def buscar_archivos():
    archivos = []

    for archivo in os.listdir():
        if archivo.endswith(".npy"):
            archivos.append(archivo)
    return archivos        

def imprimir_opciones(lista_archivos):
    for i in range(len(lista_archivos)):
        numero = i+1
        print(f"{numero}. {lista_archivos[i]}")
    while True:
        elegir = int(input("elija el archivo a trabajar: "))
        if elegir < 1 or elegir > len(lista_archivos):
            print("Error, vuelva a ingresar un numero")
            continue
        else:
            break
    return lista_archivos[elegir-1]  

def cargar_senal(nombre_archivo):
    senal = np.load(nombre_archivo)
    return senal.tolist()
#calcular mediana
def calcular_mediana(datos_senal):
    resultados = []
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        resultados.append(np.median(ventana))
    return resultados
#calcular media
def calcular_media(datos_senal):
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

fig, ax = plt.subplots()

linea, = ax.plot(datos_senal, label="Señal Original")

texto_box = ax.text(0.05, 0.95, "Señal: Original", transform=ax.transAxes)
ax.set_title("grafico señal")
ax.grid(True)
ax.legend()
print("¡Preparando ventana del gráfico!")
plt.show()

