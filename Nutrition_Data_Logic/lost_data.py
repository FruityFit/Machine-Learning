import csv

fruit_lost_data =  ['Cocos', 'Kaki', 'Mandarine', 'Mangostan', 'Maracuja', 'Pepino', 'Physalis', 'Physalis with Husk', 'Pitahaya Red', 'Salak', 'Tamarillo']
fruit_lost_data_list = []
filename = 'bard_data.csv'
with open(filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    print("Header:", reader.fieldnames)
    for nutrition_data in reader:
        nutrition_data['name'] = nutrition_data['name'].lower()
        fruit_lost_data_list.append(nutrition_data)
        print(fruit_lost_data_list)


print(len(fruit_lost_data_list))

assert len(fruit_lost_data_list) == len(fruit_lost_data) 

with open("nutrition_data.csv", mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    if file.tell() == 0:
        writer.writeheader()
    for fruit in fruit_lost_data_list:
        writer.writerow(fruit)

print(f"Data appended to nutrition_data.csv successfully.")
