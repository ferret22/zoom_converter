import os
import program_files


class ErrorWriter:

    @staticmethod
    def check_ers() -> None:
        if not os.path.exists(program_files.ers_log):
            try:
                os.mkdir('log')
            except FileExistsError:
                pass

            with open(program_files.ers_log, 'w') as ers_file:
                ers_file.write('')
            ers_file.close()

    @staticmethod
    def write_error_path(error_path: str) -> bool:
        with open(program_files.ers_log, 'r') as ers_file:
            paths = ers_file.readlines()
        ers_file.close()

        if error_path + '\n' not in paths:
            with open(program_files.ers_log, 'a') as ers_file:
                ers_file.write(error_path + '\n')
            ers_file.close()

            return True
        return False

    @staticmethod
    def check_error_path(path: str) -> bool:
        with open(program_files.ers_log, 'r') as ers_file:
            paths = ers_file.readlines()
        ers_file.close()

        if path + '\n' in paths:
            return False

        return True
