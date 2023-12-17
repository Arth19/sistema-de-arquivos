# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Sistema de Arquivos
# Aluno(s): Aildson Ferreira e Arthur Macedo


class Bloco:
    # O bloco é inicializado com tamanho e id, e possui a referência do próximo bloco
    def __init__(self, tamanho: int, id: int):
        self.tamanho = tamanho
        self.id = id
        self.prox_bloco = None

    def encadeia_bloco(self, bloco):
        self.prox_bloco = bloco
