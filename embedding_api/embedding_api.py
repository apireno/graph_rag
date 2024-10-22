import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS


embeddings_dict = {}
vector_size = 0

#load the embedding model into a dict
with open("glove.6B.50d.txt", 'r', encoding="utf-8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector
        if vector_size==0:
            vector_size = len(vector)

#converts text to a vector based on the model loaded into the dict embeddings_dict
def sentence_to_vec(sentence):
    words = sentence.lower().split()
    vectors = [embeddings_dict[w] for w in words if w in embeddings_dict]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(vector_size)

app = Flask(__name__)
CORS(app)
#the api endpoint that returns the vector of the incoming variable "text"
@app.route("/",methods=["GET","POST"])
def post_embedding():
    text_to_convert = ""
    if request.method == 'POST': 
        content = request.json
        text_to_convert = content['text'] 
    else:
        text_to_convert = request.args['text']
    return sentence_to_vec(text_to_convert).tolist()
