import json
import re

json_file_path1 = 'united_results_(o1).json'
json_file_path2 = 'united_results_(on).json'

with open(json_file_path1, 'r') as json_file:
    o1 = json.load(json_file)
with open(json_file_path1, 'r') as json_file:
    on = json.load(json_file)

print(type(o1))
print(type(on))

def find_label_o1(element, json_data=o1):
    return json_data.get(element, 'data not found')
    

def find_label_on(element, json_data=on):
    for key, label in json_data.items():
        if re.search(fr'\b{element}\b', key):
            return label
    return 'data not found'

print(find_label_o1('Apple Braeburn'))
print(find_label_on('Apple Braeburn'))

print(find_label_o1('Walnut'))
print(find_label_on('Walnut'))


import csv

def get_nutrition_data(fruit_name):
    print(fruit_name)
    with open('nutrition_data.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for nutrition_data in reader:
            if nutrition_data['name'].title() == fruit_name:
                return nutrition_data
        return 'data not found'

print(get_nutrition_data(find_label_o1('Apple Braeburn')))
print(get_nutrition_data(find_label_on('Apple Braeburn')))
print(get_nutrition_data(find_label_o1('Watermelon')))
print(get_nutrition_data(find_label_on('Watermelon')))