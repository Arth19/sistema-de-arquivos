# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Sistema de Arquivos
# Aluno(s): Aildson Ferreira e Arthur Macedo


from core.sistema_arquivos import SistemaArquivos


def lista_comandos():
    comandos = """
    Comandos Disponíveis:
        > create_file <dir> <nome> <tamanho>    Cria um arquivo
        > remove_file <dir> <nome>              Exclui um arquivo
        > list_files  <dir> <senha>             Lista arquivos em um diretório
        > create_dir <nome> <senha>             Cria um diretório
        > remove_dir <nome>                     Exclui um diretório
        > list_dirs                             Lista todos os diretórios
        > exit                                  Sai do programa
    """
    print(comandos)


def main():
    fs = SistemaArquivos(100, 1024)  # Inicializar o sistema de arquivos
    print("### Sistema de Arquivos ###")
    lista_comandos()

    while True:
        comando = input("Digite um comando: ").strip().split()

        if not comando:
            continue

        if comando[0] == "create_file" and len(comando) == 4:
            nome_diretorio, nome_arquivo, tamanho = (
                comando[1],
                comando[2],
                int(comando[3]),
            )
            print(fs.cria_arquivo(nome_diretorio, nome_arquivo, tamanho))

        elif comando[0] == "remove_file" and len(comando) == 3:
            nome_diretorio, nome_arquivo = comando[1], comando[2]
            print(fs.remove_arquivo(nome_diretorio, nome_arquivo))

        elif comando[0] == "list_files" and len(comando) == 3:
            nome_diretorio = comando[1]
            senha_diretorio = comando[2]
            print("Arquivos:", fs.lista_arquivos(nome_diretorio, senha_diretorio))

        elif comando[0] == "create_dir" and len(comando) == 3:
            nome_diretorio = comando[1]
            senha_diretorio = comando[2]
            print(fs.cria_diretorio(nome_diretorio, senha_diretorio))

        elif comando[0] == "remove_dir" and len(comando) == 2:
            nome_diretorio = comando[1]
            print(fs.remove_diretorio(nome_diretorio))

        elif comando[0] == "list_dirs":
            print("Diretórios:", fs.lista_diretorios())

        elif comando[0] == "exit":
            print("Encerrando...")
            break

        else:
            print("Comando inválido.")
            lista_comandos()


if __name__ == "__main__":
    main()
