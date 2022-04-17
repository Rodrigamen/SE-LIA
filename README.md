# SE-LIA
![portada]
(https://github.com/Rodrigamen/SE-LIA/blob/main/images/league-of-legends-champions-1.jpg)

# Objetivo
El objetivo de este proyecto es analizar les estadísitcas de los campeones por posición y ver la lógica detrás de ellas así como estudiar las elecciones de los jugadores en función de ellas y de las posiciones.

# Working plan 

![workingflow]
(https://raw.githubusercontent.com/Rodrigamen/SE-LIA/main/images/Como-influir-en-el-proceso-de-compra-industrial-02.webp)

Lo primero que he hecho ha sido entrar en kaggle para buscar una base de datos sobre campeones de League of Legends que pudiera aportarme datos para iniciar este análisis.

Tras ello, me descargo de la API de Riot los datos para sus campeones, conteniendo información de win, ban y play rates así como clasificaciones al respecto de sus usos dados los cuales podré estudiar y comparar con las estadísticas que me puede aportar mis datos originales.

Una vez solucionados los problemas para mergear la info del csv y de la API, pasé a la normalización de los datos en los cuales tuve que limpiar los campos de rate y crear algunas nuevas estadísticas acumuladas para poder realizar el análisis que necesito. Con todo esto extraído, limpio y creado, procedo al análisis que pretendo pintando los estudios realizados y sacando conclusiones basándome en la correlación entre los distintos campos que componen mi dataframe.

Para construir el dashboard, acto seguido, extraje la información que me faltaba y la incluí en un dataframe de info definitivo. Tras ello, conseguí la info sobre las habilidades y normalicé entre 0 y 1 todas las características de los campeones para poder compararlas. Con todo esto hecho, pasé a cargar mi modelo de datos de SQL y posteriormente subirlo a Tableau para mostrar todo en el dashboard.

Para realizar todo esto, he usado las siguientes fuentes:

- [Kaggle] (https://www.kaggle.com/datasets/carralas/league-of-legends-champion-stats-922): para la descarga de mi .csv original con los datos estadísticos de cada campeón
- [Riot API] (https://developer.riotgames.com/apis): para la conexión con la API de Riot y la generación del pertinente token para conectarme a ella
- [Cassiopeia] (https://github.com/meraki-analytics/cassiopeia): interfaz python para operar con la API de Riot + documentación para manejarla

### Estructura de los ficheros del proyecto

La estructura del proyecto entregado es la siguiente:

1. Una carpeta con los notebooks:

    a) **Extraccion_Datos_API.ipynb** --> conexión con la API, extracción de datos de la API, consolidación de los mismos en una dataframe y mergeo de la información de la API con la del .csv original

    b) **Exploracion_Datos** --> Análisis inicial de los datos que tenemos dentro del dataframe para plantearnos y estudiar a lo que nos vamos a enfrentar

    c) **Transformacion_Datos** --> Normalización y tratamiento de los datos que nos van a permitir el análisis posterior de los mismos

    d) **Deep_Dive_y_Visualizacion** --> Análisis en profundidad de los datos y visualización de los mismos junto con la exposición de los insights extraídos
    
    e) **Adaptación_Datos** --> Extracción de nuevos datos y adaptación para mostrarlos en el dashboard
    
    f) **Datitos_definitivos** --> últimas modificaciones antes de subir todo a SQL
    
    g) **Alimentamos_Tablas_SQL** --> Inclusión de todos los datos dentro del modelo de SQL

2. Una carpeta src con las funciones usadas en los notebooks en formato .py:

    a) **funciones_api** --> Funciones usadas para la extracción de datos de la API
    b) **funciones_transformacion_datos** --> Funciones usadas para la transformación y normalización de los datos contenidos en nuestro dataframe
    c) **funciones_datos** --> Funciones usadas para la extracción y manipulación de datos en pos de mostrarlos dentro del dashboard

3. Una carpeta data que contiene todos los .csvs usados en el proyecto

    a) **champions-stats** --> .csvs originales de los cuales extraemos las estadísticas de los campeones
    b) **campeones** --> .csvs generados como output de nuestro trabajo y desarrollo del proyecto
    c) **Abilites** --> .csv original con la data de las habilidades
    d) **habilidades** --> .csv construido con la data de habiilidades mencionada en el anterior .csv
    e) **champions** --> .csv final con toda la información necesaria de nuestros campeones
    f) **normalizado** --> .csv donde almacenamos las distintas stats de los campeones normalizada entre 0 y 1 para poder construir el spiden en Tableau
    
4. Una carpeta dashboard con el dashboard construido en Tableau
    

### CONCLUSIONES

- **MID** --> Son los campeones con mayor dificultad del juego
- **ADC** --> La gente los selecciona más que el resto debido a que son la fuente de daño de una partida junto con los mid pero tienen menor dificultad. El juego corrige esto castigándoles en sus estadísiticas base e incrementales en las mismas para equilibrarlos.
- **TOP** --> Los menos usados del juego debido a que en el meta actual se juegan tanques y es el rol menos deseado dentro de los jugadores de LoL
- **Dificultad** --> El juego pretende ser exigente de forma que no premia a los jugadores que escogen campeones de mayor dificultad con mejores estadísticas en los mismos sino que hace recaer todo en la skill sin dar ventajas por ello. Solo equilibra a la baja a aquellos campeones más fáciles y potentes, no equilibra por lo alto a aquellos que son más difíciles.
- **Clasificaciones Riot** --> No hay casi relación entre la clasificación de daño mágico, daño físico que nos propone Riot (puntúa del 1 al 10 estas variables en función de lo enfocado que está a una cosa u otra el campeón) y las estadísticas de cada campeón lo que nos hace ver que todo depende de los objetos y del escalado de habilidades con lo que hace que todo dependa de la habilidad de los jugadores. No es así para los tanques, los cuales sí que tienen un aumento y crecimiento de estadísitcas mayor que ayuda a desempeñar su labor. El juego quiere que si quieres ganar la partida, muestres una mayor habilidad que el rival. Competitivo

#Librerías

[sys](https://docs.python.org/3/library/sys.html)

[pandas](https://pandas.pydata.org/)

[requests](https://pypi.org/project/requests/2.7.0/)

[cassiopeia] (https://github.com/meraki-analytics/cassiopeia)

[numpy] (https://numpy.org/doc/stable/)

[seaborn] (https://seaborn.pydata.org/archive.html)

[matplotlib] (https://matplotlib.org/stable/users/index.html)

[files] (https://colab.research.google.com/notebooks/io.ipynb)
