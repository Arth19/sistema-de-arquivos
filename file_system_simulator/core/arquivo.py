# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Sistema de Arquivos
# Aluno(s): Aildson Ferreira e Arthur Macedo

from .bloco import Bloco


class Arquivo:
    # Cada arquivo possui nome e tamanho, e será alocado um espaço na memória com a qtd
    # de blocos necessária para o arquivo
    def __init__(self, nome: str, tamanho: int, tam_bloco: int, memoria: list[Bloco]):
        self.nome = nome
        self.tamanho = tamanho
        self.blocos = self.aloca_memoria(tamanho, tam_bloco, memoria)

    def aloca_memoria(
        self, tamanho: int, tam_bloco: int, memoria: list[Bloco]
    ) -> list[Bloco]:
        qtd_blocos_alocacao = tamanho // tam_bloco
        blocos_alocados: list[Bloco] = []

        for _ in range(qtd_blocos_alocacao):
            if memoria:
                bloco = memoria.pop(0)
                blocos_alocados.append(bloco)

                if len(blocos_alocados) > 1:
                    blocos_alocados[-2].encadeia_bloco(bloco)

        return blocos_alocados

    def __str__(self):
        info_blocos = ", ".join(f"Bloco (ID: {bloco.id})" for bloco in self.blocos)

        return f"Arquivo (Nome: {self.nome}, Tamanho: {self.tamanho}, Blocos: [{info_blocos}])"
