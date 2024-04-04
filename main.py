import os
from colorama import *
import conversion_starter


init(autoreset=True)


def program_cycle():
    while True:
        ans = input('Введите путь до папки с папками записей(n - для выхода):' + Fore.GREEN + ' ')
        print(Style.RESET_ALL)
        if ans == 'n':
            print('До свидания!')
            input()
            break

        if os.path.exists(ans):
            paths = os.listdir(ans)
            conversion_starter.start_dot_zoom(ans, paths)
        else:
            print(Fore.RED + 'Неверный ввод!' + Style.RESET_ALL)
            continue


if __name__ == '__main__':
    program_cycle()
