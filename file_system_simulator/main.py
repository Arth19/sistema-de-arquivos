from core.file_system import FileSystem

def print_commands():
    commands = """
    Comandos Disponíveis:
    - create_file [dir] [name] [size]: Cria um arquivo
    - delete_file [dir] [name]: Exclui um arquivo
    - list_files [dir]: Lista arquivos em um diretório
    - create_dir [name]: Cria um diretório
    - delete_dir [name]: Exclui um diretório
    - list_dirs: Lista todos os diretórios
    - exit: Sai do programa
    """
    print(commands)

def main():
    fs = FileSystem(100, 1024)  # Inicializar o sistema de arquivos
    print("Bem-vindo ao Simulador de Sistema de Arquivos!")
    print_commands()

    while True:
        command = input("Digite um comando: ").strip().split()
        if not command:
            continue

        if command[0] == "create_file" and len(command) == 4:
            dir_name, file_name, size = command[1], command[2], int(command[3])
            print(fs.create_file(dir_name, file_name, size))

        elif command[0] == "delete_file" and len(command) == 3:
            dir_name, file_name = command[1], command[2]
            print(fs.delete_file(dir_name, file_name))

        elif command[0] == "list_files" and len(command) == 2:
            dir_name = command[1]
            print("Files:", fs.list_files(dir_name))

        elif command[0] == "create_dir" and len(command) == 2:
            dir_name = command[1]
            print(fs.create_directory(dir_name))

        elif command[0] == "delete_dir" and len(command) == 2:
            dir_name = command[1]
            print(fs.delete_directory(dir_name))

        elif command[0] == "list_dirs":
            print("Directories:", fs.list_directories())

        elif command[0] == "exit":
            print("Saindo do simulador...")
            break

        else:
            print("Comando inválido.")
            print_commands()

if __name__ == "__main__":
    main()
