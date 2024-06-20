import subprocess

def create_group(group=None):
    if group:
        subprocess.run(["sudo", "groupadd", group], check=True)
        print(f"Group '{group}' created successfully.")
    else:
        group = input(f"Input New Group: ").strip()
        try:
            subprocess.run(["sudo", "groupadd", group], check=True)
            print(f"Group '{group}' created successfully.")
            return group
        except subprocess.CalledProcessError as e:
            print(f"Failed to create group '{group}': {e} ")
        
        
if __name__ == '__main__':
    create_group()