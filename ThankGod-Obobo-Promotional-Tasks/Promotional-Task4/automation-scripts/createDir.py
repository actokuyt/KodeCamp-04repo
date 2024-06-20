import os
import csv


def read_file_and_make_directories(file_path):
    with open(file_path, mode="r") as file:
        csv_file = csv.reader(file)

        for row in csv_file:
            os.makedirs(f"/{row[0]}")
            print(f"successfully created directory {row[0]}")


def create_dir(file_path=None):
    if file_path:
        read_file_and_make_directories(file_path)
        return

    is_file = input(
        f"Do you want to create directories from a file? yes/no ").strip().lower()
    if is_file == "yes":
        file_path = input(
            f"Provide directories csv file, please use absolute paths: ").strip()
        read_file_and_make_directories(file_path)
    elif is_file == "no":
        directory = input(
            f"provide the directory to be create, please use absolute paths: ").strip()
        os.makedirs(directory)
        print(f"successfully created directory {directory}")
    else:
        print("Do you really want to create this file?, please be certain how you want to go about it.")


if __name__ == "__main__":
    create_dir()
