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

# Funciones para mostrar las señales
"""
def senal_original(event):
    linea.set_ydata(datos_senal)    
    linea.set_label("Señal original")  
    texto_box.set_text("Original")     
    ax.legend()                       
    plt.draw()      """  #Si quieres añadimos esta funcion para añadir un boton de señal original

def mostrar_mediana(event):
    linea.set_ydata(datos_mediana)    
    linea.set_label("Mediana móvil")  
    texto_box.set_text("Mediana")     
    ax.legend()                       
    plt.draw()

def mostrar_media(event):
    linea.set_ydata(datos_media)    
    linea.set_label("Media móvil")  
    texto_box.set_text("Media")  #Podriamos sacar esta linea junto con la de mediana

    ax.legend()                       
    plt.draw()

fig, ax = plt.subplots()

# Tamaño de la gráfica
plt.subplots_adjust(top= 0.93)
plt.subplots_adjust(bottom= 0.2)

linea, = ax.plot(datos_senal, label="Señal Original")

texto_box = ax.text(0.05, 0.95, "Señal: Original", transform=ax.transAxes)
ax.set_title("Gráfico Señal")
ax.grid(True)
ax.legend()
print("¡Preparando ventana del gráfico!")



# -----------------
# Botones
# -----------------

ax_btn1 = plt.axes([0.15, 0.02, 0.2, 0.07])
ax_btn2 = plt.axes([0.65, 0.02, 0.2, 0.07])

btn_mediana = Button(ax_btn1, "Mediana móvil")
btn_media = Button(ax_btn2, "Media móvil")

btn_mediana.on_clicked(mostrar_mediana)
btn_media.on_clicked(mostrar_media)
texto_box = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.4)
    )

plt.show()
