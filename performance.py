"""
Autor: Jesús Chaves
Programa en cython para el cálculo de la orbita 
Fecha 01 de Noviembre
Tema: Cython
Tópico: Orbita gravitacional
performance: llamaa ambos programas Cy/Py

La idea principal es crear un .csv con la toma de tiempos.
"""

import time
import orbit_py
import orbit_cy

# Se inicializan los planetas
# Datos recuperados de wikipedia
# Configuración planeta tierra en Python
tierra_py = orbit_py.Planet()
tierra_py.x = 100*10**3
tierra_py.y = 300*10**3
tierra_py.z = 700*10**3
tierra_py.vx = 2.00*10**3
tierra_py.vy = 29.87*10**3
tierra_py.vz = 0.034*10**3
tierra_py.m = 3.97424*10**24

# Configuración planeta tierra en Cython
tierra_cy = orbit_cy.Planet()
tierra_cy.x = 100*10**3
tierra_cy.y = 300*10**3
tierra_cy.z = 700*10**3
tierra_cy.vx = 2.00*10**3
tierra_cy.vy = 29.87*10**3
tierra_cy.vz = 0.034*10**3
tierra_cy.m = 3.97424*10**24

# Se consideran las otras variables
time_span = 400
n_steps = 9000000

# Definición de experimentos
# Reducción ruido Gaussiano
# Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.6f},{:.6f} \n"

for i in range(30):
    print("Python: ")
    init_time = time.time()
    orbit_py.step_time(tierra_py, time_span, n_steps)
    end_time = time.time()
    total_time_python = end_time - init_time
    print(f"Tiempo total Python: {total_time_python} segundos.")


    print("Cython: ")
    init_time = time.time()
    orbit_cy.c_step_time(tierra_cy, time_span, n_steps)
    end_time = time.time()
    total_time_cython = end_time - init_time
    print(f"Tiempo total Cython: {total_time_cython} segundos." )

    print(f"Cython es {total_time_python/total_time_cython} veces más rapido que Python.")

    with open('planeta.csv', 'a') as archivo:
        archivo.write(formato_datos.format(total_time_python, total_time_cython))