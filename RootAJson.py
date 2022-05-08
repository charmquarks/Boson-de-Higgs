import uproot
import json

class RootAJson:
  def __init__(self, arch = "SMHiggsToZZTo4L.root", r1 = 50,r2 = 60):
    # Para el método constructor se obtienen, como parámetros, el nombre de archivo root, y las filas a analizar
    self.arch = arch
    self.r1 = r1
    self.r2 = r2
    try
      self.afile = uproot.open(self.arch, num_workers=8)
    except:
      print("Incorrect File Type. Try again")
      #Añadida la excepcion por si se introduce un tipo de archivo incorrecto


  def Llaves(self):
    #Regresa las claves del archivo .root
    afile= uproot.open(self.arch)
    return (afile.keys())

  def Guardar(self, narchivo = "Datos.json", i = 0):
    #Guarda los datos presentes en la clave recopilada (que es 0 por default)
    select = self.afile[self.Llaves()[i]]
    parajson = select.arrays().tolist()
    with open(narchivo, 'w') as f:
      #Se abre y guarda el archivo (de nombre "Datos.json" por default)
      json.dump(parajson[self.r1:self.r2], f, indent=2)

raj =RootAJson()
raj.Guardar()
