from .file import File
from .directory import Directory
from .block import Block

class FileSystem:
    def __init__(self, total_blocks, block_size):
        self.block_size = block_size
        self.blocks_pool = [Block(block_size, i) for i in range(total_blocks)]
        self.root_directory = Directory("root")
        self.directories = {"root": self.root_directory}

    def create_file(self, directory_name, file_name, size):
        directory = self.get_directory(directory_name)
        if directory and not any(f.name == file_name for f in directory.files):
            file = File(file_name, size, self.block_size, self.blocks_pool)
            directory.add_file(file)
            return f"File '{file_name}' created in '{directory_name}' directory. {self.check_fragmentation()}"
        else:
            return "File already exists or directory not found."

    def delete_file(self, directory_name, file_name):
        directory = self.get_directory(directory_name)
        if directory:
            file_to_delete = next((f for f in directory.files if f.name == file_name), None)
            if file_to_delete:
                for block in file_to_delete.blocks:
                    self.blocks_pool.append(block)
                directory.remove_file(file_name)
                return f"File '{file_name}' deleted from '{directory_name}' directory. {self.check_fragmentation()}"
            else:
                return "File not found."
        else:
            return "Directory not found."

    def list_files(self, directory_name):
        directory = self.get_directory(directory_name)
        if directory:
            return '\n'.join(str(file) for file in directory.files)
        else:
            return "Directory not found."

    def get_directory(self, directory_name):
        return self.directories.get(directory_name, None)

    def check_fragmentation(self):
        fragmented = any(b.next_block is not None and b.next_block.block_id != b.block_id + 1 for b in self.blocks_pool)
        return "Fragmentation detected." if fragmented else "No fragmentation."

    def create_directory(self, directory_name):
        if directory_name not in self.directories:
            self.directories[directory_name] = Directory(directory_name)
            return f"Directory '{directory_name}' created."
        else:
            return "Directory already exists."

    def delete_directory(self, directory_name):
        if directory_name in self.directories and directory_name != "root":
            directory = self.directories.pop(directory_name)
            # Liberar blocos de todos os arquivos no diretório
            for file in directory.files:
                for block in file.blocks:
                    self.blocks_pool.append(block)
            return f"Directory '{directory_name}' deleted."
        else:
            return "Cannot delete root directory or directory not found."

    def list_directories(self):
        return list(self.directories.keys())