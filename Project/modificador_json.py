import json
import os

     
     
     
        
def aniadir_al_json(nombreTag,elemento,cosaNueva):#donde nombreTag es el nombre del tag, elemento si es patterns o responses y cosaNueva es lo que quiero meter
  
  with open("/home/pi/Desktop/vector/vector proyect/conversaciones.json",'r') as file:
    data = json.load(file)
    for cosa in data["intents"]:
      if nombreTag in cosa["tag"]:
            cosa[elemento].append(cosaNueva)
            print(cosa[elemento])
            
  with open("/home/pi/Desktop/vector/vector proyect/conversaciones.json",'w') as file:
    json.dump(data,file,indent=2)
        
      
     
     

