import program_files


class Language:

    def __init__(self):
        self.ru_words = ['Введите путь до папки с папками записей(n - для выхода, s - для смены языка):',
                         'До свидания!',
                         'Введите <Enter> для закрытия программы:', 'Неверный ввод!', 'Список записей:',
                         'Общее число записей:',
                         'Список записей для конвертации сформирован. Продолжить?(n - нет):',
                         'Подождите, идёт конвертация', 'Осталось записей:', 'Запись:', 'ПОВРЕЖДЕНА!!!',
                         'ВОЗМОЖНЫ ПРОБЛЕМЫ С ИЗОБРАЖЕНИЕМ ИЛИ(И) ЗВУКОМ ПОСЛЕ КОНВЕРТАЦИИ!',
                         'Конвертация завершена!', 'Затрачено времени:', 'ч.', 'мин.', 'сек.',
                         'Введите для смены языка(1 - RU, 2 - EN, n - Отмена):']
        self.en_words = ['Enter the path to the folder with the record folders(n - for exit, s - change language):',
                         'Goodbye!',
                         'Type <Enter> to close the program:', 'Incorrect input!', 'List of records:',
                         'Total number of records:',
                         'The list of records for conversion has been formed. Continue?(n - no):',
                         'Wait, the conversion has already started', 'Records left:', 'Record:', 'CORRUPTED!!!',
                         'THERE MAY BE PROBLEMS WITH THE VIDEO OR (AND) SOUND AFTER CONVERSION!',
                         'The conversion is complete!', 'Time spent:', 'h.', 'min.', 'sec.',
                         'Enter to change the language(1 - RU, 2 - EN, n - Cancel):']

    def set_language(self) -> list[str]:
        with open(program_files.set_log, 'r') as set_log:
            lang = set_log.read()
        set_log.close()

        match lang:
            case 'ru':
                return self.ru_words
            case 'en':
                return self.en_words
