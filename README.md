# Cython

Cython es un lenguaje de programación para simplificar la escritura de módulos de extensión para Python en C y C++. Siendo estrictos, la sintaxis de Cython es la misma de Python pero con algunos agregados. Se pueden llamar funciones en C, o funciones/métodos de C++, directamente desde el código en Cython. Es posible usar tipos estáticos en las variables (enteros, flotantes, o cualquier tipo de dato). Cython compila a código en C o C++ desde Python, y el resultado puede ser usado desde Python como un "Módulo de extensión", o como una aplicación embebida en el intérprete CPython.

### Prerrequisitos compilación en linux:  

* Instalación Build-Essentials: 

Los paquetes build-essentials son meta paquetes que son necesarios para compilar software. Incluyen el depurador GNU, la colección de compiladores g++/GNU y algunas herramientas y bibliotecas más que se requieren para compilar un programa. Por ejemplo, si necesita trabajar en un compilador C/C++, debe instalar meta paquetes esenciales en su sistema antes de iniciar la instalación del compilador C. Al instalar los paquetes build-essential, algunos otros paquetes como G++, dpkg-dev, GCC y make, etc. también se instalan en su sistema. 

`sudo apt install build-essentials`

* Instalación de Python: 

`sudo apt install python3`

* Instalación de Cython: 

`sudo apt install cython3`

* Instalación de CMake:

`sudo apt install CMake`

* Clonar repositorio:

`git clone https://github.com/jchaves1406/Cython.git`

* Correr Makefile:

`make all`
