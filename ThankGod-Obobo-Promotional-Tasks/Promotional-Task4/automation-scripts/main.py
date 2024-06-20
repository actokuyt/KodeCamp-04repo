from createFile import create_file
from createDir import create_dir
from createUsers import create_user

def main():
    """
    Main function to execute user, directory, and file creation functions.
    """
    create_user()  # Calls the function to create users
    create_dir()   # Calls the function to create directories
    create_file()  # Calls the function to create files

if __name__ == "__main__":
    """
    Ensures that the main function is called only when the script is run directly,
    not when it is imported as a module.
    """
    main()
