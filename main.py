"""
Authors: Erika García,
Christian Parrish,
Jorge Blanco
"""
from Model import TextProcessor
from tabulate import tabulate
import logging
import os
from itertools import combinations
from operator import itemgetter

def compare_two_files():
    """
    This function compares two files that the user inputs, must be .txt files
    """
    while True:
        file1 = "documents/" + input("Please, input the name of the first file (name.txt): ")
        if os.path.isfile(file1):
            break
        else:
            print(f"The file {file1} isn't found. Please, input another file's name.\n")
    
    while True:
        file2 = "documents/" + input("Please, input the name of the second file (name.txt): ")
        if os.path.isfile(file2):
            break
        else:
            print(f"The file {file2} isn't found. Please, input another file's name.")
    
    processor = TextProcessor(file1, file2)
    result = processor.process()
    if result:
        print("\nResults:")
        print(tabulate([result], headers="keys", tablefmt="pretty"))

def compare_file_with_folder():
    """
    This function compares a file that the user inputs with all the files in the folder 'documents'
    """
    while True:
        file1 = "documents/" + input("Please, input the name of the file to compare (name.txt): ")
        if os.path.isfile(file1):
            break
        else:
            print(f"The file {file1} isn't found. Please, input another file's name.")
    
    files_to_compare = [f for f in os.listdir("documents/") if os.path.isfile(os.path.join("documents/", f)) and f != os.path.basename(file1)]
    
    if not files_to_compare:
        print("There are no other files in the folder 'documents' to compare.")
    else:
        results = []
        for file2 in files_to_compare:
            file2_path = os.path.join("documents/", file2)
            processor = TextProcessor(file1, file2_path)
            result = processor.process()
            if result:
                results.append(result)
        if results:
            # Sort results by the "Comparing with" field in ascending order
            results = sorted(results, key=lambda x: x["Percentage of similarity"], reverse=True)
            
            print("\nResults:")
            #print the first two results

            print(tabulate(results[0:2], headers="keys", tablefmt="pretty"))

def compare_all_files_in_folder():
    """
    This function compares all the files in the folder 'documents' between them
    """
    files = (entry.name for entry in os.scandir("documents/") if entry.is_file())
    files = list(files)  # Convert generator to list to get length

    if len(files) < 2:
        print("There are not enough files in the folder 'documents' to compare.")
    else:
        results = [
            TextProcessor(os.path.join("documents/", file1), os.path.join("documents/", file2)).process()
            for file1, file2 in combinations(files, 2)
        ]
        results = [result for result in results if result]  # Filter out None results

        if results:
            # Sort results by the "Comparing with" field in ascending order
            results.sort(key=itemgetter("Comparing with"))

            print("\nResults:")
            print(tabulate(results[0:2], headers="keys", tablefmt="pretty"))

def main():
    print("\nWelcome to the program that detects plagiarism")
    
    while True:
        print("\nMenu:")
        print("1. Compare two files")
        print("2. Compare a file with all files in the folder 'documents'")
        print("3. Compare all files in the folder 'documents' between them")
        print("4. Exit\n")
        
        choice = input("Please, choose an option (1-4): ")
        
        if choice == '1':
            compare_two_files()
        elif choice == '2':
            compare_file_with_folder()
        elif choice == '3':
            compare_all_files_in_folder()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please, try again.")

if __name__ == "__main__":
    main()
