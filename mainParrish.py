from IAModel import similarityCalculation

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detectar plagio en un archivo de texto.")
    parser.add_argument("input_file", help="Ruta del archivo de texto sospechoso.")
    parser.add_argument("documents_dir", help="Ruta de la carpeta con documentos originales.")
    parser.add_argument("percentaje_simil", type=float, help="Umbral de similitud para determinar el plagio.")
    
    args = parser.parse_args()
    
    detector = similarityCalculation(args.documents_dir, args.percentaje_simil)
    result = detector.plagiarismDetection(args.input_file)
    
    print(f"Archivo más similar: {result['most_similar_file']}")
    print(f"Porcentaje de similitud: {result['similarity_percentage']:.2f}%")
    print(f"Es plagio: {'Sí' if result['is_plagiarism'] else 'No'}")
