import program_files


class Language:

    def __init__(self):
        self.ru_words = ['Введите путь до папки с папками записей(n - для выхода):', 'До свидания!',
                         'Введите <Enter> для закрытия программы:', 'Неверный ввод!', 'Список записей:',
                         'Общее число записей:',
                         'Список записей для конвертации сформирован. Продолжить?(n - нет):',
                         'Подождите, идёт конвертация', 'Осталось записей:', 'Запись:', 'ПОВРЕЖДЕНА!!!',
                         'ВОЗМОЖНЫ ПРОБЛЕМЫ С ИЗОБРАЖЕНИЕМ ИЛИ(И) ЗВУКОМ ПОСЛЕ КОНВЕРТАЦИИ!',
                         'Конвертация завершена!', 'Затрачено времени:', 'ч.', 'мин.', 'сек.']
        self.en_words = []

    def set_language(self) -> list[str]:
        with open(program_files.set_log, 'r') as set_log:
            lang = set_log.read()
        set_log.close()

        match lang:
            case 'ru':
                return self.ru_words
            case 'en':
                return self.en_words
