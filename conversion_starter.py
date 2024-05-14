import os
import subprocess
import time
from colorama import *


dot_zoom_file = 'double_click_to_convert_01.zoom'
error_log_file = 'xcode_error.log'
process_name = 'zTscoder.exe'


def check_paths(main_path: str, paths: list[str]) -> list[str]:
    true_paths = []
    for path in paths:
        if os.path.isdir(main_path + '\\' + path):
            true_paths.append(main_path + '\\' + path)

    return true_paths


def search_dot_zoom(main_path: str, paths: list[str]) -> (list[str], list[str]):
    true_paths = check_paths(main_path, paths)
    dot_zoom_files = []
    zoom_paths = []

    for path in true_paths:
        files = os.listdir(path)
        for file in files:
            if file == dot_zoom_file:
                dot_zoom_files.append(path + '\\' + dot_zoom_file)
                zoom_paths.append(path)

    print(Fore.MAGENTA + 'Список записей:' + Style.RESET_ALL)
    for path in dot_zoom_files:
        time.sleep(0.2)
        print('\t' + Fore.GREEN + path + Style.RESET_ALL)
    print(f'Общее число записей: {len(dot_zoom_files)}')

    return dot_zoom_files, zoom_paths


def check_error_files(zoom_paths: list[str]) -> list[str]:
    error_paths = []

    for path in zoom_paths:
        files = os.listdir(path)
        if error_log_file in files:
            error_paths.append(path + '\\' + dot_zoom_file)

    return error_paths


def process_exists() -> bool:
    programs = str(subprocess.check_output('tasklist'))
    if process_name in programs:
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


def start_dot_zoom(main_path: str, paths: list[str]) -> None:
    t0 = float(time.time())
    dot_zoom_files, zoom_paths = search_dot_zoom(main_path, paths)
    error_zoom_files = check_error_files(zoom_paths)

    print()
    ans = input('Список записей для конвертации сформирован. Продолжить?(n - нет):' + Fore.GREEN + ' ')
    print(Style.RESET_ALL)

    if ans != 'n':
        print(Fore.BLUE + 'Подождите, идёт конвертация' + Style.RESET_ALL)

        while True:
            if process_exists():
                continue
            else:
                if len(dot_zoom_files) > 0:
                    print(Fore.GREEN + f'\tОсталось записей: {len(dot_zoom_files)}' + Style.RESET_ALL)
                    zoom_file = dot_zoom_files.pop()

                    if zoom_file in error_zoom_files:
                        print(Fore.RED + f'\nЗапись:\n{zoom_file}\nПОВРЕЖДЕНА!!!\n'
                                         f'ВОЗМОЖНЫ ПРОБЛЕМЫ С ИЗОБРАЖЕНИЕМ ИЛИ(И) ЗВУКОМ ПОСЛЕ КОНВЕРТАЦИИ!\n'
                              + Style.RESET_ALL)

                    os.startfile(zoom_file)
                else:
                    print(Fore.GREEN + 'Конвертация завершена!' + Style.RESET_ALL + '\n')
                    break

    t1 = float(time.time())
    times = calc_time(t0, t1)
    print(Fore.BLUE + f'Затрачено времени: {times[0]} ч. {times[1]} мин. {times[2]} сек.' + Style.RESET_ALL + '\n')
