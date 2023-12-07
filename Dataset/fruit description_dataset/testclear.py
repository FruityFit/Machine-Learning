import json

fruitdesc_file_path = 'output.json'

with open(fruitdesc_file_path, 'r') as json_file:
    fruits_json = json.load(json_file)


allowed_keys = ['Apple', 'Avocado', 'Banana', 'Grape', 'Guava', 'Lemon', 'Mango', 'Orange', 'Peach', 'Pear', 'Strawberry', 'Watermelon']

data_dict = fruits_json

keys_to_remove = [key for key in data_dict.keys() if key not in allowed_keys]
for key in keys_to_remove:
    del data_dict[key]


new_json_data = json.dumps(data_dict)

print(new_json_data)

with open('output.json', 'w') as output_file:
    output_file.write(new_json_data)

print("Data telah disimpan ke output.json")