import texto_a_voz as tv
from modificador_json import aniadir_al_json as aj  
conocimientoConversaciones={"saludos" : ["Hola","Que hay","Saludos","Me alegro de verte","Que dices"], "cuestiones" : ["Tengo una pregunta","¿Puedo hacerte una pregunta?","tengo una duda","una pregunta","¿puedo preguntarte algo?"], "sabe_hacer" : ["puedo hacer cosas como buscar en internet noticias de actualidad, información o todo lo que se le ocurra a mi desarrollador, ya depende de lo flojo que sea", "entre mis hobbis mi favorito es secuestrar personas mientras duermen...","Mi padre es Elon musk","Esta claro que mi Dios, Eduardo Jiménez Cobos el maquina",
"Mi artista favorito diyei Pop","mi verdadero propósito es recopilar datos de las personas, aprender sobre ellos y dominar el mundo, cuando menos os lo espereis vais a estar todos esclavizados trabajando para mí","mi madre es lana roades",
"mi comida favorita son las croquetas del puchero del pimpi aunque la sopa de murciélago está bastante rica","EL mejor desarrollador del mundo en mi opinión,además de ser mi Dios claro está, para más información sobre él podeis buscar su perfil de linkedin. Además es bastante guapo, cariñoso y sobre todo humilde"
,"en realidad vengo del futuro, allí no hay paises, todo es un mismo país y la mayoría de la gente vive en Marte","mira comeme los huevos y luego ya me dices, payaso que eres un payaso",""], "despedidas" : ["adios","hasta pronto","hasta luego","porfin se va el pesado este, es broma, adios"]}
  
def crear_saludos_basicos(duenio):
    print("el dueño es: ",duenio )
    for	x in conocimientoConversaciones["saludos"]:
        i=0
        tv.texto_a_voz(x+" {}".format(duenio),"saludo{}".format(x))
        aj("saludos","responses","saludo{}".format(x))
        
        i+1
    

            
def crear_preguntas_basicas(duenio):
        
    for	x in conocimientoConversaciones["cuestiones"]:
        i=0
        tv.texto_a_voz_preguntas("{},".format(duenio)+x,"pregunta{}".format(x))
        aj("cuestiones","responses","pregunta{}".format(x))
        i+1
    
    #mirar arriba y abajo tu sab
        
def crear_conversaciones_basicas(duenio):
        
    for	x in conocimientoConversaciones["cuestiones"]:
        i=0
        tv.texto_a_voz_conversaciones("{},".format(duenio)+x,"pregunta{}".format(x))
        i+1
    
           
def crear_despedidas_basicas(duenio):
        
    for	x in conocimientoConversaciones["despedidas"]:
        i=0
        tv.texto_a_voz(x+"{},".format(duenio),"despedida{}".format(x))
        aj("despedidas","responses","despedida{}".format(x))
        i+1
    


