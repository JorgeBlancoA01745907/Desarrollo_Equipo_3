import nltk
from nltk.stem import LancasterStemmer
from nltk.util import ngrams
from sklearn.metrics import pairwise
# Importation of the libraries needed for the code

def clean_file(document):
# This function is use to clean the .txt removing points and other things 
    with open(document, encoding="utf-8") as file:
        document = file.read()
        #Optimization done by removing the other .replace() functions
        for char in ",.?!()":
            document = document.replace(char, '')
    print("\n")
    print(document)
    print("\n")
    return document

def make_unigram(document):
    # This function devides the .txt in unigrams (separetes it by words)
    unigram = list(ngrams(document.split(),1))
    return unigram
    
def stemmer(unigram):
    # This function reduces each unigram into its core 
    Lancaster_stemmer = LancasterStemmer()
    words = []
    for palabra in unigram:
        words.append((Lancaster_stemmer.stem(palabra[0])))
    return words

def create_corpus(words):
    """
    This function creates a corpus with the words of the .txt
    corpus means that it will only have unique words
    """
    corpus = list(dict.fromkeys(words))
    return corpus

def create_matrix(stems1, stems2):
    """
    This function creates a matrix with the words of the .txt
    this words have been stemmed and are unique
    """
    final_matrix = [stems1, stems2]
    return final_matrix

def create_big_corpus(corpus1, corpus2):
    """
    This function creates a big corpus with the corpus of the two .txt
    removing the repeated words
    """
    big_corpus = corpus1 + corpus2
    big_corpus = list(dict.fromkeys(big_corpus))
    return big_corpus

def create_unigram_matrix(final_matrix, big_corpus):
    """
    This function creates a matrix with the final_matrix 
    and the big_corpus previously created,
    this matrix is made with 1s and 0s
    """
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
    """
    This function evaluates the cosine similarity of the unigram_matrix
    When the cosine similarity is 1, the two .txt are the same, bigger the
    cosine similarity, means that the .txt analyzed are more similar
    """
    return pairwise.cosine_similarity(unigram_matrix)

def results(cosine_evaluation):
    """
    This function prints the similarity of the two .txt analyzed
    as a percentage with two decimal points if the percentage is above
    55% the two .txt are considered similar and therefor plagiarism.
    A message indicating plagiarism is printed
    """
    print("The similarity of the two documents is: {:.2f}%".format(cosine_evaluation[0][1]*100), "\n", "The two documents provided are similar and therefor plagiarism is present.\n" if cosine_evaluation[0][1] > 0.55 else "The two documents are not similar, there's no plagiarism present.\n")
    
def main():
    """
    This function is the main function of the code, it calls all the functions
    and prints the cosine similarity of the two .txt analyzed
    """

    # Clean documents
    document1 = clean_file("org-023.txt")
    document2 = clean_file("FID-005.txt")

    # Create unigram
    unigram1 = make_unigram(document1)
    unigram2 = make_unigram(document2)
    
    # Stemming
    stems1 = stemmer(unigram1)
    stems2 = stemmer(unigram2)
    
    # Create corpus
    corpus1 = create_corpus(stems1)
    corpus2 = create_corpus(stems2)
    big_corpus = create_big_corpus(corpus1, corpus2)

    # Create matrix
    final_matrix = create_matrix(stems1, stems2)
    unigram_matrix = create_unigram_matrix(final_matrix, big_corpus)

    # Cosine evaluation, the result is printed
    print(cosine_evaluation(unigram_matrix))
    results(cosine_evaluation(unigram_matrix))

if __name__ == "__main__":
    main()
