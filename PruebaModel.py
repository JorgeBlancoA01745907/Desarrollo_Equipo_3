import os
import glob
import logging
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer, AutoModel
import torch
import nltk
nltk.download('stopwords')
nltk.download('punkt')

class similarityCalculation:
    """
    Clase para calcular la similitud entre documentos de texto y detectar plagio.
    
    Atributos:
    ----------
    lemmatizer : WordNetLemmatizer
        Objeto para lematizar palabras.
    documents_dir : str
        Ruta a la carpeta que contiene los archivos de texto.
    percentaje_simil : float
        Umbral de similitud para determinar el plagio.
    stop_words : set
        Conjunto de palabras vacías (stopwords) en inglés.
    """

    def __init__(self, documents_dir: str, percentaje_simil: float) -> None:
        """
        Inicializa la clase similarityCalculation con la ruta de los archivos de texto
        y el umbral de similitud.
        
        Parámetros:
        -----------
        documents_dir : str
            Ruta a la carpeta que contiene los archivos de texto.
        percentaje_simil : float
            Umbral de similitud para determinar el plagio.
        """
        self.lemmatizer = WordNetLemmatizer()
        self.documents_dir = documents_dir
        self.percentaje_simil = percentaje_simil
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = AutoTokenizer.from_pretrained("roberta-base")
        self.model = AutoModel.from_pretrained("roberta-base")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s\n%(message)s')
        
    def plagiarismDetection(self, input_file_path: str):
        """
        Detecta plagio comparando un archivo de entrada con los archivos en la base de datos.
        
        Parámetros:
        -----------
        input_file_path : str
            Ruta del archivo de entrada a verificar.
        
        Retorna:
        --------
        is_plagiarism : bool
            True si se detecta plagio, False en caso contrario.
        most_similar_file : str
            Nombre del archivo más similar en caso de plagio.
        similarity_score : float
            Puntaje de similitud del archivo más similar.
        is_tp : bool
            True si 'TP' está en el nombre del archivo, False en caso contrario.
        """
        files_and_content_processed = self.dataBaseProcessing()
        print(files_and_content_processed.pop(input_file_path))
        input_text = self._read_file(input_file_path)
        preprocessed_input_text = self._preprocess_text(input_text)
        
        most_similar_file, similarity_score = self.similarityComparison(preprocessed_input_text, files_and_content_processed)
        
        is_plagiarism = similarity_score >= self.percentaje_simil
        is_tp = 'TP' in os.path.basename(input_file_path)

        if similarity_score >= self.percentaje_simil:
            is_plagiarism = True
            return is_plagiarism, most_similar_file, similarity_score, is_tp
        
        return is_plagiarism
    
    def similarityComparison(self, preprocessed_input_text: str, files_and_content: dict):
        """
        Compara el texto preprocesado de entrada con los textos en la base de datos.
        
        Parámetros:
        -----------
        preprocessed_input_text : str
            Texto de entrada preprocesado.
        files_and_content : dict
            Diccionario con los nombres de archivos y sus contenidos preprocesados.
        
        Retorna:
        --------
        most_similar_file : str
            Nombre del archivo más similar.
        similarity_score : float
            Puntaje de similitud del archivo más similar.
        """
        input_embedding = self._get_embedding(preprocessed_input_text)
        max_similarity = 0
        most_similar_file = None

        for file_name, content in files_and_content.items():
            content_embedding = self._get_embedding(content)
            similarity = self._cosine_similarity(input_embedding, content_embedding)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_file = file_name

        logging.debug(f'Archivo más similar: {most_similar_file} con una similitud de {max_similarity}')
        
        return most_similar_file, max_similarity
    
    def dataBaseProcessing(self) -> dict:
        """
        Procesa los archivos de texto en la base de datos.
        
        Retorna:
        --------
        files_and_content_processed : dict
            Diccionario con los nombres de archivos y sus contenidos preprocesados.
        """
        files_and_content_processed = self._uploadDatabase(self.documents_dir)
        return files_and_content_processed
    
    def _preprocess_text(self, text: str) -> str:
        """
        Preprocesa el texto realizando lematización, eliminación de signos de puntuación,
        conversión a minúsculas, eliminación de stopwords y números.
        
        Parámetros:
        -----------
        text : str
            Texto a preprocesar.
        
        Retorna:
        --------
        str
            Texto preprocesado.
        """
        text = text.lower()  # Convertir a minúsculas
        text = text.translate(str.maketrans('', '', string.punctuation))  # Eliminar signos de puntuación
        tokens = word_tokenize(text)  # Tokenizar
    
    def evaluate_directory(self, evaluation_dir: str):
        """
        Aplica la detección de plagio a todos los documentos en un directorio específico.
        
        Parámetros:
        -----------
        evaluation_dir : str
            Ruta al directorio que contiene los archivos de texto a evaluar.
        
        Retorna:
        --------
        auc : float
            Medida de desempeño basada en el conteo de True Positive, True Negative, False Positive y False Negative.
        """
        tp_count = 0
        tn_count = 0
        fp_count = 0
        fn_count = 0

        evaluation_files = glob.glob(os.path.join(evaluation_dir, '*.txt'))

        for file in evaluation_files:
            is_plagiarism = self.plagiarismDetection(file)
            
            is_tp = 'TP' in os.path.basename(file)

            if is_tp:
                if is_plagiarism:
                    tp_count += 1
                else:
                    fn_count += 1
            else:
                if is_plagiarism:
                    fp_count += 1
                else:
                    tn_count += 1

        results = {
            'True Positive': tp_count,
            'True Negative': tn_count,
            'False Positive': fp_count,
            'False Negative': fn_count
        }

        if (tp_count + fn_count) == 0:
            tpr = 0
        else:
            tpr = tp_count / (tp_count + fn_count)

        if (fp_count + tn_count) == 0:
            fpr = 0
        else:
            fpr = fp_count / (fp_count + tn_count)

        auc = (1 + tpr - fpr) / 2

        print(f'AUC: {auc}')

        return auc
    
    def dataBaseProcessing(self) -> dict:
        """
        Procesa los archivos de texto en la base de datos.
        
        Retorna:
        --------
        files_and_content_processed : dict
            Diccionario con los nombres de archivos y sus contenidos preprocesados.
        """
        files_and_content_processed = self._uploadDocuments(self.documents_dir)
        return files_and_content_processed
    
    def _uploadDocuments(self, documents_dir: str) -> dict:
        """
        Sube los archivos de texto de la base de datos y los preprocesa.
        
        Parámetros:
        -----------
        documents_dir : str
            Ruta a la carpeta que contiene los archivos de texto.
        
        Retorna:
        --------
        files_and_content : dict
            Diccionario con los nombres de archivos y sus contenidos preprocesados.
        """
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
        """
        Lee el contenido de un archivo de texto.
        
        Parámetros:
        -----------
        path : str
            Ruta del archivo a leer.
        
        Retorna:
        --------
        str
            Contenido del archivo.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            logging.error(f'Error al leer el archivo: {e}')
            content = ''
        return content
    
    def _get_embedding(self, text: str) -> torch.Tensor:
        """
        Calcula la incrustación (embedding) del texto utilizando RoBERTa.
        
        Parámetros:
        -----------
        text : str
            Texto para el cual se calculará la incrustación.
        
        Retorna:
        --------
        torch.Tensor
            Incrustación del texto.
        """
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, max_length=512)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)  # Mean pooling



