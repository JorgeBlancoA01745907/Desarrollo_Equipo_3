import nltk
from nltk.stem import LancasterStemmer
from nltk.util import ngrams
from sklearn.metrics import pairwise
from nltk.tokenize import word_tokenize
# Importation of the libraries needed for the code

class TextProcessor:
    """
    This class contains all the functions needed to preprocess, analyze and compare the .txt files
    """
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
    
    def clean_file(self, document):
    # This function is use to clean the .txt removing points and other things 
        with open(document, encoding="utf-8") as file:
            document = file.read().lower()
            #Optimization done by removing the other .replace() functions and just using the for loop
            for char in ",.¿?¡!()@#$":
                document = document.replace(char, '')
            # Remove extra spaces, this was added after running the tests
            document = ' '.join(document.split())
        #print("\n")
        #print(document)
        #print("\n")
        return document

    def make_unigram(self, document):
        # This function devides the .txt in unigrams (separetes it by words)
        unigram = list(ngrams(document.split(),1))
        return unigram
        
    def stemmer(self, unigram):
        # This function reduces each unigram into its core 
        Lancaster_stemmer = LancasterStemmer()
        words = []
        for palabra in unigram:
            if palabra and palabra[0]:  # Check if palabra is not None and contains at least one element
                words.append((Lancaster_stemmer.stem(palabra[0])))
        return words

    def create_corpus(self, stems):
        """
        This function creates a corpus with the words of the .txt
        corpus means that it will only have unique words
        """
        corpus = list(dict.fromkeys(stems))
        return corpus

    def create_matrix(self, stems1, stems2):
        """
        This function creates a matrix with the words of the .txt
        this words have been stemmed and are unique
        """
        final_matrix = [stems1, stems2]
        return final_matrix

    def create_big_corpus(self, corpus1, corpus2):
        """
        This function creates a big corpus with the corpus of the two .txt
        removing the repeated words
        """
        big_corpus = corpus1 + corpus2
        big_corpus = list(dict.fromkeys(big_corpus))
        return big_corpus

    def create_unigram_matrix(self, final_matrix, big_corpus):
        """
        This function creates a matrix with the final_matrix 
        and the big_corpus previously created,
        this matrix is made with 1s and 0s
        """
        # Optimized by removing the for loop and using list comprehension
        # changed it due to the test results
        unigram_matrix = []
        for paragraph in final_matrix:
            unigram_matrix.append([1 if word in paragraph else 0 for word in big_corpus])
        return unigram_matrix

    def cosine_evaluation(self, unigram_matrix):
        """
        This function evaluates the cosine similarity of the unigram_matrix
        When the cosine similarity is 1, the two .txt are the same, bigger the
        cosine similarity, means that the .txt analyzed are more similar
        """
        return pairwise.cosine_similarity(unigram_matrix)

    def results(self, cosine_evaluation):
        """
        This function prints the similarity of the two .txt analyzed
        as a percentage with two decimal points if the percentage is above
        55% the two .txt are considered similar and therefor plagiarism.
        A message indicating plagiarism is printed
        """
        similarity_percentage = cosine_evaluation[0][1] * 100
        similarity_message = "The two documents provided are similar and therefore plagiarism is present.\n" if cosine_evaluation[0][1] >= 0.55 else "The two documents are not similar, there's no plagiarism present.\n"
    
        result_message = "\nThe similarity of the two documents is: {:.2f}%\n{}".format(similarity_percentage, similarity_message)
        return result_message
        

    def process(self):
        """
        This function is the main function of the class TextProcessor
        This function calls all the other functions in the class to analyze the .txt
        """

        # Clean documents
        document1 = self.clean_file("org-023.txt")
        document2 = self.clean_file("FID-005.txt")

        # Create unigram
        unigram1 = self.make_unigram(document1)
        unigram2 = self.make_unigram(document2)
        
        # Stemming
        stems1 = self.stemmer(unigram1)
        stems2 = self.stemmer(unigram2)
        
        # Create corpus
        corpus1 = self.create_corpus(stems1)
        corpus2 = self.create_corpus(stems2)
        big_corpus = self.create_big_corpus(corpus1, corpus2)

        # Create matrix
        final_matrix = self.create_matrix(stems1, stems2)
        unigram_matrix = self.create_unigram_matrix(final_matrix, big_corpus)

        # Cosine evaluation
        similarity_score = self.cosine_evaluation(unigram_matrix)
        print(self.results(similarity_score))
        return similarity_score

def main():
    processor = TextProcessor("org-023.txt", "FID-005.txt")
    processor.process()

if __name__ == "__main__":
    main()
