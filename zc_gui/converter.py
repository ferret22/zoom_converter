import os
import subprocess
import time


class ZoomConverter:

    def __init__(self, main_path: str, paths: list[str]):
        self.__main_path = main_path
        self.__paths = paths
        self.__process_name = 'zTscoder.exe'
        self.dot_zoom_files = []

    def __check_paths(self):
        true_paths = []
        for path in self.__paths:
            if os.path.isdir(self.__main_path + '\\' + path):
                true_paths.append(self.__main_path + '\\' + path)

        return true_paths

    def search_dot_zoom(self):
        true_paths = self.__check_paths()

        for path in true_paths:
            files = os.listdir(path)
            for file in files:
                if file == 'double_click_to_convert_01.zoom':
                    self.dot_zoom_files.append(path + '\\double_click_to_convert_01.zoom')

    def __process_exists(self):
        programs = str(subprocess.check_output('tasklist'))
        if self.__process_name in programs:
            return True
        return False

    def start_dot_zoom(self):
        t0 = time.time()

        while True:
            if self.__process_exists():
                continue
            else:
                if len(self.dot_zoom_files) > 0:
                    os.startfile(self.dot_zoom_files.pop())
                else:
                    break

        t1 = time.time()
        return t1 - t0
