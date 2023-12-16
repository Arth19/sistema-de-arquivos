class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def remove_file(self, file_name):
        self.files = [f for f in self.files if f.name != file_name]

    def list_files(self):
        return [f.name for f in self.files]
