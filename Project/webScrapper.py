import requests
from bs4 import BeautifulSoup as bs
import re
import google

def scrapper_wikipedia(nombre):
    
    
    if(" " in nombre):
        
        
        array_nombre=nombre.split(" ")
        array_nombre[0]=array_nombre[0].capitalize()
        array_nombre[1]=array_nombre[1].capitalize()

        if "El" in array_nombre[0]:
            
            r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre[1]))
    
        elif "La" in array_nombre[0]:
            r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre[1]))
        elif "Un" in array_nombre[0]:
            r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre[1]))
        elif "Una" in array_nombre[0]:
            r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre[1]))
        
        else:    
            r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre[0]+"_"+array_nombre[1]))
    else:
        array_nombre=nombre.capitalize()
        r= requests.get("https://es.wikipedia.org/wiki/{}".format(array_nombre))
    
    soup = bs(r.text, 'html.parser')
    p=soup.find_all('p')
    text=''

    for i in range(len(p)):
        text+=p[i].text.strip()+"\n"
        
   
        
    
    
    substr=re.findall(r"(?<=\().*?(?=\))",text)
    #substr2=re.findall(r"(?<=\[).*?(?=\])",text)
    #print(substr2)
    for x in substr:
        text=text.replace(x,"")    
    #for x in substr2:
     #   text=text.replace(x,"")    
    
    text=text.replace("()","")
    if("Si el artículo incluso así no existe:" in text ):
        return("No se ha encontrado esa información")
    else:
        text=text.replace(";",",")
        text=text.replace("  "," ")
        text=text.replace("(","")
        text=text.replace(")","")
        text=text.replace("¿","")
        text=text.replace("?","")
        text=text.replace("&","y")
        text=text.replace("[","")
        text=text.replace("]","")
        array=text.split(".")
        
       
        texto_final="".join(array[0])
        texto_final=texto_final+"".join(array[1])
        
        if(len(texto_final)<100 and len(array)>1):
            texto_final=texto_final+"".join(array[2])
        return(texto_final)
