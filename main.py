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
        
        # Verifica la existencia del segundo archivo
        while True:
            file2 = "documents/" + input("Por favor ingrese el nombre del segundo archivo (nombre.txt): ")
            if os.path.isfile(file2):
                break
            else:
                print(f"El archivo {file2} no se encuentra. Por favor, ingrese otro nombre de archivo.")
        
        processor = TextProcessor(file1, file2)
        processor.process()
        compare = input("Desea comparar otro par de archivos? (s/n): ").lower() == "s"
    
if __name__ == "__main__":
    main()