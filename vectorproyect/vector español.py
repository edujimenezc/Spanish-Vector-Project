 #!/usr/bin/env python3.7
 # -*- coding: utf-8 -*-
import sys

import speech_recognition as sr
import anki_vector
from gtts import gTTS
from anki_vector import robot as vector #vector.disconnect().conn.close() mirarlo bn
from webScrapper import scrapper_wikipedia as scrapper
import configuracion_conversaciones_basicas as cb
import chatbot

import texto_a_voz as tv
def voz_a_texto():
    text=""
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("di algo")
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
            
            audio="/home/pi/Desktop/vector/vector proyect/audios/"+sonido1
            #donde sonido es audio.wav
            robot.audio.stream_wav_file(audio,100)
        
        
     
    
       
       
    



     
            

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
    mi_vector=mi_robot()
    configurado=mi_vector.get_configurado()
   
    print("Robot configurado: ",configurado)
    
    if(configurado==False):
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            
            mi_vector.hablar("conf0.wav")#saludo de entrada
            mi_vector.hablar("conf1.wav")#configuracion nombre
            mi_vector.set_nombre(nuevoNombre=voz_a_texto())
            print("nombre : ",mi_vector.get_nombre())
            
            while(mi_vector.get_nombre()==""):
                tv.texto_a_voz("Lo siento no te he escuchado bien, ¿puedes repetirlo? ","ErrorVozNoReconocida")
                mi_vector.hablar("ErrorVozNoReconocida.wav")
                mi_vector.set_nombre(nuevoNombre=voz_a_texto())
                
            tv.texto_a_voz("Vale, a partir de ahora me llamo {}".format(mi_vector.get_nombre()),"confNombre")
            mi_vector.hablar("confNombre.wav")
            
            
            #mi_robot.hablar(conf3)#configuracion del cumpleaños ver con fechas
            #mi_robot.set_cumpleanios(nuevaFecha=voz_a_texto())
            #creacion de textos preconstruidos con los datos del registro
            ##saludo1="Me llamo {}, ese es el nombre que me pusiste".format(self.nombre)
            #texto_a_voz(robotMio.getConversaciones(""),"/audios/basictalk0.wav")
            #texto_a_voz("Mi nombre es {}".format(robotMio.get_nombre()),"basictalk0")
            mi_vector.hablar("conf2.wav")#configuracion duenio
            mi_vector.set_duenio(nuevoDuenio=voz_a_texto())
            while(mi_vector.get_duenio()==""):
                tv.texto_a_voz("Lo siento no te he escuchado bien, ¿puedes repetirlo? ","ErrorVozNoReconocida")
                mi_vector.hablar("ErrorVozNoReconocida.wav")
                mi_vector.set_duenio(nuevoDuenio=voz_a_texto())
            tv.texto_a_voz("De acuerdo, encantada de conocerte, {}".format(mi_vector.get_duenio()),"confDuenio")
            mi_vector.hablar("confDuenio.wav")
            tv.texto_a_voz("Ahora mientras termino de configurarme voy a ponerte una canción","confTerminando")
            mi_vector.hablar("confTerminando.wav")
            mi_vector.hablar("colacao.wav")
            #aqui van las conversaciones basicas
            tv.texto_a_voz("dime","dime")
            
            
            
            #meter sonido de victoria
           
            #saludo2="Mi dueño es {}".format(self.duenio)
            #texto_a_voz(saludo2,"basictalk1.wav")
            
            
            #for x in preguntas:
             #   texto_a_voz(preguntas[x]+" {}".format(self.duenio),"/audios/preguntas/pregunta{}.wav".format(x))

            
            cb.crear_saludos_basicos(mi_vector.get_duenio())
            cb.crear_preguntas_basicas(mi_vector.get_duenio())
            #falta poner la fecha actual y el cumpleaños


            
            #self.conversaciones={"cómo te llamas": hablar(basictalk0.wav), "cuál es tu nombre" : hablar(basictalk0.wav), "quién es tu dueño" : hablar(basictalk1)}
            tv.texto_a_voz("¡Listo ya ha acabado la configuración!","confTerminado")
            mi_vector.hablar("confTerminado.wav")
           
        mi_vector.set_configurado(True)
        configurado=mi_vector.get_configurado()
        print(configurado)
   
     
     
    print("configurado correctamente")
    mi_vector.hablar("saludoHola.wav")
    texto=""
    while(("vete a dormir" in texto)==False):
        texto=voz_a_texto()
        
        #mi_vector.get_nombre()
        if "paco" in texto:
            mi_vector.hablar("dime.wav")
            texto=voz_a_texto()
            print(texto)
            
            if "quién es" in texto:
                pregunta=texto.split(" ")
                nombre="".join(pregunta[2])
                if(len(pregunta)>3):
                    nombre=nombre+" "+"".join(pregunta[3])
                
                respuesta=scrapper(nombre)
                
                tv.texto_a_voz(respuesta,nombre)
                
                mi_vector.hablar(nombre+".wav")
                
            if "chatbot" in texto:
                mi_vector.hablar("dime.wav")
                texto=voz_a_texto()
                print(os.sys("/home/pi/Desktop/vector/vector proyect/chatbot_resultados.py"))
                audio=chatbot(texto)
                if " " in audio:
                    audio=audio.replace(" ","")
                mi_vector.hablar("{}.wav".format(audio))# queda rpobarlo
            
    

    
    
        

    
    
        
            

            
                
                

                
            



if __name__ == "__main__":
    main()