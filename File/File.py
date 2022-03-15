from File.file_helpers import *
class File:
    def __init__(self, path):
        self.path = path
        self.lines =""

    def read_file(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
        lines = format_lines(lines)
        self.lines = delete_emty_items_from_lines(lines)
        return lines