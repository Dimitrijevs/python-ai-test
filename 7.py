import fasttext
import fasttext.util
import os
from numpy import dot
from numpy.linalg import norm

# Install fasttext if you haven't already:
# pip install fasttext

# Download the Latvian FastText model if it's not already downloaded
if not os.path.exists('cc.lv.300.bin'):
    print("Downloading Latvian FastText model...")
    fasttext.util.download_model('lv', if_exists='ignore')  # Downloads 'cc.lv.300.bin'

# Load the model
print("Loading the model...")
ft = fasttext.load_model('cc.lv.300.bin')

# Optionally reduce the model size for faster computation
print("Reducing the model dimensions...")
fasttext.util.reduce_model(ft, 100)  # Reduces dimensions to 100

# Define the words
word1 = 'māja'
word2 = 'dzīvoklis'
word3 = 'jūra'

# Get the word vectors
vec1 = ft.get_word_vector(word1)
vec2 = ft.get_word_vector(word2)
vec3 = ft.get_word_vector(word3)

# Function to compute cosine similarity
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# Compute similarities
sim1 = cosine_similarity(vec1, vec2)  # māja and dzīvoklis
sim2 = cosine_similarity(vec1, vec3)  # māja and jūra
sim3 = cosine_similarity(vec2, vec3)  # dzīvoklis and jūra

# Print the results
print(f"Cosine similarity between '{word1}' and '{word2}': {sim1}"
print(f"Cosine similarity between '{word1}' and '{word3}': {sim2}")
print(f"Cosine similarity between '{word2}' and '{word3}': {sim3}")
