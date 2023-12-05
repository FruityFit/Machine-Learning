fruits = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Beetroot', 'Blueberry', 'Cactus', 'Cantaloupe', 'Cherry', 'Chestnut', 'Clementine', 'Corn', 'Cucumber', 'Dates', 'Eggplant', 'Ginger Root', 'Grape', 'Grapefruit', 'Guava', 'Huckleberry', 'Kiwi', 'Kohlrabi', 'Kumquats', 'Lemon', 'Limes', 'Lychee', 'Mango', 'Melon', 'Mulberry', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepper', 'Pepper Orange', 'Pineapple', 'Plum', 'Pomegranate', 'Pomelo', 'Potato', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Strawberry', 'Tangelo', 'Tomato', 'Watermelon', 'Cocos', 'Kaki', 'Mandarine', 'Mangostan', 'Maracuja', 'Pepino', 'Physalis', 'Physalis With Husk', 'Pitahaya Red', 'Salak', 'Tamarillo']
fruit_description = {}
state  = ''
with open("data2.txt", 'r') as data:
    print(data)
    n_index = 0
    for i in data:
        if len(i) == 1 or len(i) == 8 or len(i) == 5:
            continue
        else:
            if len(i) <= 47:
                if '/' not in i:
                    print(i)
                    words = i.split()
                    print(words.index('pengertian'))
                    print(words.count)
                   
                    fruit_description[' '.join(words[:(words.index('pengertian'))]).title()] = ''
                    state = ' '.join(words[:(words.index('pengertian'))]).title()
                            
                    n_index +=1
            
            else:
                modified_string = i.replace("\n", "")
                if len(fruit_description[state]) == 0:
                    fruit_description[state] = modified_string
                else:
                    fruit_description[state] += " "
                    fruit_description[state] += modified_string
             



fruit_description["Physalis With Husk"] = "Physalis with husk, atau physalis dengan kulit atau kelopaknya, adalah variasi dari buah physalis yang dikenal dengan ciri khas kelopak kering dan transparan yang melindungi buahnya. Meskipun sering ditemukan sebagai hiasan dalam presentasi makanan, physalis with husk dapat dikonsumsi dan memiliki rasa yang manis dan sedikit asam. Kulit luar yang kering dan tipis melindungi buahnya dari kontaminan, menjadikannya pilihan yang higienis dan menarik dalam penyajian makanan. Di beberapa budaya, physalis with husk digunakan dalam pengobatan tradisional untuk beberapa masalah kesehatan, meskipun bukti ilmiah mendukung manfaat kesehatannya masih terbatas. Manfaat kesehatan physalis with husk melibatkan kandungan nutrisi dan potensi efek positifnya pada tubuh. Buah ini mengandung vitamin C, vitamin A, serat, dan antioksidan seperti karotenoid. Vitamin C mendukung sistem kekebalan tubuh dan kesehatan kulit, sedangkan serat membantu menjaga kesehatan pencernaan. Antioksidan dalam physalis with husk dapat membantu melawan radikal bebas, melindungi sel-sel tubuh dari kerusakan oksidatif, dan memiliki potensi efek antiinflamasi. Meskipun manfaat kesehatannya perlu diteliti lebih lanjut, kehadiran nutrisi dan senyawa bioaktif dalam physalis with husk membuatnya menjadi pilihan buah yang menarik untuk dimasukkan dalam pola makan sehari-hari." 
print(fruit_description)
print(len(fruit_description))

fruit_check = set()
fruit_check_data = set(fruits[29:])
for i in fruit_description:
    fruit_check.add(i.title())
print(fruit_check_data - fruit_check)





import json

file_path = "output.json"
with open(file_path, "r") as json_file:
    data_json = json.load(json_file)

data_json.update(fruit_description)

# Save the JSON string to the file
with open(file_path, 'w') as json_file:
    json_file.write(json.dumps(data_json))

print(f"JSON data saved to {file_path}")

import csv
csv_file_path = "output.csv"
data = fruit_description

# Convert the dictionary to CSV
with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for name, description in data.items():
        csv_writer.writerow([name, description])
print(f"CSV data saved to {csv_file_path}")