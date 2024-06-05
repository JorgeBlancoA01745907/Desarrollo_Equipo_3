import os
import numpy as np
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity

# Function to load text files from a directory
def load_texts_from_directory(directory):
    texts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                texts[filename] = file.read()
    return texts

# Load the texts
directory = './documents'  # Set the path to your .txt files
texts = load_texts_from_directory(directory)

# Load pre-trained BERT model and tokenizer
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Encode the texts using BERT
encoded_texts = {filename: model.encode(text) for filename, text in texts.items()}

# Function to compute cosine similarity
def compute_similarity(texts, encoded_texts):
    filenames = list(texts.keys())
    num_files = len(filenames)
    similarities = np.zeros((num_files, num_files))
    for i in range(num_files):
        for j in range(i, num_files):
            if i == j:
                similarities[i, j] = 1.0
            else:
                sim = util.pytorch_cos_sim(encoded_texts[filenames[i]], encoded_texts[filenames[j]]).item()
                similarities[i, j] = sim
                similarities[j, i] = sim
    return similarities, filenames

# Compute the similarity matrix
similarity_matrix, filenames = compute_similarity(texts, encoded_texts)

# Function to identify the types of plagiarism based on heuristics
def identify_plagiarism_types(text1, text2):
    # Dummy implementation for demonstration; in practice, this would involve more sophisticated analysis
    if text1 == text2:
        return "Exact match"
    elif set(text1.split()) == set(text2.split()):
        return "Disorder the sentences"
    else:
        return "Paraphrasing"

# Analyze the similarities and determine the types of plagiarism
plagiarism_reports = []
threshold = 0.8  # Set a threshold for detecting plagiarism

for i in range(len(filenames)):
    for j in range(i + 1, len(filenames)):
        if similarity_matrix[i, j] > threshold:
            plagiarism_type = identify_plagiarism_types(texts[filenames[i]], texts[filenames[j]])
            report = {
                'file1': filenames[i],
                'file2': filenames[j],
                'similarity': similarity_matrix[i, j],
                'plagiarism_type': plagiarism_type
            }
            plagiarism_reports.append(report)

# Print the plagiarism reports
for report in plagiarism_reports:
    print(f"Plagiarism detected between {report['file1']} and {report['file2']}")
    print(f"Similarity: {report['similarity']:.2f}")
    print(f"Type of Plagiarism: {report['plagiarism_type']}")
    print()

# You can further refine the identify_plagiarism_types function to detect specific types of plagiarism more accurately
