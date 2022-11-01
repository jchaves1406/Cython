# Autor: Jesús Chaves
# Fichero para la prueba y comparativa rendimiento
# Fecha 01 de Noviembre del 2022

import time
import orbit_py
import orbit_cy

planet_cy = orbit_cy.Planet()
planet_py = orbit_py.Planet()


init_time = time.time()
print("Python: ")
orbit_py.step_time(planet_py, 555.5, 3000000)
end_time = time.time()
total_time_python = end_time - init_time
print(f"Tiempo total Python: {total_time_python} segundos.")


init_time = time.time()
print("Cython: ")
orbit_cy.c_step_time(planet_cy, 555.5, 3000000)
end_time = time.time()
total_time_cython = end_time - init_time
print(f"Tiempo total Cython: {total_time_cython} segundos." )

print(f"Cython es {total_time_python/total_time_cython} veces más rapido que Python.")
