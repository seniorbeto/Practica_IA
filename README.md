# Práctica Inteligencia Artificial UC3M 2023
### Por Alberto Penas Díaz ([@seniorbeto](https://github.com/seniorbeto)) y Raúl  Aguilar Arroyo ([@Ragarr](https://github.com/Ragarr))
## Resumen
Este proyecto trata de codificar el problema propuesto como enunciado en un Modelo Oculto de Markov (MDP) e implementarlo 
de la manera más general posible en python. Para ello se ha hecho uso de las ecucaciones de Bellman
para distinguir la política óptima de cada estado y así poder generar una simulación realista 
del problema propuesto. 

![equation](https://latex.codecogs.com/svg.image?V(s)=\max_{a&space;\in&space;A(s)}\left[C(a)&space;&plus;&space;\sum_{s'&space;\in&space;S}P(s'&space;\mid&space;s,a)V(s')\right])

El objetivo principal era generalizar la idea al máximo, para poder introducir en el código cualquier 
problema codificabe en un MDP y así, tener máxima flexibilidad a la hora de cambiar parámetros y poder
ver cómo afectan a la resolución del problema. 

## Implementación

Se ha trabajado con las librerías `pandas y matplotlib` para la generación de los data frames y gráficas
respectivamente. Los data frames se generan a partir de los .csv localizados en src/data/ , los cuales representan 
la función de transición de cada posible acción (en nuestro caso, como se trata de un termostato, nuestras
únicas acciones son "Turn ON" y "Turn OFF"). 

Toda la lógica del problema se halla en thermostat.py, el cual es el encargado de llamar en bucle a su función 
interna `calculate_bellman()` para actualizar su valor esperado y su acción más conveniente hasta que este valor
converja. 

