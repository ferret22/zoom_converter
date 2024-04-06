import os
import tkinter as tk
from colorama import *
import conversion_starter


init(autoreset=True)


def get_screen_rect() -> tuple[int, int]:
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()

    return width, height


def program_cycle() -> None:
    width, height = get_screen_rect()
    os.system(f'mode con: cols={int(width // 4.55)} lines={int(height // 9.6)}')

    while True:
        ans = input('Введите путь до папки с папками записей(n - для выхода):' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)
        if ans == 'n':
            print('До свидания!')
            input('Введите <Enter> для закрытия программы: ')
            break

        if os.path.exists(ans):
            paths = os.listdir(ans)
            conversion_starter.start_dot_zoom(ans, paths)
        else:
            print(Fore.RED + 'Неверный ввод!' + Style.RESET_ALL)
            continue


if __name__ == '__main__':
    program_cycle()
