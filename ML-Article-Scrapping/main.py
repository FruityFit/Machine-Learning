from googlesearch import search
from bs4 import BeautifulSoup
import requests
import json
import os 

class Botie_Google_Bot():
    def __init__(self):
        self.google_search = search

    # Botie Recommended Article
    def get_the_links(self, input_user):
        unique_links = []
        for link in self.google_search(input_user, lang='in'):
            if link not in unique_links:
                unique_links.append(link)
        return unique_links

    def recommended_article(self, data):
        recommended_links = self.get_the_links(data)
        recommended_article = []
        for link in recommended_links:
            response = requests.get(link)
            if str(response) == "<Response [200]>":
                soup = BeautifulSoup(response.text, 'html.parser')
                # print(soup.head)

                title_tag = soup.head.title
                title_text = title_tag.get_text() if title_tag else "No title found"
                article = {
                    'title' : title_text.split(' - ')[0] if ' - ' in title_text else title_text.split(' | ')[0] if  ' | ' in title_text else title_text ,
                    'url' :link
                    }
                recommended_article.append(article)
        return recommended_article

Botie_aricle_recommended = Botie_Google_Bot()
def get_history_user(fruit_history="Apel anggur Jeruk"):
    return Botie_aricle_recommended.recommended_article(f"cara membuat jus {fruit_history}")

classes_indo=['Apel', 'Alpukat', 'Pisang', 'Anggur', 'Jambu', 'Lemon', 'Mangga', 'Jeruk', 'Persik', 'Pir', 'Stroberi', 'Semangka']
hasil = []
# if __name__ == "__main__":
#     for i in classes_indo:
#         print(i)
#         x = get_history_user(i)
#         existing_data.extend(hasil)


#     with open('output.json', 'w') as json_file:
#         json.dump(hasil, json_file, indent=2)  
#     print(hasil)
existing_data = []
for i in classes_indo:
    x =get_history_user(i)
    existing_data.extend(x)
    time.sleep(300)
print(existing_data)
with open('output.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=2)      
        
    
