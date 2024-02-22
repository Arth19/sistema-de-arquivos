# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Sistema de Arquivos
# Aluno(s): Aildson Ferreira e Arthur Macedo

from .arquivo import Arquivo


class Diretorio:
    # Os diretórios possuem nome e lista de arquivos
    # É possível adicionar, remover e listar os arquivos de cada diretório
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha
        self.arquivos: list[Arquivo] = []

    def adiciona_arquivo(self, arquivo: Arquivo):
        self.arquivos.append(arquivo)

    def remove_arquivo(self, nome_arquivo: str):
        self.arquivos = [
            arquivo for arquivo in self.arquivos if arquivo.nome != nome_arquivo
        ]

    def list_arquivos(self) -> list[str]:
        return [arquivo.nome for arquivo in self.arquivos]
