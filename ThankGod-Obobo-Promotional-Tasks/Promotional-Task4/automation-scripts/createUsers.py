import subprocess
import csv
from createGroups import create_group


def read_file_and_create_users(file_path):
    with open(file_path, mode="r") as file:
        csv_file = csv.reader(file)

        for row in csv_file:
            user = row[0]
            group = row[1]
            try:
                create_group(group)
                subprocess.run(
                    ['sudo', 'useradd', '-g', group, user], check=True)
                print(f"User '{user}' created successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to create user '{user}': {e}")


def create_user(file_path=None):
    if file_path:
        read_file_and_create_users(file_path)

    is_file = input(
        f"Do you want to create users from a file?, yes/no: ").strip().lower()
    if is_file == "yes":
        file_path = input(
            f"provide the users csv file path, please use absolute paths: ").strip()
        read_file_and_create_users(file_path)
    elif is_file == "no":
        user = input(f"Input New User: ").strip()
        group = ''

        try:
            which_group = input(
                f"Do you want to add this user to a new or existing group; new/existing: ").strip().lower()

            if which_group == "new":
                group = create_group()
            elif which_group == "existing":
                group = input(f"Enter group name: ").strip()

            if group:
                subprocess.run(
                    ['sudo', 'useradd', '-g', group, user], check=True)
                print(f"User '{user}' created successfully.")
            else:
                print(f"Creating user '{user}' without a group...")
                subprocess.run(['sudo', 'useradd', user], check=True)
                print(f"User '{user}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create user '{user}': {e}")
    else:
        print("Do you really want to create this user?, please be certain how you want to go about it.")


if __name__ == '__main__':
    create_user()
