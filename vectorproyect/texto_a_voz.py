from gtts import gTTS
from conversorAudio import transformar_audio,transformar_audio_saludos,transformar_audio_preguntas

def texto_a_voz(texto,texto2):
    #donde texto es el mensaje y texto2 el nombre del archivo
    texto=texto
    file=gTTS(texto,lang="es")
    archivo=texto2
    file.save("/home/pi/Desktop/vector/vector proyect/audios/{}".format(texto2)+".mp3")
    print("guardado")
    transformar_audio("/home/pi/Desktop/vector/vector proyect/audios/{}".format(texto2)+".mp3",texto2)
    print("transformado")

        
def texto_a_voz_saludos(texto,texto2):
    #donde texto es el mensaje y texto2 el nombre del archivo
    texto=texto
    file=gTTS(texto,lang="es")
    archivo=texto2
    file.save("/home/pi/Desktop/vector/vector proyect/audios/saludos/{}".format(texto2)+".mp3")
    print("guardado")
    transformar_audio_saludos("/home/pi/Desktop/vector/vector proyect/audios/saludos/{}".format(texto2)+".mp3",texto2)
    print("transformado")


        
def texto_a_voz_preguntas(texto,texto2):
    #donde texto es el mensaje y texto2 el nombre del archivo
    texto=texto
    file=gTTS(texto,lang="es")
    archivo=texto2
    file.save("/home/pi/Desktop/vector/vector proyect/audios/preguntas/{}".format(texto2)+".mp3")
    print("guardado")
    transformar_audio_preguntas("/home/pi/Desktop/vector/vector proyect/audios/preguntas/{}".format(texto2)+".mp3",texto2)
    print("transformado")



def texto_a_voz_conversaciones(texto,texto2):
    #donde texto es el mensaje y texto2 el nombre del archivo
    texto=texto
    file=gTTS(texto,lang="es")
    archivo=texto2
    file.save("/home/pi/Desktop/vector/vector proyect/audios/conversaciones/{}".format(texto2)+".mp3")
    print("guardado")
    transformar_audio_preguntas("/home/pi/Desktop/vector/vector proyect/audios/conversaciones/{}".format(texto2)+".mp3",texto2)
    print("transformado")

