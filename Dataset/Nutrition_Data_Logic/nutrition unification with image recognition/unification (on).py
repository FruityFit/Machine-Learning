import re
import csv

names = ['Apple', 'Avocado', 'Banana', 'Grape', 'Guava', 'Lemon', 'Mango', 'Orange', 'Peach', 'Pear', 'Strawberry', 'Watermelon']
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
