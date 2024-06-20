import csv
import os

# List of allowed company directories
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
    """
    Creates a file in the specified directory if the directory is in the list of allowed company directories.

    :param file_name: Name of the file to create.
    :param directory: Directory in which to create the file.
    """
    if directory in company_directories:
        # Create the file in the specified directory
        with open(f"{directory}/{file_name}", "x") as file:
            file.write("")  # Write an empty string to create the file
        exists = os.path.exists(f"{directory}/{file_name}")  # Check if the file exists
        if exists:
            print(f"file {file_name} successfully created at {directory}")
        else:
            print(f"unable to create file {file_name} at {directory}")
    else:
        # Print error if directory is not in the allowed list
        print(f"unable to create file {file_name} at {directory}, use a company directory.")

def create_file(file_path=None):
    """
    Main function to create files. It can either read file names and directories from a CSV file or take a single file name and directory input from the user.

    :param file_path: Optional; Path to the CSV file. If provided, files will be created based on the file.
    """
    if file_path:
        # If a file path is provided, create files based on the file
        with open(file_path, "r") as file:
            csv_file = csv.reader(file)
            
            for row in csv_file:
                read_csv_and_create_file(row[0], row[1])
                
    # Ask the user if they want to create files from a CSV file
    is_file = input(f"Do you want to create files from a csv file?, yes/no: ").strip().lower()
    if is_file == "yes":
        # If yes, ask for the file path
        file_path = input(f"provide the files csv file path, please use absolute paths: ").strip()
        with open(file_path, "r") as file:
            csv_file = csv.reader(file)
            
            for row in csv_file:
                read_csv_and_create_file(row[0], row[1])
    elif is_file == "no":
        # If no, ask for a single file name and directory to create
        file_name = input(f"Please provide a file name: ").strip()
        directory = input(f"Please provide a directory, use absolute paths: ").strip()
        read_csv_and_create_file(file_name, directory)
    else:
        # If the user input is invalid, print a message
        print("Invalid input. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    create_file()
