import re
import csv

names = ['Apple Braeburn', 'Apple Crimson Snow', 'Apple Golden', 'Apple Granny Smith', 'Apple Pink Lady', 'Apple Red', 'Apple Red Delicious', 'Apple Red Yellow', 'Apricot', 'Avocado', 'Avocado ripe', 'Banana', 'Banana Lady Finger', 'Banana Red', 'Beetroot', 'Blueberry', 'Cactus fruit', 'Cantaloupe', 'Cherry', 'Chestnut', 'Clementine', 'Cocos', 'Corn', 'Corn Husk', 'Cucumber Ripe', 'Dates', 'Eggplant', 'Ginger Root', 'Grape Blue', 'Grape Pink', 'Grape White', 'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Huckleberry', 'Kaki', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon', 'Lemon Meyer', 'Limes', 'Lychee', 'Mandarine', 'Mango', 'Mango Red', 'Mangostan', 'Maracuja', 'Melon Piel de Sapo', 'Mulberry', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepino', 'Pepper Green', 'Pepper Orange', 'Pepper Red', 'Pepper Yellow', 'Physalis', 'Physalis with Husk', 'Pineapple', 'Pineapple Mini', 'Pitahaya Red', 'Plum', 'Pomegranate', 'Pomelo Sweetie', 'Potato Red', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Salak', 'Strawberry', 'Strawberry Wedge', 'Tamarillo', 'Tangelo', 'Tomato', 'Watermelon']
labels =[]

with open('nutrition_data.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    print("Header:", reader.fieldnames)
    for nutrition_data in reader:
        nutrition_data['name'] = nutrition_data['name'].title()
        labels.append(nutrition_data['name'])

#print(names)
#print(labels)

label_to_name = {

}
for label in labels:
    label_to_name[label] = []
    for name in names:
        pattern = re.compile(fr'\b{label}\b', re.IGNORECASE)
        matches = pattern.findall(name)
        if matches:
            label_to_name[label].append(name)
            #print(f"The extracted word is: {matches[0]}")
        else:
            pass
#print(label_to_name)

JSON_ObjectChecker = {

}
for element in label_to_name:
    JSON_ObjectChecker[' '.join(label_to_name[element])] = element
print("")
print(JSON_ObjectChecker)

label_from_image_recognition = names
count = 0
for name in names:
    for key, label in JSON_ObjectChecker.items():
        if re.search(fr'\b{name}\b', key):
            print(re.search(fr'\b{name}\b', key))
            count = 0
            break
        count +=1
        print(count)
print(len(JSON_ObjectChecker))


import json


# Specify the file path where you want to save the JSON
json_file_path = 'united_results_(on).json'

# Save the dictionary to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(JSON_ObjectChecker, json_file)
print(len(JSON_ObjectChecker))
print(len(label_to_name))
print(f"JSON file '{json_file_path}' created successfully.")
