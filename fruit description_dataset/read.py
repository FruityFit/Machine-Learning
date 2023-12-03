fruits = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Beetroot', 'Blueberry', 'Cactus', 'Cantaloupe', 'Cherry', 'Chestnut', 'Clementine', 'Corn', 'Cucumber', 'Dates', 'Eggplant', 'Ginger Root', 'Grape', 'Grapefruit', 'Guava', 'Huckleberry', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon', 'Limes', 'Lychee', 'Mango', 'Melon', 'Mulberry', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepper', 'Pepper Orange', 'Pineapple', 'Plum', 'Pomegranate', 'Pomelo', 'Potato', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Strawberry', 'Tangelo', 'Tomato', 'Watermelon', 'Cocos', 'Kaki', 'Mandarine', 'Mangostan', 'Maracuja', 'Pepino', 'Physalis', 'Physalis With Husk', 'Pitahaya Red', 'Salak', 'Tamarillo']
fruit_description = {}
state  = ''
with open("data.txt", 'r') as data:
    print(data)
    n_index = 0
    for i in data:
        if len(i) == 1 or len(i) == 8 or len(i) == 5:
            continue
        else:
            if len(i) <= 47:
                if '/' not in i:
                    words = i.split()
                    for word in words:
                        if word.title() in fruits:
                            fruit_description[word.title()] = ''
                            state = word.title()
                            break
                        elif word == "Ginger":
                            fruit_description[i[:2].title()] = ''
                            state = i[:2].title()
                            break
                    n_index +=1
            
            else:
                modified_string = i.replace("\n", "")
                if len(fruit_description[state]) == 0:
                    fruit_description[state] = modified_string
                else:
                    fruit_description[state] += " "
                    fruit_description[state] += modified_string
             

assert n_index == 29
print(fruit_description)
print(len(fruit_description))

import json
json_string = json.dumps(fruit_description)
file_path = "output.json"

# Save the JSON string to the file
with open(file_path, 'w') as json_file:
    json_file.write(json_string)

print(f"JSON data saved to {file_path}")

import csv
csv_file_path = "output.csv"
data = fruit_description

# Convert the dictionary to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Description'])
    for name, description in data.items():
        csv_writer.writerow([name, description])
print(f"CSV data saved to {csv_file_path}")
