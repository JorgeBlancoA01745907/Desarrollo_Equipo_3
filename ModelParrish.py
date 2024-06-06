
import os
import logging
import string
import torch
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer, AutoModel
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
        dict
            Diccionario con el nombre del archivo plagiado (si lo hay) y el porcentaje de similitud.
        """
        input_content = self._read_file(input_file_path)
        input_embedding = self._get_embedding(input_content)
        
        files_and_content = self._read_files_in_dir(self.documents_dir)
        similarities = {}
        
        for file_name, content in files_and_content.items():
            doc_embedding = self._get_embedding(content)
            similarity = self._calculate_similarity(input_embedding, doc_embedding)
            similarities[file_name] = similarity
        
        # Identificar el archivo con mayor similitud
        most_similar_file = max(similarities, key=similarities.get)
        highest_similarity = similarities[most_similar_file]
        
        result = {
            "most_similar_file": most_similar_file,
            "similarity_percentage": highest_similarity * 100,
            "is_plagiarism": highest_similarity >= self.percentaje_simil
        }
        
        return result

    def _preprocess_text(self, text: str) -> str:
        """
        Preprocesa el texto eliminando puntuación, stopwords y aplicando lematización.
        
        Parámetros:
        -----------
        text : str
            Texto a preprocesar.
        
        Retorna:
        --------
        str
            Texto preprocesado.
        """
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = word_tokenize(text)
        words = [word for word in words if word not in self.stop_words]
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return " ".join(words)
    
    def _read_files_in_dir(self, documents_dir: str) -> dict:
        """
        Lee y preprocesa todos los archivos en un directorio dado.
        
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
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, max_length=512, truncation=True)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)  # Mean pooling

    def _calculate_similarity(self, embedding1: torch.Tensor, embedding2: torch.Tensor) -> float:
        """
        Calcula la similitud coseno entre dos incrustaciones.
        
        Parámetros:
        -----------
        embedding1 : torch.Tensor
            Primer tensor de incrustación.
        embedding2 : torch.Tensor
            Segundo tensor de incrustación.
        
        Retorna:
        --------
        float
            Similitud coseno entre las dos incrustaciones.
        """
        cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
        similarity = cos(embedding1, embedding2)
        return similarity.item()
