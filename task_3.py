import sys
from pathlib import Path
from colorama import Fore, Style, init as colorama_init

""" 
startup script: python task_3.py src/picture 
"""


def folder_and_file_structure_output(path, gap=0):
    """
    The function takes the path to a folder
    and displays all its contents in expanded form.
    """
    print(Fore.BLUE + " " * gap + path.name + "/")
    gap += 4
    try:
        for item in path.iterdir():
            if item.is_file():
                print(Fore.GREEN + " " * gap + item.name)
            elif item.is_dir():
                folder_and_file_structure_output(item, gap)
    except PermissionError:
        print(Fore.RED + " " * gap + "[нет доступа]")
        return


def main():
    colorama_init(autoreset=True)
    if len(sys.argv) <= 1:
        print(Fore.RED + "You haven't specified a directory.")
        return 1
    p = Path(sys.argv[1])
    if not p.exists():
        print(Fore.RED + "The specified directory does not exist.")
        return 1
    if not p.is_dir():
        print(Fore.RED + "You specified the path to the file, not the directory.")
        return 1
    folder_and_file_structure_output(p)
    return 0


if __name__ == "__main__":
    main()
