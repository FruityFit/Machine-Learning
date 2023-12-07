import time
fruit_description = [
    "Apel merupakan buah yang kaya akan mineral penting, termasuk zat besi dan kalium. Kedua mineral ini memberikan manfaat signifikan dalam mendukung kesehatan tulang. Kandungan zat besi dalam apel membantu meningkatkan transportasi oksigen ke seluruh tubuh, termasuk sel-sel tulang. Sementara itu, kalium berperan penting dalam menjaga keseimbangan cairan dalam tubuh dan meningkatkan kepadatan mineral tulang, yang pada gilirannya dapat meningkatkan kekuatan dan kepadatan tulang. Dengan mengonsumsi apel secara teratur, Anda dapat mendukung kesehatan tulang dan mendapatkan manfaat mineral-mineral penting ini untuk menjaga sistem rangka tubuh tetap kuat dan sehat.",
    ""

]
fruits = ['Apple', 'Avocado', 'Banana', 'Grape', 'Guava', 'Lemon', 'Mango', 'Orange', 'Peach', 'Pear', 'Strawberry', 'Watermelon']

# for i in fruits:
#     print(i + " pengertian + manfaat  2 paragraf" )
n = 0  
for i in fruits:
    if i =="Mulberry":
        n+= 1
        break
    n+= 1
print(len(fruits) -  n)