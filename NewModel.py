import os
import glob
import logging
import string
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer, AutoModel
import torch
import nltk
from Model import TextProcessor
from tabulate import tabulate
from sklearn.metrics import roc_auc_score, roc_curve
nltk.download('stopwords')
nltk.download('punkt')

class similarityCalculation:
    def __init__(self, documents_dir: str, percentaje_simil: float, metric: str = 'cosine') -> None:
        self.lemmatizer = WordNetLemmatizer()
        self.documents_dir = documents_dir
        self.percentaje_simil = percentaje_simil
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = AutoTokenizer.from_pretrained("roberta-base")
        self.model = AutoModel.from_pretrained("roberta-base")
        self.metric = metric  # Añadido para seleccionar la métrica
        self.auc_list = []
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s\n%(message)s')

    def plagiarismDetection(self, input_file_path: str):
        files_and_content_processed = self.dataBaseProcessing()
        input_text = self._read_file(input_file_path)
        preprocessed_input_text = self._preprocess_text(input_text)
        
        most_similar_file, similarity_score = self.similarityComparison(input_file_path, preprocessed_input_text, files_and_content_processed)
        
        is_plagiarism = similarity_score >= self.percentaje_simil
        is_tp = 'TP' in os.path.basename(input_file_path)

        if is_plagiarism:
            return is_plagiarism, most_similar_file, similarity_score, is_tp
        
        return is_plagiarism, None, similarity_score, is_tp

    def similarityComparison(self, input_file_name: str, preprocessed_input_text: str, files_and_content: dict):
        input_embedding = self._get_embedding(preprocessed_input_text)
        best_score = float('-inf') if self.metric == 'cosine' else float('inf')
        most_similar_file = None

        for file_name, content in files_and_content.items():
            content_embedding = self._get_embedding(content)
            if self.metric == 'cosine':
                similarity = self._cosine_similarity(input_embedding, content_embedding)
                if similarity > best_score:
                    best_score = similarity
                    most_similar_file = file_name
            elif self.metric == 'euclidean':
                distance = self._euclidean_distance(input_embedding, content_embedding)
                if distance < best_score:
                    best_score = distance
                    most_similar_file = file_name

        # logging.debug(f'Archivo más similar: {most_similar_file} con un puntaje de {best_score}')
        # print(f"Plagiarism detected between {input_file_name} and {most_similar_file}")
        # print(f"Score: {best_score:.2f}")
        
        return most_similar_file, best_score

    def dataBaseProcessing(self) -> dict:
        files_and_content_processed = self._uploadDocuments(self.documents_dir)
        return files_and_content_processed

    def _preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(tokens)

    def evaluate_directory(self, evaluation_dir: str):

        evaluation_files = glob.glob(os.path.join(evaluation_dir, '*.txt'))
        
        print("\nResults:")

        for file in evaluation_files:
            is_plagiarism, similar_file, similarity_score, is_tp = self.plagiarismDetection(file)
            
            if is_plagiarism:
                similar_file= "originals/" + similar_file
                processor = TextProcessor(file, similar_file)
                result = processor.process()
                if result:
                    print(tabulate([result], headers="keys", tablefmt="pretty"))
                if result["Plagiarism"] == "Plagiarism detected":
                    self.auc_list.append(1)
                else:
                    self.auc_list.append(0)
            else:
                self.auc_list.append(0)

        # Datos de ejemplo con etiquetas reales
        labels = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        


        # Calcula el AUC-ROC
        auc = roc_auc_score(self.auc_list, labels)
        print(f"AUC-ROC: {auc:.2f}")

        # Genera la curva ROC
        fpr, tpr, thresholds = roc_curve(self.auc_list, labels)

        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic')
        plt.legend(loc="lower right")
        plt.show()

        return auc

    def _uploadDocuments(self, documents_dir: str) -> dict:
        files_and_content = {}
        txt_files = [f for f in os.listdir(documents_dir) if f.endswith('.txt')]
        for file_name in txt_files:
            try:
                with open(os.path.join(documents_dir, file_name), 'r', encoding='utf-8') as f:
                    content = f.read()
                    files_and_content[file_name] = self._preprocess_text(content)
                    logging.debug(f'Read file: {file_name}')
            except Exception as e:
                logging.error(f'Error al leer el archivo {file_name}: {e}')
        return files_and_content

    def _read_file(self, path: str) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            logging.error(f'Error al leer el archivo: {e}')
            content = ''
        return content

    def _get_embedding(self, text: str) -> torch.Tensor:
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

    def _cosine_similarity(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> float:
        return torch.nn.functional.cosine_similarity(tensor1, tensor2).item()

    def _euclidean_distance(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> float:
        return torch.dist(tensor1, tensor2).item()
