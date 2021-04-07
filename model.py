import tensorflow as tf
import numpy as np
import random

'''
Things to consider:
1. Use average or weighted average to represent user's history?
2. Have different models each contribute to a set of candidates? (ensemble)
3. 
'''


utility_dimensions = 
num_of_candidates = 


class article_2_vector(tf.keras.Model):
    def __init__(self):
        self.input = tf.keras.layers.Input(shape=(), dtype=tf.string)
        self.bert_preprocessing = 
        self.bert_encoder =
        self.dense =
        
    
    def call(self):



class recommendation_model(tf.keras.Model):

    def __init__(self):
        super(recommendation_model, self).__init__()
        #compress user vector into the dimension that is the same as the embedding dimension for an article
        #self.input_vector = tf.keras.layers.Input(shape=(), dtype=tf.int64)

        self.dense1 = tf.keras.layers.Dense()
    

        #dense layers
        ......
        

        self.embedding = tf.keras.layers.Dense(num_of_candidates, name='article_embedding')
        #calculate the dot products of user vector and each article embedding
        
        self.dot_product = tf.keras.layers.Dot()
        self.densex = tf.keras.layers.Dense(1, activation='softmax')

        self.densex+1 = tf.keras.layers.Dense()

        #dense layers
        ......

        self.densex+y = Dense(utility_dimensions, activation=None)
        


    def call(self, inputs):
        #lstm
        input1 = inputs[0]
        
        user_embedding = self.dense1(input1)

        ......

        dot_products = self.dot_product([self.embedding, user_vector])

        #teacher-student
        #optimization: write a custom dense layer that stores the dot products in a max heap
        candidates = self.dense2(dot_products)
        

        #input2 includes metrics of articles including average read time, time since publishing, number of likes/dislikes......
        #look up in our database
        input2 = 

        #concatenate with other features if needed

        '''
        final_input2 = []
        for candidate in candidates:
            final_input2.append(tf.concat([candidate, input2], axis=1))
        final_input2 = np.array(final_input2)
        '''
        
        #dense layers
        result = self.densex+1(final_input2)
        ......

        result = self.densex+y(result)
        return result
        


'''
model = recommendation_model()
test = np.array([[1, 2]])
output = model(inputs=[test, []])
model.save('model')
model = tf.keras.models.load_model('model')
old_weights = model.get_layer('article_embedding').get_weights()[0]
print(old_weights)
print(f' old weights are: {old_weights}')
new_articles = np.array([[1, 1], [1, 1]])
new_weights = tf.concat([old_weights, new_articles], axis=0)
model.get_layer('article_embedding').reshape(4)
model.get_layer('article_embedding').set_weights(new_weights)
print(f' new weights are: {model.get_layer("article_embedding").get_weights()[0]}')
'''

        
def preprocess_articles(article):

    sequences = article.splitlines()

    sequence = ''

    #randomly select sequences until the length is larger than 512
    while len(sequence) < 512:
        sequence += random.randint(len(sequences))
    
    return sequence




def encode_articles():

    #load the article_2_vector model
    model = tf.keras.models.load_model()

    #retrieve new articles
    dictionary = {}

    for article in articles:
        sequence = preprocess_articles(article)
        dictionary.update({article, model.predict(sequence)})

    for article, embedding in dictionary.items():
        #save embedding into the database item that corresponds to the article




def update_model(new_articles):
    #retrieve the latest model from storage bucket
    model = tf.keras.models.load_model()
    
    #train the model using the data gathered between now and the latest update
    model.fit(data)

    #concatenate the old embedding matrix with the newly added articles
    old_weights = model.get_layer('article_embedding').get_weights()[0]
    new_weights = tf.concat([old_weights, new_articles], axis=0)
    model.get_layer('article_embedding').set_weights(new_weights)

    #push the new model to storage
    model.save()


def calculate_utililty(utility_vector):


def make_predictions(uid, ):
    #retrieve the latest model from storage bucket
    #create the user vector
    recommender = model.load()
    results = model.predict(user_embedding)

    heap = max_heap()

    for result in results:
        utility = calculate_utililty(result)
        #push into heap
    
    #return the top n results
    i = 0
    for i in range():
    
    return 

    





    







