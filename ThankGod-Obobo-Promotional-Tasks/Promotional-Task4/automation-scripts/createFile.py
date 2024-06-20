import csv
import os

company_directories = [
"/finance-budgets",
"/contract-documents",
"/business-projections",
"/business-models",
"/employee-data",
"/company-vision-and-mission-statement",
"/server-configuration-script",
]

def read_csv_and_create_file(file_name=None, directory=None):
    if directory in company_directories:
        with open(f"{directory}/{file_name}", "x") as file:
            file.write("")
        exists = os.path.exists(f"{directory}/{file_name}")
        if exists:
            print(f"file {file_name} successfully created at {directory}")
        else:
            print(f"unable to create file {file_name} at {directory}")
    else:
        print(f"unable to create file {file_name} at {directory}, use a company directory.")

def create_file(file_path=None):
    if file_path:
        with open(file_path, "r") as file:
            csv_file = csv.reader(file)
            
            for row in csv_file:
                read_csv_and_create_file(row[0], row[1])
                
    is_file = input(f"Do you want to create files from a csv file?, yes/no: ").strip().lower()
    if is_file == "yes":
        file_path = input(f"provide the files csv file path, please use absolute paths: ").strip()
        with open(file_path, "r") as file:
            csv_file = csv.reader(file)
            
            for row in csv_file:
                read_csv_and_create_file(row[0], row[1])
    elif is_file == "no":    
        file_name = input(f"Please provide a file name: ").strip()
        directory = input(f"Please provide a directory, use absolute paths: ").strip()
        read_csv_and_create_file(file_name, directory)
    else:
        print("Do you really want to create this file?, please be certain how you want to go about it.")
                
if __name__ == "__main__":
    create_file()