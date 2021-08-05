import pickle
import json
import random
import numpy as np
from .date_and_time import current_Datetime
from .data import bag_of_words
from .model_trainer import model_making
from tensorflow.keras.models import load_model

with open("./intents.json") as file:
    intents_json = json.load(file)

try:
    with open("./data.pkl", "rb") as f:
        words, classes, train_x, train_y = pickle.load(f)
    model = load_model('./chatbot_model.h5')

except:
    model_making()
    model = load_model('./chatbot_model.h5')


main = '<div class="bot-inbox inbox"><div class="icon"><i class="fas fa-user"></i></div><div class="msg-header"><p>'


def string_manipulation(string):
    string = str(string)
    last = '</p></div></div>'
    string = string.split("<break>")
    first = string[0]
    string.pop(0)
    blank = ""
    first = main + first + last
    for items in string:
        item = main + items + last
        blank += item
    final = first + blank
    return final


def getResponse(user_input):
    user_input = str(user_input)
    end_tag = '</p></div></div>'

    if user_input.isascii() == False:
        return main + "Please do not use emojis." + end_tag

    results = model.predict(np.array([bag_of_words(user_input, words)]))[0]
    results_index = np.argmax(results)
    tag = classes[results_index]
    list_of_intents_json = intents_json['intents']
    not_found = ["Sorry I didn't get that. Try to rephrase what you just said",
                 "Something asked wrong", "My bad, ask something else"]
    dict1 = {"Time": current_Datetime()}

    if results[results_index] > 0.9:
        for i in list_of_intents_json:
            if (i['tag'] == tag):
                result = random.choice(i['responses'])
                if (i['tag'] in dict1):
                    output = dict1[i['tag']]
                    result = string_manipulation(output)
                elif "<break>" in result:
                    result = string_manipulation(result)
                else:
                    result = main + result + end_tag
                return result
    else:
        result = main + random.choice(not_found) + end_tag
        return result


getResponse("Hello")
