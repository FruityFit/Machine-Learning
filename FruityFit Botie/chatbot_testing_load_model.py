import unittest
from ChatBot_Deep_Learning import BotieDeepLearning
Chatbot = BotieDeepLearning('intent.json')
Chatbot.load_model('chatbot/model/chatbot_model_2.h5')

class TestTestingTemplate(unittest.TestCase):
    def test_model(self):
        instance = Chatbot
        self.assertIsNotNone(instance.model)

    def test_response_category1(self):
        _,tag = Chatbot.generate_response_classification("Berikan saran untuk membuat jus?")
        self.assertEqual(tag, "Recommendation")

    def test_response_category2(self):
        _,tag = Chatbot.generate_response_classification("jus enak apa yang dapat dibuat hari ini?")
        self.assertEqual(tag, "Recommendation")

    def test_response_category2(self):
        _,tag = Chatbot.generate_response_classification("menurut anda bagaimana jus itu yang enak ")
        self.assertEqual(tag, "Recommendation")
    
    def test_response_category3(self):
        _,tag = Chatbot.generate_response_classification("menurut anda bagaimana jus itu yang enak ")
        self.assertEqual(tag, "Recommendation")

    def test_response_nutrrition(self):
        input_texts = [
            "Apakah buah apel memiliki banyak nutrisi?",
            "Beritahu saya tentang nutrisi buah blueberry",
            "Rasa apa saja yang bisa saya temukan di cherry?",
            "keuntungan buah jeruk bagi tubuh karena memiliki nutrisi apa?",
            "buah melon dilihat dari sisi kesehatan memiliki nutrisi?"
        ]

        expected_tag = "Nutrition"

        for input_text in input_texts:
            _, tag = Chatbot.generate_response_classification(input_text)
            self.assertEqual(tag, expected_tag)

    def test_response_category_greeting(self):
        greeting_patterns = [
            "Hi",
            "Halo!",
            "Ada orang kah",
            "Salam kenal",
            "Halo, aku ",
            "P",
            "Assalamualaikum",
            "Hai",
            "hey",
            "heyho",
            "Hey"
        ]

        expected_tag = "greeting"

        for pattern in greeting_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)

    def test_response_category_goodbye(self):
        goodbye_patterns = [
            "Bye",
            "Dadah",
            "Sampai jumpa!",
            "See you later",
            "Dah"
        ]

        expected_tag = "goodbye"

        for pattern in goodbye_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)

    def test_response_category_thanks(self):
        thanks_patterns = [
            "Thanks",
            "Thank you",
            "Terima kasih!",
            "Makasih",
            "Terimakasih",
            "thankyou"
        ]

        expected_tag = "thanks"

        for pattern in thanks_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)

    def test_response_category_types(self):
        types_patterns = [
            "apa sih jenis buah di Indonesia?",
            "Jenis buah di Indonesia ada apa aja?",
            "Jenis buah ada apa aja?",
            "sebutkan buah buah yang ada di indonesia",
            "buah buah apa aja yang ada di Indonesia"
        ]

        expected_tag = "types"

        for pattern in types_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)

    def test_response_category_benefit(self):
        benefit_patterns = [
            "apa keuntungan memakan buah AZ ?",
            "kegunaan buah az bagi kesehatan ?",
            "mengapa kita harus memakan buah az?",
            "mengapa buah az sangat berguna bagi kesehatan?"
        ]

        expected_tag = "benefit"

        for pattern in benefit_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)

    def test_response_category_trends(self):
        trends_patterns = [
            "Apa trend buah yang terkenal di Indonesia sekarang?",
            "Apa buah yang diminati anak anak muda ?",
            "Sebutin dong beberapa buah terkenal yang ada di Indonesia"
        ]

        expected_tag = "trends"

        for pattern in trends_patterns:
            _, tag = Chatbot.generate_response_classification(pattern)
            self.assertEqual(tag, expected_tag)


    
if __name__ == '__main__':
    unittest.main()