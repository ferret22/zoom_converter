import os
import program_files


class FileWriter:

    def check_ers(self) -> None:
        if (not os.path.exists(program_files.ers_log)) or (not os.path.exists(program_files.set_log)):
            try:
                os.mkdir('log')
            except FileExistsError:
                pass

            self.create_file(program_files.ers_log)
            self.create_file(program_files.set_log)
            self.set_default()

    @staticmethod
    def create_file(file_name) -> None:
        with open(file_name, 'w') as file:
            file.write('')
        file.close()

    @staticmethod
    def read_file(file_name) -> list[str]:
        with open(file_name, 'r') as file:
            paths = file.readlines()
        file.close()
        return paths

    @staticmethod
    def set_default() -> None:
        lang = 'ru'
        with open(program_files.set_log, 'w') as set_log:
            set_log.write(lang)
        set_log.close()

    @staticmethod
    def write_lang(lang: str) -> None:
        with open(program_files.set_log, 'w') as set_log:
            set_log.write(lang)
        set_log.close()

    def write_error_path(self, error_path: str) -> bool:
        paths = self.read_file(program_files.ers_log)

        if error_path + '\n' not in paths:
            with open(program_files.ers_log, 'a') as ers_file:
                ers_file.write(error_path + '\n')
            ers_file.close()

            return True
        return False

    def check_error_path(self, path: str) -> bool:
        paths = self.read_file(program_files.ers_log)

        if path + '\n' in paths:
            return False
        return True
