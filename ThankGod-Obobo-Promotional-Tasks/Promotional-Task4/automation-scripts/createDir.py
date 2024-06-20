import os
import csv


def read_file_and_make_directories(file_path):
    """
    Reads a CSV file containing directory names and creates those directories.

    :param file_path: Path to the CSV file containing directory names.
    """
    with open(file_path, mode="r") as file:
        csv_file = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_file:
            # Create a directory with the name specified in the first column of each row
            os.makedirs(f"/{row[0]}")
            print(f"successfully created directory {row[0]}")


def create_dir(file_path=None):
    """
    Main function to create directories. It can either read directory names from a CSV file or take a single directory name input from the user.

    :param file_path: Optional; Path to the CSV file. If provided, directories will be created based on the file.
    """
    if file_path:
        # If a file path is provided, create directories based on the file
        read_file_and_make_directories(file_path)
        return

    # Ask the user if they want to create directories from a file
    is_file = input(f"Do you want to create directories from a file? yes/no ").strip().lower()
    if is_file == "yes":
        # If yes, ask for the file path
        file_path = input(f"Provide directories csv file, please use absolute paths: ").strip()
        read_file_and_make_directories(file_path)
    elif is_file == "no":
        # If no, ask for a single directory name to create
        directory = input(f"Provide the directory to be created, please use absolute paths: ").strip()
        os.makedirs(directory)
        print(f"successfully created directory {directory}")
    else:
        # If the user input is invalid, print a message
        print("Invalid input. Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    create_dir()
