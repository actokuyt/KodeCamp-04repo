import subprocess
import csv
from createGroups import create_group

def read_file_and_create_users(file_path):
    """
    Reads a CSV file containing usernames and group names, then creates the users and groups accordingly.

    :param file_path: Path to the CSV file containing usernames and group names.
    """
    with open(file_path, mode="r") as file:
        csv_file = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_file:
            user = row[0]  # Get the username from the first column
            group = row[1]  # Get the group name from the second column
            try:
                create_group(group)  # Create the group if it doesn't exist
                # Create the user and assign them to the group
                subprocess.run(['sudo', 'useradd', '-g', group, user], check=True)
                print(f"User '{user}' created successfully.")
            except subprocess.CalledProcessError as e:
                # Handle errors if the user creation fails
                print(f"Failed to create user '{user}': {e}")

def create_user(file_path=None):
    """
    Main function to create users. It can either read usernames and group names from a CSV file or take a single username and group input from the user.

    :param file_path: Optional; Path to the CSV file. If provided, users will be created based on the file.
    """
    if file_path:
        # If a file path is provided, create users based on the file
        read_file_and_create_users(file_path)

    # Ask the user if they want to create users from a file
    is_file = input(f"Do you want to create users from a file?, yes/no: ").strip().lower()
    if is_file == "yes":
        # If yes, ask for the file path
        file_path = input(f"Provide the users csv file path, please use absolute paths: ").strip()
        read_file_and_create_users(file_path)
    elif is_file == "no":
        # If no, ask for a single username and group to create
        user = input(f"Input New User: ").strip()
        group = ''

        try:
            # Ask if the user should be added to a new or existing group
            which_group = input(f"Do you want to add this user to a new or existing group; new/existing: ").strip().lower()

            if which_group == "new":
                group = create_group()  # Create a new group and get its name
            elif which_group == "existing":
                group = input(f"Enter group name: ").strip()  # Get the existing group name from the user

            if group:
                # If a group is specified, create the user and assign them to the group
                subprocess.run(['sudo', 'useradd', '-g', group, user], check=True)
                print(f"User '{user}' created successfully.")
            else:
                # If no group is specified, create the user without a group
                print(f"Creating user '{user}' without a group...")
                subprocess.run(['sudo', 'useradd', user], check=True)
                print(f"User '{user}' created successfully.")
        except subprocess.CalledProcessError as e:
            # Handle errors if the user creation fails
            print(f"Failed to create user '{user}': {e}")
    else:
        # If the user input is invalid, print a message
        print("Invalid input. Please answer 'yes' or 'no'.")

if __name__ == '__main__':
    create_user()
