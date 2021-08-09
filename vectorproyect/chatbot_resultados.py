import random
import json
import pickle
import numpy as np
import nltk
#nltk.download('punkt')
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from tensorflow import keras
lemmatizer = WordNetLemmatizer()
intents = json.loads(open("/home/pi/Desktop/vector/vectorproyect/intents.json",encoding="utf8", errors='ignore').read())

words = pickle.load(open("/home/pi/Desktop/vector/vectorproyect/words.pk1","rb"))
classes = pickle.load(open("/home/pi/Desktop/vector/vectorproyect/classes.pk1","rb"))

model= keras.models.load_model("chatbot_model.h5")


def clean_up_sentence(sentence):
      sentence_words = nltk.word_tokenize(sentence)
      sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
      return sentence_words

def bag_of_words(sentence):
  sentence_words=clean_up_sentence(sentence)
  bag=[0] * len(words)
  for w in sentence_words:
    for i, word in enumerate(words):
      if word == w:
        bag[i]=1
  return np.array(bag)


def predict_class(sentence):
  bow = bag_of_words(sentence)
  res = model.predict(np.array([bow]))[0]
  ERROR_TRESHOLD = 0.25
  results = [[i,r] for i, r in enumerate(res) if r > ERROR_TRESHOLD]

  results.sort(key=lambda x: x[1],reverse=True)
  return_list= []
  for r in results:
    return_list.append({"intent":classes[r[0]]})
  return return_list
def get_response(intents_list,intents_json):
  tag = intents_list[0]["intent"]
  list_of_intents=intents_json["intents"]
  for i in list_of_intents:
    if i["tag"] == tag:
      result= random.choice(i["responses"])
      break
  return result

def hablar_chatbot(texto):
  
  message=texto
  ints=predict_class(message)
  res= get_response(ints,intents)
  return res
  
  
print(hablar_chatbot("hola"))