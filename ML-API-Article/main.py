from googlesearch import search
from bs4 import BeautifulSoup
import requests

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
    return Botie_aricle_recommended.recommended_article(f"cara membuat jus{fruit_history}")


from flask import Flask, jsonify

app = Flask(__name__)
Botie_aricle_recommended = Botie_Google_Bot()

@app.route('/get_recommended_article/<fruit_history>', methods=['GET'])
def get_recommended_article(fruit_history):
    recommended_articles = Botie_aricle_recommended.recommended_article(f"cara membuat jus {fruit_history}")
    return jsonify(recommended_articles)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
