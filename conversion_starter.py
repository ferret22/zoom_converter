import os
from colorama import *


def check_paths(main_path: str, paths: list[str]):
    true_paths = []
    for path in paths:
        if os.path.isdir(main_path + '\\' + path):
            true_paths.append(path)

    for path in true_paths:
        print(Fore.GREEN + path + Style.RESET_ALL)

    return true_paths
