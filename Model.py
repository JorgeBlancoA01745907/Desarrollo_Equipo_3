import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.util import ngrams
from sklearn.metrics import pairwise

def clean_file(document):
    with open(document, encoding="utf-8") as file:
        document1 = file.read().replace('\n', '')
        document1 = document1.replace(",","") #Eliminar comas
        document1 = document1.replace(".", "") #Eliminar puntos
        document1 = document1.replace("?", "") #Eliminar ?
        document1 = document1.replace("!", "") #Eliminar !
        document1 = document1.replace("(", "") #Eliminar (
        document1 = document1.replace(")", "") #Eliminar )
    print(document1)
    return document1

def make_unigram(document1):
    unigram = list(ngrams(document1.split(),1))
    return unigram
    
def stemmer(unigram):
    Lancaster_stemmer = LancasterStemmer()
    words = []
    for palabra in unigram:
        words.append((Lancaster_stemmer.stem(palabra[0])))
    return words

def create_corpus(words):
    corpus = list(dict.fromkeys(words))
    return corpus

def create_matrix(words1, words2):
    final_matrix = [words1, words2]
    return final_matrix

def create_big_corpus(corpus1, corpus2):
    big_corpus = corpus1 + corpus2
    big_corpus = list(dict.fromkeys(big_corpus))
    return big_corpus

def create_unigram_matrix(final_matrix, big_corpus):
    unigram_matrix = []
    for parrafo in final_matrix:
        mx = []
        for palabra_c in big_corpus:
            if palabra_c in parrafo:
                mx.append(1)
            else:
                mx.append(0)
        unigram_matrix.append(mx)
    
    return unigram_matrix

def cosine_evaluation(unigram_matrix):
    return pairwise.cosine_similarity(unigram_matrix)

document1 = clean_file("txt_prueba.txt")
unigram1 = make_unigram(document1)
words1 = stemmer(unigram1)
corpus1 = create_corpus(words1)
document2 = clean_file("txt_prueba_2.txt")
unigram2 = make_unigram(document2)
words2 = stemmer(unigram2)
corpus2 = create_corpus(words2)
final_matrix = create_matrix(words1, words2)
big_corpus = create_big_corpus(corpus1, corpus2)
unigram_matrix = create_unigram_matrix(final_matrix, big_corpus)
print(cosine_evaluation(unigram_matrix))
