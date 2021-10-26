from chatbot_resultados import hablar_chatbot as chatbotIA
#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import sys
from datetime import date
import os
import asteroides 
import speech_recognition as sr
import anki_vector
from gtts import gTTS
from anki_vector import robot as vector #vector.disconnect().conn.close() mirarlo bn
from webScrapper import scrapper_wikipedia as scrapper
import configuracion_conversaciones_basicas as cb
import texto_a_voz as tv
#from modificador_json import aniadir_al_json
def voz_a_texto():
    text=""
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("di algo")#cambiarlo por animacion
        audio =r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            
        except:
            print("Error al reconocer la voz")
    return text.lower()








                

            




                    

            #robot.behavior.drive_on_charger()








class mi_robot:

    def __init__(self):
     
        #fichero = open("./docs/validado.txt", 'r')
        
        self.nombre="Manuel"
        self.duenio ="Yo"
        self.validado=False#fichero.read()
        #fichero.close()
        self.color_ojos=0
        self.cumpleanios="Uno de Mayo del dosmil dos"
         #web scraping cto 
        
        #self.edad= edad
        

    def set_nombre(self,nuevoNombre):
        self.nombre=nuevoNombre
    
    def set_duenio(self,nuevoDuenio):
        self.duenio=nuevoDuenio
    
    def set_color_ojos(self,color):
        self.color_ojos=color
        colores_disponibles={"morado" : [0.83, 0.76] , "zafiro" : [0.57, 1.00] , "naranja": [0.05, 0.95] }
        for x in colores_disponibles:
            if x in self.color_ojos:
                robot.behavior.set_eye_color(x[0],x[1])

        

    def set_cumpleanios(self,nuevaFecha):
        self.cumpleanios=nuevaFecha
    def get_nombre(self):
        return self.nombre

    def get_duenio(self):
        return self.duenio

    
    def get_configurado(self):
        return self.validado
    
    def set_configurado(self,validado_o_no):
        self.validado=validado_o_no
    #
    #esta tard
    #
    #

    def hablar(self,sonido):
        
        sonido1=sonido
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            audio=os.path.dirname(os.path.abspath(__file__))+"/audios/"+sonido1
            
            robot.audio.stream_wav_file(audio,100)
            
    def chatbot(self,texto):
        
                
        audio=chatbotIA(texto)
        audioReal=audio    
        if " " in audio:
            audio=audio.replace(" ","")
        if "{}.wav".format(audio) in os.listdir(os.path.dirname(os.path.abspath(__file__))+"/audios"):
            self.hablar("{}.wav".format(audio))
        else:
            tv.texto_a_voz(audioReal,audio)
            self.hablar("{}.wav".format(audio))
                    
        #self.hablar("seguirchatbot.wav")
        #def aprender(self,nombreTag,tipoPR,texto):
        #   aniadir_al_json()
        
                    
     
    
       
       
    



     
            

    def conversar(self):
        
        conversacion=voz_a_texto()
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            for x in self.acciones:
                if x in conversacion:
                    robot.behavior.say_text(acciones[x])

    #def validado():
     #fichero= open("/home/pi/Desktop/vector/vector proyect/docs/validado.txt", 'w')
     #fichero.write("True")
     #fichero.close
    



def main():
    fecha0=date.today()
    fecha=str(fecha0.strftime("%Y-%m-%d"))
    mi_vector=mi_robot()
    configurado=mi_vector.get_configurado()
   
    print("Robot configurado: ",configurado)
    
    if(configurado==True):
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            
            mi_vector.hablar("conf0.wav")#saludo de entrada
            mi_vector.hablar("conf1.wav")#configuracion nombre
            mi_vector.set_nombre(nuevoNombre=voz_a_texto())
            print("nombre : ",mi_vector.get_nombre())
            
            while(mi_vector.get_nombre()==""):
                mi_vector.hablar("ErrorVozNoReconocida.wav")
                mi_vector.set_nombre(nuevoNombre=voz_a_texto())
                
            tv.texto_a_voz("Vale, a partir de ahora me llamo {}".format(mi_vector.get_nombre()),"confNombre")
            mi_vector.hablar("confNombre.wav")
            
            
            #texto_a_voz("Mi nombre es {}".format(robotMio.get_nombre()),"basictalk0")
            mi_vector.hablar("conf2.wav")#configuracion duenio
            mi_vector.set_duenio(nuevoDuenio=voz_a_texto())
            while(mi_vector.get_duenio()==""):
                #tv.texto_a_voz("Lo siento no te he escuchado bien, puedes repetirlo ","ErrorVozNoReconocida")
                mi_vector.hablar("ErrorVozNoReconocida.wav")
                mi_vector.set_duenio(nuevoDuenio=voz_a_texto())
            tv.texto_a_voz("De acuerdo, encantada de conocerte, {}".format(mi_vector.get_duenio()),"confDuenio")
            mi_vector.hablar("confDuenio.wav")
            tv.texto_a_voz("Ahora mientras termino de configurarme voy a ponerte una cancion","confTerminando")
            mi_vector.hablar("confTerminando.wav")
            mi_vector.hablar("colacao.wav")
            #aqui van las conversaciones basicas
            tv.texto_a_voz("dime","dime")
            
            
            
            
            #for x in preguntas:
             #   texto_a_voz(preguntas[x]+" {}".format(self.duenio),"/audios/preguntas/pregunta{}.wav".format(x))

            
            cb.crear_saludos_basicos(mi_vector.get_duenio())
            cb.crear_preguntas_basicas(mi_vector.get_duenio())
            

            
            tv.texto_a_voz("Listo ya ha acabado la configuracion","confTerminado")
            mi_vector.hablar("confTerminado.wav")
           
        mi_vector.set_configurado(True)
        configurado=mi_vector.get_configurado()
        print(configurado)
   
     
     
    print("configurado correctamente")
    #mi_vector.hablar("saludoHola.wav")
    texto_llamada=""
    texto=""
    while(("vete a dormir" in texto)==False):
        texto_llamada=voz_a_texto()
        
        #mi_vector.get_nombre()
        while "paco" in texto_llamada:

            
            try:
                seguir_texto="si"
                mi_vector.hablar("dime.wav")
                texto=voz_a_texto()
   
                print(texto)
                if "vete a tu casa" in texto:
                    args = anki_vector.util.parse_command_args()
                    with anki_vector.Robot(args.serial) as robot:
                        robot.behavior.drive_on_charger()
                elif "sal de tu casa" in texto:
                    args = anki_vector.util.parse_command_args()
                    with anki_vector.Robot(args.serial) as robot:
                        robot.behavior.drive_off_charger()
                elif "hay asteroides peligrosos esta semana" in texto:
                    args = anki_vector.util.parse_command_args()
                    with anki_vector.Robot(args.serial) as robot:
                        mi_vector.hablar("espera.wav")#espera un momento, voy a mirarlo
                        num_asteroides=asteroides.contar_asteroides_peligrosos()
                        tv.texto_a_voz("actualmente hay "+str(num_asteroides)+" asteroides peligrosos","asteroides"+fecha)#fecha hoy

                        mi_vector.hablar("asteroides"+fecha+".wav")
                        if num_asteroides > 0:
                            #mi_vector.hablar("quieresnombresasteroides.wav")#quieres saber sus nombres
                            
                            
                            #mi_vector.hablar("espera.wav")#un momento porfabor
                            tv.texto_a_voz("Los nombres de los asteroides peligrosos son "+asteroides.nombres_de_asteroides_peligrosos(),"nombreasteroides"+fecha)#fechahoyasteroidespeligrosos
                            mi_vector.hablar("nombreasteroides"+fecha+".wav")
                            if num_asteroides > 1 :
                                mi_vector.hablar("creoquevamosamorir.wav")
                            
                elif "quién es" or "qué es" in texto:
                    pregunta=texto.split(" ")
                    nombre="".join(pregunta[2])
                    if(len(pregunta) > 3):
                            nombre=nombre+" "+"".join(pregunta[3])
                        
                    
                    if "{}.wav".format(nombre) in os.listdir(os.path.dirname(os.path.abspath(__file__))+"/audios"):
                        mi_vector.hablar(nombre+".wav")
                    else:
         
                        respuesta=scrapper(nombre)
                
                        tv.texto_a_voz(respuesta,nombre)
                
                        mi_vector.hablar(nombre+".wav")
                
            
                else:
                    mi_vector.chatbot(texto)
                mi_vector.hablar("seguirhablando.wav")
                seguir_texto=voz_a_texto()
                if seguir_texto != "si":
                    texto_llamada=""   
                

            except IndexError:
                mi_vector.chatbot(texto)
                mi_vector.hablar("seguirhablando.wav")
                seguir_texto=voz_a_texto()
                if seguir_texto != "si":
                    texto_llamada=""
        
        

                #mi_vector.hablar(vale)
        
        
        
        
        
        
            #elif "crea una página web" in texto:
             #   mi_vector.hablar("crearweb1.wav")
            #elif "te voy a enseñar una cosa" or "quiero que aprendas algo" in texto:
                #mi_vector.hablar("aprender1.wav") #que vas a enseñarme
                #cosa_a_aprender=voz_a_texto()
                #if "una nueva conversacion" or "conversacion" or "nueva conversacion" in cosa_a_aprender:
                 #   mi_vector.hablar("aprender2.wav") #vale, puedes enseñarme (categorias json), de que se trata esta vez?
                  #  tipo_conversacion=voz_a_texto()
                   # mi_vector.hablar("aprender3.wav") #perfecto, tu que vas a decirme 
                    #emisor=voz_a_texto()
                    #mi_vector.hablar("aprender4.wav") # gracias, ya he aprendido algo más
                    #aniadir_al_json(tipo_conversacion,"patterns",emisor)
                    #aniadir_al_json(tipo_conversacion,"responses",emisor)
                    
                    
                    

            
                
                
                    
                
                
            
    

    
    
        

    
    
        
            

            
                
                

                
            



if __name__ == "__main__":
    main()