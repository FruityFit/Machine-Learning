from ChatBot_Deep_Learning  import BotieDeepLearning
from Botie_GenerativeAI import BotieBotGenerativeAI
from Botie_search_bot import Botie_Google_Bot

import random
import requests
import json 
import re
from googletrans import Translator
json_path = 'intent.json'

class Botie:
    def __init__(self):
        self.text_classification = BotieDeepLearning('intent.json')
        self.text_classification.load_model('chatbot/model/chatbot_model_2.h5')
        self.generative_ai = BotieBotGenerativeAI()
        self.google_bot = Botie_Google_Bot()
        with open(json_path) as intention:
            self.intents = json.load(intention)

        self.tropical_fruit = ["alpukat", "belimbing", "buah naga", "durian", "jambu biji", "jeruk", "jeruk bali", "kelengkeng", "langsat", "manggis", "markisa", "nanas", "nangka", "pepaya", "pisang", "rambutan", "sawo", "salak", "srikaya", "sukun", "tamarindo", "vanili"]
        self.subtropical_fruit = ["apel", "anggur", "ceri", "delima", "mangga", "melon", "peach", "pir", "stroberi", "tomat"]
        self.import_fruit = [ "avocado", "blackcurrant", "blueberry", "cranberry", "fig", "kiwi", "lemon", "lychee", "mandarin", "passionfruit", "papaya", "pomelo", "quince", "raspberry", "rhubarb", "starfruit", "tangerine", "watermelon"]

        self.en_tropical_fruit = ["avocado", "starfruit", "dragon fruit", "durian", "guava", "orange", "Bali orange", "longan", "duku", "mangosteen", "passion fruit", "pineapple", "jackfruit", "papaya", "banana", "rambutan", "sapodilla", "salak", "soursop", "breadfruit", "tamarind", "vanilla"]
        self.en_subtropical_fruit = ["apple", "grape", "cherry", "pomegranate", "mango", "melon", "peach", "pear", "strawberry", "tomato"]
        self.en_import_fruit = [ "avocado", "blackcurrant", "blueberry", "cranberry", "fig", "kiwi", "lemon", "lychee", "mandarin", "passionfruit", "papaya", "pomelo", "quince", "raspberry", "rhubarb", "starfruit", "tangerine", "watermelon"]


        self.translator = Translator()


    def Botie_text_classification(self, user_chat):
        return self.text_classification.generate_response_classification(user_chat)

    def answer_based_text_classification(self, user_chat):
        results = self.Botie_text_classification(user_chat)
        print(results)
        list_index = {'greeting': 0, 'goodbye': 1, 'thanks': 2, 'types': 3, 'Recommendation': 4, 'Nutrition': 5, 'benefit': 6, 'trends': 7}
        category = results[1]
        
        # try:
        if category == 'greeting' or category == 'goodbye' or category == 'thanks':
            response = self.regard(list_index[category])
        elif category == 'types':
            response = self.types(list_index[category])
        elif category == 'Recommendation':
            response = self.Recommendation(list_index[category], user_chat)
        elif category == 'Nutrition':
            response = self.Nutrition(list_index[category], user_chat)
        elif category == 'benefit':
            response = self.benefit(list_index[category], user_chat)
        elif category == 'trends':
            response = self.trends(list_index[category], user_chat)
        # except Exception as err:
        #     print(err)
        #     response = 'Maaf aku tidak bisa memahami hal ini'  # Handle
        return response
    
    def regard(self, index):
        return random.choice(self.intents['intents'][index]['responses'])
    
    def Recommendation(self, index, user_chat):
        response = random.choice(self.intents['intents'][index]['responses']) + "\n"
        user_fruit = self.google_bot.get_nutrition_in_english(re.sub(r'[!()-\[\]{};:\'"\\,<>./?@#$%^&*_~]', '', user_chat))
        string_input_data = ''
        if len(user_fruit) != 0:
            for fruit in user_fruit:
                string_input_data += fruit['name']
                string_input_data += " "
        if string_input_data == "juice ":
            all_fruits = self.tropical_fruit + self.subtropical_fruit + self.import_fruit
            random_fruit = random.choice(all_fruits)
            string_input_data = random_fruit
            string_input_data = string_input_data + " juice"
        #print(string_input_data)

        try: 
            LLM_predict = self.generative_ai.chat(string_input_data)
            response +=  LLM_predict
            youtube_url = self.google_bot.get_the_video_links(string_input_data)
            response += "\n link yang direcomendasikan adalah sebagai berikut \n"
            response += youtube_url[1] 
        except:
            response += "adalah jus apel"

        return response




    def types(self, index):
        response = random.choice(self.intents['intents'][index]['responses']) 
        all_fruits = self.tropical_fruit + self.subtropical_fruit + self.import_fruit
        max_count = 5
        count = min(max_count, len(all_fruits))
        random_fruits = random.sample(all_fruits, count)
        fruit_set = set(random_fruits)
        print(fruit_set)
        for fruit in fruit_set:
            response += f" {fruit},"

        return response[:-1]

    def Nutrition(self, index, user_input):
        response_templates = random.choice(self.intents['intents'][index]['responses'])
        nutritions_infor = self.google_bot.get_nutrition(re.sub(r'[!()-\[\]{};:\'"\\,<>./?@#$%^&*_~]', '', user_input))
        nutritions_infor_len = len(nutritions_infor)
        index = 0
        for nutrition_info in nutritions_infor:
            response = re.sub(r'AZ', nutrition_info['name'], response_templates)
            response += f"\nKalori: {nutrition_info['calories']}\nUkuran Porsi: {nutrition_info['serving_size_g']}g\nLemak Total: {nutrition_info['fat_total_g']}g\nProtein: {nutrition_info['protein_g']}g\nKarbohidrat: {nutrition_info['carbohydrates_total_g']}g\nSerat: {nutrition_info['fiber_g']}g\nGula: {nutrition_info['sugar_g']}g\n"
            if index != nutritions_infor_len - 1:
                response += "\n&"         
        return response
    
    def benefit(self, index, user_chat):
        translate_to_eng  = self.translate_to_lang(user_chat, "en")
        LLM_predict = self.generative_ai.generate_chat(translate_to_eng)
        response =  self.translate_to_lang(LLM_predict, "id")
        return response


    def trends(self, index, user_chat):
        response = random.choice(self.intents['intents'][index]['responses'])
        get_web_link = self.google_bot.get_web_link(user_chat)
        if len(get_web_link)  != 0:
            for web_link in  get_web_link[1]:
                response += f" {get_web_link[1][web_link]}"
                response += f" dengan judul artikel {web_link}"        
        return response
    
    def translate_to_lang(self, user_input, language_code):
        translated_response = self.translator.translate(user_input, dest=language_code).text
        return translated_response

    def chat(self):
        while True:
            user_input = str(input("User: "))
            print(f"Botie: {self.answer_based_text_classification(user_input)}")



if __name__ == "__main__":
    chatbot = Botie()
    print(chatbot.Botie_text_classification("jus enak apa yang dapat dibuat hari ini?"))
    print(chatbot.answer_based_text_classification("Hi"))
    print(chatbot.answer_based_text_classification("Thanks"))
    print(chatbot.answer_based_text_classification("Bye"))
    #print(chatbot.answer_based_text_classification("Nutrisi apa saja yang bisa saya temukan di cherry?"))
    #print(chatbot.answer_based_text_classification('Apa trend buah yang terkenal di Indonesia sekarang?'))
    #print(chatbot.answer_based_text_classification('apa sih jenis buah di Indonesia?'))
    #print(chatbot.answer_based_text_classification("apa keuntungan memakan buah anggur ?"))
    #print(chatbot.answer_based_text_classification("apa keuntungan memakan buah anggur ?"))

    print(chatbot.answer_based_text_classification("Berikan saran untuk membuat jus apel pls?"))
    print(chatbot.answer_based_text_classification("Berikan saran untuk membuat jus?"))
    print(chatbot.answer_based_text_classification("jus enak apa yang dapat dibuat hari ini?"))