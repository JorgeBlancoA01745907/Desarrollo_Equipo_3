from Model import TextProcessor
import logging
import os

def main():
    print("Bienvenido al programa de detección de plagio")
    compare = True
    while compare:
        # Verifica la existencia del primer archivo
        while True:
            file1 = "documents/" + input("Por favor ingrese el nombre del primer archivo (nombre.txt): ")
            if os.path.isfile(file1):
                break
            else:
                print(f"El archivo {file1} no se encuentra. Por favor, ingrese otro nombre de archivo.")

        # Lista de archivos en la carpeta 'documents' (excepto el file1)
        files_to_compare = [f for f in os.listdir("documents/") if os.path.isfile(os.path.join("documents/", f)) and f != os.path.basename(file1)]
        
        if not files_to_compare:
            print("No hay otros archivos en la carpeta 'documents' para comparar.")
        else:
            for file2 in files_to_compare:
                file2_path = os.path.join("documents/", file2)
                #print(f"Comparando {file1} con {file2_path}")
                processor = TextProcessor(file1, file2_path)
                processor.process()
        
        compare = input("Desea comparar otro archivo? (s/n): ").lower() == "s"
    
if __name__ == "__main__":
    main()