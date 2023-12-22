import requests
from googletrans import Translator

class Botie_Google_Bot:
    def __init__(self):
        self.api_key = 'API_KEY'
        self.youtube_url = 'https://www.googleapis.com/youtube/v3/search'
        self.part = 'snippet'
        self.type = 'video'

        self.search_engine_id = 'CX_ID'
        self.search_url = 'https://www.googleapis.com/customsearch/v1'

        self.ninja_api_key = 'API_KEY'
        self.ninja_url = 'https://api.api-ninjas.com/v1/nutrition'

    def get_the_video_info(self, query='resep jus'):
        params = {
            'part': self.part,
            'key': self.api_key,
            'type': self.type,
            'q': query
        }
        response = requests.get(self.youtube_url, params=params)
        return response.json()

    def get_the_video_links(self, input_user):
        video_information = self.get_the_video_info(input_user)
        links = []

        if 'items' in video_information:
            for item in video_information['items']:
                video_id = item['id']['videoId']
                video_url = f'https://www.youtube.com/watch?v={video_id}'
                links.append(video_url)

        return links

    def get_content(self, query):
        params = {
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': query
        }

        try:
            response = requests.get(self.search_url, params=params)
            data = response.json()
            return data

        except Exception as e:
            print(f"An error occurred: {e}")

    def get_web_link(self, user_input):
        web_links = self.get_content(user_input)
        result = []
        if 'items' in web_links:
            for item in web_links['items']:
                title = item['title']
                link = item['link']
                result.append({title : link})
        return result

    def get_nutrition(self, data):
        english_data = self.translate_to_lang(data, 'en')
        api_url = f'{self.ninja_url}?query={english_data}'
        headers = {'X-Api-Key': self.ninja_api_key}

        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if len(data) != 0:
                    data[0]['name'] = self.translate_to_lang(data[0]['name'], 'id')
                    return data
                else:
                    return { 'calories': 53.4, 'serving_size_g': 100.0, 'fat_total_g': 0.2, 'fat_saturated_g': 0.0, 'protein_g': 0.3, 'sodium_mg': 1, 'potassium_mg': 11, 'cholesterol_mg': 0, 'carbohydrates_total_g': 13.8, 'fiber_g': 2.4, 'sugar_g': 10.3}


        except Exception as e:
            print(f"An error occurred: {e}")

    def get_nutrition_in_english(self, data):
        english_data = self.translate_to_lang(data, 'en')
        api_url = f'{self.ninja_url}?query={english_data}'
        headers = {'X-Api-Key': self.ninja_api_key}

        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if len(data) != 0:
                    return data
                else:
                    return []


        except Exception as e:
            print(f"An error occurred: {e}")

    def translate_to_lang(self, user_input, language_code):
        translator = Translator()
        translated_response = translator.translate(user_input, dest=language_code).text
        return translated_response

# Example usage:
if __name__ == "__main__":
    bot = Botie_Google_Bot()
    video_links = bot.get_the_video_links('resep jus blueberry')
    for link in video_links:
       print(link)
    #bot.get_content("tipe buah di Indonesia")
    #bot.get_web_link("trend buah apa yang sekarang populer")
    #bot.get_nutrition("Apakah buah apel memiliki banyak nutrisi?")



    

