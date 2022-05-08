
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

class Histograma:
  # Clase que permitirá producir un histograma usando pandas, a partir de datos en formato JSON
  data = ""
  r1 = 0
  r2 = 1

  def __init__(self,datos = "Datos.json", r1 = 0, r2 = 10):
    # Se extraen los datos, y las observaciones que se desean obtener
    self.datos = datos
    self.d1 = r1
    self.d2 = r2


  def ToPandas(self):
    d1 = self.d1
    d2 = self.d2
    data = pd.read_json(self.datos)
    return data[d1:d2]
  def ToPandasTodo(self):
    data = pd.read_json(self.datos)
    return data
  #Convierte todas a dataframes de Pandas

  def Cols(self):
    try:
      return self.ToPandasTodo().columns
    except:
      print("Invalid data type, try again")

  #Te entrega el arreglo de columnas de los DATAFRAMES de pandas
  def NomCols(self):
    listnoms =[]
    for cols in self.ToPandasTodo().columns:
      listnoms.append(cols)
    return listnoms

  def Histo(self, variable = "Muon_mass"):
    #Aquí debes de introducir la columna de donde quieres obtener el histograma. Por default se añadió la masa del muón

    sconj = self.ToPandas()[variable]
    hist = plt.hist(sconj)
    return plt.show()

hist = Histograma("Datos.json")
hist.Histo()
