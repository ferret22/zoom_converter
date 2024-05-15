import os
import subprocess
import time
from colorama import *
import program_files
from file_writer import FileWriter


writer = FileWriter()


def check_paths(main_path: str, paths: list[str]) -> list[str]:
    true_paths = []
    for path in paths:
        if os.path.isdir(main_path + '\\' + path):
            true_paths.append(main_path + '\\' + path)

    return true_paths


def search_dot_zoom(main_path: str, paths: list[str], words: list[str]) -> tuple[list[str], list[str]]:
    true_paths = check_paths(main_path, paths)
    dot_zoom_files = []
    zoom_paths = []

    for path in true_paths:
        files = os.listdir(path)
        for file in files:
            if file == program_files.dot_zoom_file:
                zoom_paths.append(path)
                if writer.check_error_path(path + '\\' + program_files.dot_zoom_file):
                    dot_zoom_files.append(path + '\\' + program_files.dot_zoom_file)

    print(Fore.MAGENTA + f'{words[4]}' + Style.RESET_ALL)
    for path in dot_zoom_files:
        time.sleep(0.2)
        print('\t' + Fore.GREEN + path + Style.RESET_ALL)
    print(f'{words[5]} {len(dot_zoom_files)}')

    return dot_zoom_files, zoom_paths


def check_error_files(zoom_paths: list[str]) -> list[str]:
    error_paths = []

    for path in zoom_paths:
        files = os.listdir(path)
        if program_files.error_log_file in files:
            if writer.write_error_path(path + '\\' + program_files.dot_zoom_file):
                error_paths.append(path + '\\' + program_files.dot_zoom_file)

    return error_paths


def process_exists() -> bool:
    programs = str(subprocess.check_output('tasklist'))
    if program_files.process_name in programs:
        return True
    return False


def calc_time(t0: float, t1: float) -> tuple[int, int, int]:
    t = t1 - t0

    hours = 0
    minutes = 0
    seconds = round(t)

    if int(t) >= 60:
        minutes_int = int(t // 60)
        minutes_fl = t / 60
        seconds = round((minutes_fl - minutes_int) * 60)

        minutes = minutes_int

        if minutes_int >= 60:
            hours_int = int(minutes_fl // 60)
            hours_fl = minutes_fl / 60
            minutes = round((hours_fl - hours_int) * 60)

            hours = hours_int

    return hours, minutes, seconds


def start_dot_zoom(main_path: str, paths: list[str], words: list[str]) -> None:
    t0 = float(time.time())
    dot_zoom_files, zoom_paths = search_dot_zoom(main_path, paths, words)
    error_zoom_files = check_error_files(zoom_paths)

    print()
    ans = input(f'{words[6]}' + Fore.GREEN + ' ')
    print(Style.RESET_ALL)

    if ans != 'n':
        print(Fore.BLUE + f'{words[7]}' + Style.RESET_ALL)

        while True:
            if process_exists():
                continue
            else:
                if len(dot_zoom_files) > 0:
                    print(Fore.GREEN + f'\t{words[8]} {len(dot_zoom_files)}' + Style.RESET_ALL)
                    zoom_file = dot_zoom_files.pop()

                    if zoom_file in error_zoom_files:
                        print(Fore.RED + f'\n{words[9]}\n{zoom_file}\n{words[10]}\n{words[11]}\n' + Style.RESET_ALL)

                    os.startfile(zoom_file)
                else:
                    print(Fore.GREEN + f'{words[12]}' + Style.RESET_ALL + '\n')
                    break

    t1 = float(time.time())
    times = calc_time(t0, t1)
    print(Fore.BLUE + f'{words[13]} {times[0]} {words[14]} {times[1]} {words[15]} {times[2]} {words[16]}'
          + Style.RESET_ALL + '\n')
