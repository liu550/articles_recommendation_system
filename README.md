# articles_recommendation_system
A hypothetical articles recommendation system (imagine I am working on such a system for WeChat, Medium, etc.)

# crawler.py
A program that crawls the article websites using multi-threading and BFS.

# model.py
The recommendation system based on BERT and neural network. Its structure is the following:

# Model 1 - BERT encoding

'''Input layer'''                   Random setences of articles

Preprocessing layer           BERT preprocessing layer

Encoding layer                BERT encoding layer

Dense layers (optional)       Reduce the dimension of the article embedding vector if needed

Output layer                  n-dimensional article embedding vector

# Model 2 - neural network recommender

Input layer                   concatenation of (1) n-dimensional user vector representing the average his past reading and search history and (2) other                                           characteristics of the user such as age and location
Dense layers                  reduce the dimension of the input down to n

Dense layer                   Multiply the matrix of all article embeddingd by the input to this layer

Selection layer (optional)    Select the top m results among the output of the previous layer (the top m artcicles that the user is most likely to like)

Dense layers                  reduce the dimension of the input down to u (utility dimension)

Output layer                  u-dimensional vector with each element representing a measurable metric about the interaction between the user and a article (reading                               time, like, etc.)
