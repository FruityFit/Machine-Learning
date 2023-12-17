import json
import numpy as np
import tensorflow as tf
import nltk
import requests
import urllib.parse

json_path = 'intent.json'
nltk.download('all')

class BotieDeepLearning():
    def __init__(self, json_path, model=None):
        with open(json_path) as intention:
            self.intents = json.load(intention)
        self.model = None 
        self.words = []
        self.classes = []
        self.docs = []
        self.ignore=['!','?','.....',',','.']
        self.lemmatize = None
        self.train_x = None
        self.train_y = None     
    
    def preprocessing_data(self):
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                token = nltk.word_tokenize(pattern)
                self.words.extend(token)
                self.docs.append((token,intent['tag']))
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.lemmatizer = nltk.WordNetLemmatizer()
        self.words = [self.lemmatizer.lemmatize(token.lower()) for token in self.words if token not in self.ignore]
        self.words = sorted(list(set(self.words)))
       

    def create_train_list(self):
        self.preprocessing_data()
        training_list = []
        output_nan = [0] * len(self.classes)

        for doc in self.docs:
            bow = []
            pattern = doc[0]
            pattern = [self.lemmatizer.lemmatize(sentence.lower()) for sentence in pattern]
            for word in self.words:
                bow.append(1) if word in pattern else bow.append(0)

            output = list(output_nan)
            output[self.classes.index(doc[1])] = 1
            bow_array = np.array(bow)
            output_array = np.array(output)

            training_list.append((bow_array, output_array))

        training = np.array(training_list)
        train_x = np.stack(list(training[:,0]))
        train_y = np.stack(list(training[:,1]))
        self.train_x = train_x
        self.train_y = train_y
        return train_x, train_y

    def nlp_model(self):
        train_x, train_y = self.create_train_list()
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(8, input_shape=(len(train_x[0]), )),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(len(train_y[0]), activation='softmax')
        ])
        self.model.summary()
        return self.model

    def save_model(self):
        self.model.save('chatbot/model/chatbot_model_2.h5')

    def train(self):
        if self.model is None:
            self.nlp_model()
        self.model.compile(loss=tf.keras.losses.categorical_crossentropy, optimizer='adam', metrics=['acc'])
        self.model.fit(self.train_x, self.train_y, epochs=1000, batch_size=8)
        print("=========== TRAINING IS SUCCESS ===========")
    
    def clean_sentence(self,sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words if word not in self.ignore]
        sentence_words = sorted(list(set(sentence_words)))
        return sentence_words

    def bag_of_words(self, sentence, show_details=False):
        sentence_words = self.clean_sentence(sentence)
        bag = [0] * len(self.words)
        for s in sentence_words:
            for i, w in enumerate(self.words):
                if w == s:
                    bag[i] = 1

        arrBag = np.array(bag)
        return np.stack(arrBag)
    
    def generate_response_classification(self, sentence):
        input_data = self.bag_of_words(sentence, self.words)
        input_data = input_data.reshape(1, input_data.shape[0])
        results = self.model.predict(input_data)[0]
        results_index = np.argmax(results)
        tag = self.classes[results_index]
        return results, tag
        
    
    def load_model(self, model_path):
        self.create_train_list()
        load_model = tf.keras.models.load_model('chatbot/model/chatbot_model_2.h5')
        load_model.summary()
        self.model = load_model
        self.train()

        pass


    

        
if __name__ == "__main__":
    print(np.__version__)
    Chatbot = BotieDeepLearning(json_path)
    #print(Chatbot.model)
    #Chatbot.create_train_list()
    Chatbot.train()
    #Chatbot.clean_sentence("p")
    #Chatbot.load_model('chatbot/model/chatbot_model_2.h5')
    print(Chatbot.bag_of_words('P').shape)
    print(Chatbot.generate_response_classification("Berikan saran untuk membuat jus?"))
    Chatbot.save_model()