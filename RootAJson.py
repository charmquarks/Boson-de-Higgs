import uproot
import json

class RootAJson:
  def __init__(self, arch = "SMHiggsToZZTo4L.root", r1 = 50,r2 = 60):
    self.arch = arch
    self.r1 = r1
    self.r2 = r2
    self.afile = uproot.open(self.arch, num_workers=8)


  def Llaves(self):
    afile= uproot.open(self.arch)
    return (afile.keys())

  def Guardar(self, narchivo = "Datos.json"):
    select = self.afile[self.Llaves()[0]]
    parajson = select.arrays().tolist()
    with open(narchivo, 'w') as f:
      json.dump(parajson[self.r1:self.r2], f, indent=2)

raj =RootAJson()
raj.Guardar()
