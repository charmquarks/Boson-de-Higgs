import uproot
import json

root = uproot.open("ZZTo4mu.root", num_workers=5)
file = open("test.json","w") 

print(root.keys())
events = root["Events"]

data = events.arrays()[:100].tolist()
jsonfile = json.dumps(data)
file.write(jsonfile) 

