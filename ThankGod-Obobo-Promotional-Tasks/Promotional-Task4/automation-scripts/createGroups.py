import subprocess

def create_group(group=None):
    """
    Creates a new group using the 'groupadd' command. If a group name is provided, it uses that.
    Otherwise, it prompts the user for a group name.

    :param group: Optional; Name of the group to create. If not provided, the user will be prompted for a group name.
    """
    if group:
        # If a group name is provided, create the group
        subprocess.run(["sudo", "groupadd", group], check=True)
        print(f"Group '{group}' created successfully.")
    else:
        # If no group name is provided, prompt the user for a group name
        group = input(f"Input New Group: ").strip()
        try:
            # Attempt to create the group with the provided name
            subprocess.run(["sudo", "groupadd", group], check=True)
            print(f"Group '{group}' created successfully.")
            return group
        except subprocess.CalledProcessError as e:
            # Handle errors if the group creation fails
            print(f"Failed to create group '{group}': {e}")

if __name__ == '__main__':
    create_group()
