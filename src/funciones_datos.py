def minmax_norm(df):
    return (df - df.min()) / ( df.max() - df.min())


def extraer_lore (lista, dicc):
  for campeon in lista:
    name_ = Champion(name = campeon, region="EUW")

    if len(name_.name) == 0:
      dicc["Nombre"].append("NS/NC")
    else:
      dicc["Nombre"].append(name_.name)

    if len(str(name_.id)) == 0:
      dicc["ID"].append("NS/NC")
    else:      
      dicc["ID"].append(name_.id) 

    if len(str(name_.lore)) == 0:
      dicc["Lore"].append("NS/NC")
    else:      
      dicc["Lore"].append(name_.lore) 

    if len(str(name_.title)) == 0:
      dicc["Title"].append("NS/NC")
    else:      
      dicc["Title"].append(name_.title)       

def union (lista1, lista2, diccionario):
  for i, z in zip(lista1, lista2):
    diccionario[i] = z      