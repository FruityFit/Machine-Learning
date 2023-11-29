import requests
import csv


fruit_list = ['Apple Braeburn', 'Apple Crimson Snow', 'Apple Golden', 'Apple Granny Smith', 'Apple Pink Lady', 'Apple Red', 'Apple Red Delicious', 'Apple Red Yellow', 'Apricot', 'Avocado', 'Avocado ripe', 'Banana', 'Banana Lady Finger', 'Banana Red', 'Beetroot', 'Blueberry', 'Cactus fruit', 'Cantaloupe', 'Cherry', 'Chestnut', 'Clementine', 'Cocos', 'Corn', 'Corn Husk', 'Cucumber Ripe', 'Dates', 'Eggplant', 'Ginger Root', 'Grape Blue', 'Grape Pink', 'Grape White', 'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Huckleberry', 'Kaki', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon', 'Lemon Meyer', 'Limes', 'Lychee', 'Mandarine', 'Mango', 'Mango Red', 'Mangostan', 'Maracuja', 'Melon Piel de Sapo', 'Mulberry', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepino', 'Pepper Green', 'Pepper Orange', 'Pepper Red', 'Pepper Yellow', 'Physalis', 'Physalis with Husk', 'Pineapple', 'Pineapple Mini', 'Pitahaya Red', 'Plum', 'Pomegranate', 'Pomelo Sweetie', 'Potato Red', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Salak', 'Strawberry', 'Strawberry Wedge', 'Tamarillo', 'Tangelo', 'Tomato', 'Watermelon']
nutrition_data_list = []
lost_data = []
same_data = set()
count = 0

for fruit in fruit_list:
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(fruit)
    response = requests.get(api_url, headers={'X-Api-Key': 'pPzJD+fOb2o2JMf1zVI2aA==DFrXiqIJWnmzuqCJ'})
    if response.status_code == requests.codes.ok:
        nutrition_data = response.json()
        print(f"{count}. {fruit} = {nutrition_data}")
        if len(nutrition_data) == 0:
            lost_data.append(fruit)
            


        else:
            if nutrition_data[0]['name'] not in same_data:
                nutrition_data_list.append(nutrition_data[0])
                same_data.add(nutrition_data[0]['name'])
                print(same_data)
                print(nutrition_data)
        count += 1
    else:
        print("Error:", response.status_code, response.text)
print("")
print("")
print(f"lost data in csv file is {lost_data}")
print(count)
assert count == 81 # check if fruit total response okey is already 80

file_name = "nutrition_data.csv"
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=nutrition_data_list[0].keys())
    writer.writeheader()
    writer.writerows(nutrition_data_list)
print(f"CSV file '{file_name}' created successfully.")


