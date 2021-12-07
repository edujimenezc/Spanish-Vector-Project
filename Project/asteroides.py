from urllib.request import urlopen
import json
from datetime import date
from datetime import timedelta
asteroides_peligrosos=[]
def getApi(dias):
    fecha=date.today()
    fechaInicio=fecha.strftime("%Y-%m-%d")
    fechaFinal=fecha+timedelta(days=dias)
    fechaFInal=fechaFinal.strftime("%Y-%m-%d")
    
    
    url="https://api.nasa.gov/neo/rest/v1/feed?start_date="+fechaInicio+"&end_date=2021-09-30&api_key=BpQZqBfGdd8jARaTrQS5pDlrPOSXZqz8t7XPBsQt"
    response =urlopen(url)
    data=json.loads(response.read())
    asteroides=data["near_earth_objects"]
    fechas=asteroides.keys()
    asteroidesVerdad=[]
    for x in fechas:
        asteroidesVerdad.append(asteroides[x])

    for x in asteroidesVerdad:
   
        for y in x:
            if y["is_potentially_hazardous_asteroid"] is True:
                asteroides_peligrosos.append(y["name"])
        

def contar_asteroides_peligrosos():
    return len(asteroides_peligrosos)

def nombres_de_asteroides_peligrosos():
    asteroides=""
    for x in asteroides_peligrosos:
        asteroides+=x+"\n"
    return asteroides.replace("[\'(","").replace("(","").replace(")","")
