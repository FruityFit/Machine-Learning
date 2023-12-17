import google.generativeai as palm
from googletrans import Translator

class BotieBotGenerativeAI():
    def __init__(self):
        self.palm = palm.configure(api_key="AIzaSyAJsMNXM0gZtxKYLx_qnjHAFV-V_2O_r9A")
        self.defaults = {
                        'model': 'models/chat-bison-001',
                        'temperature': 0.25,
                        'candidate_count': 1,
                        'top_k': 40,
                        'top_p': 0.95,
                        }
        self.context = "juice"
        self.message = []
    
    def return_examples(self):
        examples = [
            [
                "apple juice ",
                " Apple juice is a drink made from the pressed juice of apples. It is a popular beverage in many parts of the world, and is often served as a breakfast drink or as a snack. Apple juice is a good source of vitamins A and C, and is also a good source of fiber. It is a low-calorie beverage, and is a good source of antioxidants. Apple juice is a healthy and refreshing drink that can be enjoyed by people of all ages.\n\nHere are some of the health benefits of apple juice:\n\n* Apple juice is a good source of vitamins A and C. Vitamin A is important for vision, skin, and immune function. Vitamin C is an antioxidant that helps protect the body from damage caused by free radicals.\n* Apple juice is a good source of fiber. Fiber is important for digestive health and can help lower cholesterol levels.\n* Apple juice is a low-calorie beverage. It is a good choice for people who are trying to lose weight or maintain a healthy weight.\n* Apple juice is a good source of antioxidants. Antioxidants help protect the body from damage caused by free radicals. Free radicals are unstable molecules that can damage cells, leading to diseases such as cancer and heart disease.\n* Apple juice is a healthy and refreshing drink that can be enjoyed by people of all ages. \n\n To make apple juice, you will need:\n\n* 6 apples, peeled, cored, and sliced\n* 1 cup of water\n* 1/2 spoon of sugar\nInstructions:\n\n1. In a large pot, combine the apples, water, and sugar.\n2. Bring to a boil over medium heat, then reduce heat and simmer for 15 minutes, or until the apples are soft.\n3. Remove from heat and let cool slightly.\n4. Pour the apple mixture into a blender or food processor and blend until smooth.\n5. Strain the apple juice through a fine-mesh sieve to remove any solids.\n6. Pour the apple juice into a cup and refrigerate until chilled.\n7. Serve and enjoy!\n\nTips:\n\n* You can use any type of apples you like for this recipe.\n* If you like your apple juice sweeter, you can add more sugar to taste.\n* Apple juice can be stored in the refrigerator for up to 1 week. \n"
            ],
            [
                "blueberry juice",
                " Blueberry juice is a delicious and healthy drink that is made from the juice of blueberries. Blueberries are a good source of vitamins A and C, and they are also a good source of fiber. Blueberries are also a good source of antioxidants, which can help protect the body from damage caused by free radicals.\n\nBlueberry juice is a low-calorie beverage, and it is a good choice for people who are trying to lose weight or maintain a healthy weight. Blueberry juice is also a good source of potassium, which is an important mineral for heart health.\n\nBlueberry juice is a refreshing and healthy drink that can be enjoyed by people of all ages. It is a good choice for breakfast, lunch, dinner, or as a snack. Blueberry juice can also be used in smoothies, cocktails, and other recipes.\n\nHere is a recipe for blueberry juice:\n\nIngredients:\n\n* 10 blueberries\n* 1 cup of water\n* 1/2 spoon of sugar\nInstructions:\n\n1. In a blender or food processor, combine the blueberries, water, sugar.\n2. Blend until smooth.\n3. Strain the blueberry juice through a fine-mesh sieve to remove any solids.\n4. Pour the blueberry juice into a cup and refrigerate until chilled.\n5. Serve and enjoy!\n\nTips:\n\n* You can use any type of blueberries you like for this recipe.\n* If you like your blueberry juice sweeter, you can add more sugar to taste.\n* Blueberry juice can be stored in the refrigerator for up to 1 week. "
            ],
            [
                "orange juice",
                "source of vitamins A and C, and is also a good source of potassium. Orange juice is a low-calorie beverage, and is a good choice for people who are trying to lose weight or maintain a healthy weight. Orange juice is also a good source of antioxidants.\n\nOrange juice is a refreshing and healthy drink that can be enjoyed by people of all ages. It is a good choice for breakfast, lunch, dinner, or as a snack. Orange juice can also be used in smoothies, cocktails, and other recipes.\n\nHere is a recipe for orange juice:\n\nIngredients:\n\n* 4 oranges\n\nInstructions:\n\n1. Wash the oranges thoroughly.\n2. Cut the oranges in half and squeeze the juice into a glass.\n3. Enjoy!\n\nTips:\n\n* You can use any type of oranges you like for this recipe. \n* Orange juice can be stored in the refrigerator for up to 3 days. "
            ],
            [
                "grape juice",
                " Grape juice is a drink made from the juice of grapes. It is a popular beverage in many parts of the world, and is often served as a breakfast drink or as a snack. Grape juice is a good source of vitamins A and C, and is also a good source of fiber. It is a low-calorie beverage, and is a good source of antioxidants. Grape juice is a healthy and refreshing drink that can be enjoyed by people of all ages.\n\nHere are some of the health benefits of grape juice:\n\n* Grape juice is a good source of vitamins A and C. Vitamin A is important for vision, skin, and immune function. Vitamin C is an antioxidant that helps protect the body from damage caused by free radicals.\n* Grape juice is a good source of fiber. Fiber is important for digestive health and can help lower cholesterol levels.\n* Grape juice is a low-calorie beverage. It is a good choice for people who are trying to lose weight or maintain a healthy weight.\n* Grape juice is a good source of antioxidants. Antioxidants help protect the body from damage caused by free radicals. Free radicals are unstable molecules that can damage cells, leading to diseases such as cancer and heart disease.\n* Grape juice is a healthy and refreshing drink that can be enjoyed by people of all ages.\n\nTo make grape juice, you will need:\n\n*  grapes, washed and destemmed\n* 1 cup of water\n* 1/2 spoon of sugar\nInstructions:\n\n1. In a large pot, combine the grapes, water, sugar.\n2. Bring to a boil over medium heat, then reduce heat and simmer for 15 minutes, or until the grapes are soft.\n3. Remove from heat and let cool slightly.\n4. Pour the grape mixture into a blender or food processor and blend until smooth.\n5. Strain the grape juice through a fine-mesh sieve to remove any solids.\n6. Pour the grape juice into a cup and refrigerate until chilled.\n7. Serve and enjoy!\n\nTips:\n\n* You can use any type of grapes you like for this recipe. \n* If you like your grape juice sweeter, you can add more sugar to taste.\n* Grape juice can be stored in the refrigerator for up to 1 week. "
            ],
            [
                "melon juice",
                " Melon juice is a delicious and refreshing drink that is made from the juice of melons. Melons are a good source of vitamins A and C, and they are also a good source of fiber. Melons are also a good source of antioxidants, which can help protect the body from damage caused by free radicals.\n\nMelon juice is a low-calorie beverage, and it is a good choice for people who are trying to lose weight or maintain a healthy weight. Melon juice is also a good source of potassium, which is an important mineral for heart health.\n\nMelon juice is a refreshing and healthy drink that can be enjoyed by people of all ages. It is a good choice for breakfast, lunch, dinner, or as a snack. Melon juice can also be used in smoothies, cocktails, and other recipes.\n\nHere is a recipe for melon juice:\n\nIngredients:\n\n* a melon, peeled, seeded, and diced\n* 1 cup of water\n* 1/2 spoon of sugar\n\nInstructions:\n\n1. In a blender or food processor, combine the melon, water, sugar.\n2. Blend until smooth.\n3. Strain the melon juice through a fine-mesh sieve to remove any solids.\n4. Pour the melon juice into a cup and refrigerate until chilled.\n5. Serve and enjoy!\n\nTips:\n\n* You can use any type of melon you like for this recipe.\n* If you like your melon juice sweeter, you can add more sugar to taste.\n* Melon juice can be stored in the refrigerator for up to 1 week. "
            ],
            [
                "carrot juice",
                " Carrot juice is a delicious and nutritious drink that is made from the juice of carrots. Carrots are a good source of vitamins A and C, and they are also a good source of fiber. Carrots are also a good source of antioxidants, which can help protect the body from damage caused by free radicals.\n\nCarrots are a low-calorie vegetable, and carrot juice is a low-calorie beverage. It is a good choice for people who are trying to lose weight or maintain a healthy weight. Carrot juice is also a good source of potassium, which is an important mineral for heart health.\n\nCarrots are a root vegetable that is native to Europe and Asia. They are a member of the Apiaceae family, which also includes celery, parsley, and fennel. Carrots are typically orange in color, but they can also be white, yellow, red, or purple.\n\nCarrots are a good source of vitamins A and C, as well as fiber. They are also a good source of antioxidants, which can help protect the body from damage caused by free radicals. Carrots are also a good source of potassium, which is an important mineral for heart health.\n\nCarrots can be eaten raw or cooked. They can be used in salads, soups, stews, and other dishes. Carrot juice is a popular drink that is made from the juice of carrots. Carrot juice is a good source of vitamins A and C, as well as fiber. It is also a good source of antioxidants.\n\nHere is a recipe for carrot juice:\n\nIngredients:\n\n* 6 carrots, peeled and chopped\n* 1 cup of water\n* 1/2 spoon of sugar\n*\n\nInstructions:\n\n1. In a blender or food processor, combine the carrots, water, sugar\n2. Blend until smooth.\n3. Strain the carrot juice through a fine-mesh sieve to remove any solids.\n4. Pour the carrot juice into a cup and refrigerate until chilled.\n5. Serve and enjoy!\nTips:\n\n* You can use any type of carrots you like for this recipe.\n* If you like your carrot juice sweeter, you can add more sugar to taste.\n* Carrot juice can be stored in the refrigerator for up to 1 week. "
            ]
        ]
        return examples

    def add_messages(self):
        self.message.append("NEXT REQUEST")

    def generate_chat(self, data):
        self.add_messages()
        response = palm.chat(
            **self.defaults,
            context=self.context,
            examples=self.return_examples(),
            messages=data
        )
        return response.last # Response of the AI to your most recent request

    def translate_chat_to_indonesian(self, data):
        generated_response = self.generate_chat(data)

        # Use Google Translate to translate the response to Indonesian
        translator = Translator()
        translated_response = translator.translate(generated_response, dest='id').text

        return translated_response


    def chat(self, data):
        return self.translate_chat_to_indonesian(data)



if __name__ == "__main__":
    botie = BotieBotGenerativeAI()
    print(botie.chat("watermelon juice"))
    print(botie.chat("apple juice"))     

     
