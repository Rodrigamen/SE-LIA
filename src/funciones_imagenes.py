# -*- coding: utf-8 -*-
"""funciones_imagenes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bj6-fXlhqbKXOuZUcZSZ5BAnAjf5LZQp
"""

def imagenes_url (lista)  
  
  for i in lista:

    url = "https://www.leagueoflegends.com/es-es/champions/"+ f"{i}"
    page = requests.get(url)

  
    if page.status_code == 200:
        sopa = BeautifulSoup(page.content, 'html.parser')
        lista_imagenes1.append(sopa.find_all("img"))

def limpieza_fondo (lista)

  for i in lista:
    i1 = str(i[0]).replace('<img alt="" class="style__NoScriptImg-g183su-0 style__Img-g183su-1 cipsic dBitJH" src="', (""))
    i2 = i1.replace('" style="object-fit:cover;object-position:center 20%"/>', (""))
    resultados_imagenes["fondo"].append(i2)

def limpieza_pasiva (lista)

  for i in lista:
    i1 = str(i[4]).replace('<img alt="" class="style__NoScriptImg-g183su-0 style__Img-g183su-1 cipsic dBitJH" src="', (""))
    i2 = i1.replace('"/>', (""))
    resultados_imagenes["pasiva"].append(i2)

def limpieza_habilidades (lista, habilidad)  
  
  for i in lista_imagenes1:
    i1 = str(i[6]).replace('<img alt="" class="style__NoScriptImg-g183su-0 style__Img-g183su-1 cipsic dBitJH" src="', (""))
    i2 = i1.replace('"/>', (""))
    resultados_imagenes[f"{habilidad}"].append(i2)

def limpieza_portada(lista)

  for i in lista[0]:
    i1 = str(i).replace('<img alt="" class="m-0" loading="lazy" src="', (""))
    i2 = i1.replace('"/>', (""))
    lista_temp.append(i2)