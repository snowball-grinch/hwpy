import glob
import re


class File:

    list_of_parents = []

    def __init__(self, file):
        self.file = file
        self.__text = ""
        self.file_name = re.search(r"[0-9]+", self.file).group()

    def __repr__(self):
        return f"File[{self.file_name}] -> {self.__text}"

    def text(self) -> str:
        if self.__text == "":
            with open(self.file, "r") as a_file:
                self.__text = a_file.readline()
                return self.__text

    @property
    def parent(self):
        if self.text() != "0":
            if self.__text == "":
                self.text()
            file_parent = f'./files/{self.__text}.txt'
            new_file = File(file_parent)
            return new_file
        return None

    @property
    def parents(self):
        new = self.parent
        while new is not None:
            self.list_of_parents.append(new)
            new = new.parent
        return self.list_of_parents


list_of_files = glob.glob('./files/*.txt')
list_of_files_obj = []
for files in list_of_files:
    list_of_files_obj.append(File(files))

if __name__ == '__main__':
    for file_obj in list_of_files_obj:
        if file_obj.text() == "0":
            print(file_obj)
