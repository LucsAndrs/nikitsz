#importamos las librerias
import os 
import matplotlib.pyplot as plt 
import math
from matplotlib.widgets import Button 
import numpy as np 

#esto lo creamos para no tener que estar escribiendo manualmente en la terminal el directorio en el que se encuentran las carpetas
ruta = input("Pegue la ruta de la carpeta (o presione Enter para buscar aquí mismo): ")
if ruta: os.chdir(ruta) 

print(f"\nBuscando archivos .npy en: {os.getcwd()}")
print("-" * 40)

#definimos una funcion para buscar archivos
def buscar_archivos(): 
    archivos = [] 
    for archivo in os.listdir(): 
        if archivo.endswith(".npy"): 
            archivos.append(archivo)
          
    return archivos  

#definimos una funcion para imprimir las opciones disponibles en la carpeta
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
            print(f"El archvio seleccionado es: {lista_archivos[elegir - 1]}")
            break 
    return lista_archivos[elegir-1]  
#definimos una funcion para cargar la señal
def cargar_senal(nombre_archivo): 
    senal = np.load(nombre_archivo) 
    return senal.tolist() 

#definimos una funcion para calcular la mediana
def calcular_mediana(datos_senal): 
    resultados = [] 
    
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        ventana_ordenada = sorted(ventana)
        indice_central = len(ventana_ordenada) // 2        
        resultados.append(ventana_ordenada[indice_central])
        
    return resultados
#definimos una funcion para el progedio general
def calcular_promedio_global(datos):
    suma_total = sum(datos)
    cantidad_datos = len(datos)
    promedio = suma_total / cantidad_datos
    return promedio

#definimos una funcion para calcular media
def calcular_media(datos_senal):
    resultados = []
    for i in range(len(datos_senal)):
        ventana = datos_senal[i:i+7]
        promedio_ventana = calcular_promedio_global(ventana)
        resultados.append(promedio_ventana)
    return resultados

#entrelazamos las funciones entre si para que funcione el codigo
archivos_encontrados = buscar_archivos()
archivo_elegido = imprimir_opciones(archivos_encontrados)
datos_senal = cargar_senal(archivo_elegido)
datos_mediana = calcular_mediana(datos_senal)
datos_media = calcular_media(datos_senal)

#definimos una funcion para la señal original
def senal_original(event):
    linea.set_ydata(datos_senal)
    linea.set_label("Señal original")
    texto_box.set_text("Original")
    ax.legend()
    plt.draw()

#definimos una funcion para mostrar la mediana
def mostrar_mediana(event):
    linea.set_ydata(datos_mediana)
    linea.set_label("Mediana móvil")
    texto_box.set_text("Mediana")
    ax.legend()
    plt.draw()

#definimos una funcion para mostrar media
def mostrar_media(event):
    linea.set_ydata(datos_media)    
    linea.set_label("Media móvil")  
    texto_box.set_text("Media")     
    ax.legend()                       
    plt.draw()


#definimos una funcion para calcular desviacion estandar
def calcular_desviacion_global(datos):
    promedio = calcular_promedio_global(datos)
    suma_diferencias = 0
    for x in datos:
        diferencia = x - promedio
        suma_diferencias += diferencia ** 2
    varianza = suma_diferencias / len(datos)
    desviacion = math.sqrt(varianza)
    return desviacion

#definimos una funcion para mostrar las estadisticas (promedio, desviacion estandar, minimo, maximo)
def mostrar_estadisticas(event):
    datos_actuales = linea.get_ydata()
    maximo_actual = calcular_maximo(datos_actuales)
    minimo_actual = calcular_minimo(datos_actuales)
    promedio_actual = calcular_promedio_global(datos_actuales)
    desviacion_actual = calcular_desviacion_global(datos_actuales)
    texto_estadisticas = f"Promedio: {promedio_actual:.2f}\nDesv. Estándar: {desviacion_actual:.2f}\nMaximo: {maximo_actual:.2f}\nMinimo: {minimo_actual:.2f}"
    texto_box.set_text(texto_estadisticas)
    plt.draw()

#definimos una funcion para calcular el minimo
def calcular_minimo(datos):
    minimo = np.min(datos)
    return minimo

#definimos una funcion para calcular maximo
def calcular_maximo(datos):
    maximo = np.max(datos)
    return maximo

#aca creamos el grafico
fig, ax = plt.subplots()        #prepara el area especifica para dibujar el grafico

linea, = ax.plot(datos_senal, label="Señal Original") #esto traza el grafico

ax.set_title("grafico señal") 
ax.grid(True)                   #creamos una cuadricula
ax.legend()
plt.subplots_adjust(bottom=0.20)#esto deja un espacio vacio del 20% del grafico para posicionarse de manera correcta los botones
print("¡Preparando ventana del gráfico!")

#le asignamos pocisiones a los botones
ax_btn1 = plt.axes([0.5, 0.02, 0.2, 0.07])
ax_btn2 = plt.axes([0.75, 0.02, 0.2, 0.07])
ax_btn3 = plt.axes([0.25, 0.02, 0.2, 0.07])
ax_btn4 = plt.axes([0.02, 0.02, 0.2, 0.07])

#aca creamos los nombres de los botones y la funcionalidad
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