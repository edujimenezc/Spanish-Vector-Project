import pyttsx3
voz = pyttsx3.init()
voz.setProperty("rate", 145)
contador=3
voz.save_to_file('¿Tú quién eres, cómo quieres que te llame?', f'conf'+str(contador)+'.wav')

voz.runAndWait()

