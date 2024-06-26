from NewModel import similarityCalculation

# Definir el umbral de que es plagio o no
TXT_FILES_PATH = 'originals/'
UMBRAL = 0.988

if __name__ == '__main__':
    file_to_analyse = 'input_file.txt'
    
    plagiarism = similarityCalculation(TXT_FILES_PATH, UMBRAL, metric='cosine')
    
    #result = plagiarism.plagiarismDetection(file_to_analyse)
    #Evaluar todos los archivos en el directorio 'Evaluation'
    results = plagiarism.evaluate_directory('suspicious/')
    print(results)