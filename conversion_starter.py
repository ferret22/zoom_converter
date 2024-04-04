import os
import subprocess
import time
from colorama import *


def check_paths(main_path: str, paths: list[str]):
    true_paths = []
    for path in paths:
        if os.path.isdir(main_path + '\\' + path):
            true_paths.append(main_path + '\\' + path)

    print(Fore.MAGENTA + 'Список записей:' + Style.RESET_ALL)
    for path in true_paths:
        time.sleep(1.2)
        print('\t' + Fore.GREEN + path + Style.RESET_ALL)

    return true_paths


def search_dot_zoom(main_path: str, paths: list[str]):
    true_paths = check_paths(main_path, paths)
    dot_zoom_files = []

    for path in true_paths:
        files = os.listdir(path)
        for file in files:
            if file == 'double_click_to_convert_01.zoom':
                dot_zoom_files.append(path + '\\double_click_to_convert_01.zoom')

    return dot_zoom_files


def process_exists(process_name: str):
    programs = str(subprocess.check_output('tasklist'))
    if process_name in programs:
        return True
    else:
        return False


def start_dot_zoom(main_path: str, paths: list[str]):
    t0 = time.process_time()
    process_name = 'zTscoder.exe'
    dot_zoom_files = search_dot_zoom(main_path, paths)
    os.startfile(dot_zoom_files.pop())

    print()
    print(Fore.BLUE + 'Подождите, идёт конвертация' + Style.RESET_ALL)

    while True:
        if process_exists(process_name):
            continue
        else:
            if len(dot_zoom_files) > 0:
                os.startfile(dot_zoom_files.pop())
            else:
                print(Fore.GREEN + 'Конвертация завершена!' + Style.RESET_ALL)
                break

    t1 = time.process_time()
    print(Fore.BLUE + f'Затрачено времени: {t1 - t0} сек.' + Style.RESET_ALL)
