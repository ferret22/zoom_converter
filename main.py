import os


def program_cycle():
    while True:
        ans = input('Введите путь до папки с папками записей(n - для выхода): ')
        if ans == 'n':
            print('До свидания!')
            break

        if os.path.exists(ans):
            paths = os.listdir(ans)
            print()
            print(*paths, sep='\n')
            print()
        else:
            print('Неверный ввод!')
            continue


if __name__ == '__main__':
    program_cycle()
