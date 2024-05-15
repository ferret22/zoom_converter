import os
import tkinter as tk
from colorama import *
import conversion_starter
from file_writer import FileWriter
from language import Language


init(autoreset=True)
writer = FileWriter()
writer.check_ers()
lang = Language()


def get_screen_rect() -> tuple[int, int]:
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()

    return width, height


def settings(words: list[str]) -> list[str]:
    while True:
        ans = input(f'{words[17]}' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)
        try:
            if ans == 'n':
                return lang.set_language()

            match int(ans):
                case 1:
                    writer.write_lang('ru')
                case 2:
                    writer.write_lang('en')
        except ValueError:
            print(Fore.RED + f'{words[3]}' + Style.RESET_ALL)
            continue

        return lang.set_language()


def program_cycle(words: list[str]) -> None:
    width, height = get_screen_rect()
    os.system(f'mode con: cols={int(width // 4.55)} lines={int(height // 9.6)}')

    while True:
        ans = input(f'{words[0]}' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)
        if ans == 'n':
            print(f'{words[1]}')
            input(f'{words[2]} ')
            break
        elif ans == 's':
            words = settings(words)
        elif os.path.exists(ans):
            paths = os.listdir(ans)
            conversion_starter.start_dot_zoom(ans, paths, words)
        else:
            print(Fore.RED + f'{words[3]}' + Style.RESET_ALL)
            continue


if __name__ == '__main__':
    program_cycle(lang.set_language())
