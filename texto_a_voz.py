from gtts import gTTS
from conversorAudio import transformar_audio,transformar_audio_saludos,transformar_audio_preguntas
import os
def texto_a_voz(texto,texto2):
    #donde texto es el mensaje y texto2 el nombre del archivo
    texto=texto
    file=gTTS(texto,lang="es")
    archivo=texto2
    file.save(os.path.dirname(os.path.abspath(__file__))+"/audios/{}".format(texto2)+".mp3")
    #print("guardado")
    transformar_audio(os.path.dirname(os.path.abspath(__file__))+"/audios/{}".format(texto2)+".mp3",texto2)
    #print("transformado")

