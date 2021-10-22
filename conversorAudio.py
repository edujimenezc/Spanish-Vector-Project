from os import path
from os import remove
from pydub import AudioSegment
import sox
def transformar_audio(entrada,salida):
    
    src = entrada
    dst = os.path.dirname(os.path.abspath(__file__))+"/audios/"+salida+"{}".format('.wav')

    sound = AudioSegment.from_mp3(src)
    sound= sound.set_frame_rate(16000)
    sound.export(dst,format="wav")
    remove(entrada)


def transformar_audio_saludos(entrada,salida):
    
    src = entrada
    dst = os.path.dirname(os.path.abspath(__file__))+"/audios/saludos/"+salida+"{}".format('.wav')

    sound = AudioSegment.from_mp3(src)
    sound= sound.set_frame_rate(16000)
    sound.export(dst,format="wav")
    remove(entrada)

def transformar_audio_preguntas(entrada,salida):
    
    src = entrada
    dst = os.path.dirname(os.path.abspath(__file__))+"/audios/preguntas/"+salida+"{}".format('.wav')

    sound = AudioSegment.from_mp3(src)
    sound= sound.set_frame_rate(16000)
    sound.export(dst,format="wav")
    remove(entrada)
