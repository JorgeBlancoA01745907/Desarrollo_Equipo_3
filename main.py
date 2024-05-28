"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""
from Model import TextProcessor
import logging
import os

def main():
    print("Welcome to the program that detects plagiarism")
    compare = True
    while compare:
        # Verifica la existencia del primer archivo
        while True:
            file1 = "documents/" + input("Please, input the name of the first file (name.txt): ")
            if os.path.isfile(file1):
                break
            else:
                print(f"The file {file1} isn't showing. Please, input another file's name.")

        # Lista de archivos en la carpeta 'documents' (excepto el file1)
        files_to_compare = [f for f in os.listdir("documents/") if os.path.isfile(os.path.join("documents/", f)) and f != os.path.basename(file1)]
        
        if not files_to_compare:
            print("There are not more files in the folder 'documents' to compare.")
        else:
            for file2 in files_to_compare:
                file2_path = os.path.join("documents/", file2)
                #print(f"Comparando {file1} con {file2_path}")
                processor = TextProcessor(file1, file2_path)
                processor.process()
        
        compare = input("Would you like to compare other file? (y/n): ").lower() == "y"
    
if __name__ == "__main__":
    main()