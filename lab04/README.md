# INTEGRACIÓN GTEST VISUAL STUDIO

## Instalación
En caso de no ternerlo instalado tratar de instalarlo con el siguiente codigo que es para ubuntu, en casos de otros linux buscar la equivalencia, si se trata de windows, por lo general vendra integrado en algun IDE
```
    sudo apt-get install libgtest-dev
```

## Creación del proyecto
Simplemente crear una carpeta y empezar a trabajar
![Creación](img/img_2_a.png)

## Pruebas 
Crearemos programas que nos permitan ver como funciona gtest

Crear funcion normal y simple

![funcion normal](img/img_1_b.png)

Crear las pruebas

![funciones pruebas](img/img_1_a.png)

Crear el documento CMake

![cmake file](img/img_1_c.png)

Ejecutamos lo siguiente y vemos el resultado
```
cmake CMakeLists.txt
make
./runTests
```
![resultados](img/img_2_g.png)


## Integracion de gtest
Intalamos la herramienta CMake tools

![cmake tools](img/img_2.png)

Vamos a terminal, y creamos una nueva built 

![crear built](img/img_2_d.png)

Se creara la carpeta built

![built](img/img_2_e.png)

Corre con el boton de play 

![built](img/img_2_h.png)

Nos mostrara el resultado

![resultados 2](img/img_2_g.png)