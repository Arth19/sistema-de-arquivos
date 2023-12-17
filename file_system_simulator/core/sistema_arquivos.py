# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Sistema de Arquivos
# Aluno(s): Aildson Ferreira e Arthur Macedo

from .arquivo import Arquivo
from .diretorio import Diretorio
from .bloco import Bloco


class SistemaArquivos:
    # O Sistema de Arquivos é inicializado a partir de uma dada qtd. de blocos e tam. de bloco
    # Um diretório 'root' ou raiz é criado e a memória é gerada a partir do tamanho do bloco e
    #   a quantidade de blocos
    def __init__(self, qtd_blocos: int, tam_bloco: int):
        self.tam_bloco = tam_bloco
        self.memoria = [Bloco(tam_bloco, i) for i in range(qtd_blocos)]
        self.root_dir = Diretorio("root")
        self.diretorios = {"root": self.root_dir}

    def cria_arquivo(
        self, nome_diretorio: str, nome_arquivo: str, tam_arquivo: int
    ) -> str:
        diretorio = self.encontra_diretorio(nome_diretorio)

        if diretorio:
            if not any(arquivo.nome == nome_arquivo for arquivo in diretorio.arquivos):
                arquivo = Arquivo(
                    nome_arquivo, tam_arquivo, self.tam_bloco, self.memoria
                )

                diretorio.adiciona_arquivo(arquivo)

                return f"'{nome_arquivo}' foi criado em '/{nome_diretorio}'. {self.verifica_fragmentacao()}\n"
            else:
                return f"'{nome_arquivo}' já existe em '/{nome_diretorio}'.\n"
        else:
            return f"'/{nome_diretorio}' não encontrado.\n"

    def remove_arquivo(self, nome_diretorio: str, nome_arquivo: str) -> str:
        diretorio = self.encontra_diretorio(nome_diretorio)

        if diretorio:
            candidato_remocao = next(
                (
                    arquivo
                    for arquivo in diretorio.arquivos
                    if arquivo.nome == nome_arquivo
                ),
                None,
            )

            if candidato_remocao:
                for block in candidato_remocao.blocos:
                    self.memoria.append(block)

                diretorio.remove_arquivo(nome_arquivo)

                return f"'{nome_arquivo}' foi removido de '/{nome_diretorio}'. {self.verifica_fragmentacao()}\n"
            else:
                return f"'{nome_arquivo}' não foi encontrado em '/{nome_diretorio}'.\n"
        else:
            return f"'/{nome_diretorio}' não encontrado.\n"

    def lista_arquivos(self, nome_diretorio: str) -> str:
        diretorio = self.encontra_diretorio(nome_diretorio)

        if diretorio:
            return "\n".join(str(arquivo) for arquivo in diretorio.arquivos)
        else:
            return f"'/{nome_diretorio}' não encontrado.\n"

    def encontra_diretorio(self, nome_diretorio: str):
        return self.diretorios.get(nome_diretorio, None)

    def verifica_fragmentacao(self) -> str:
        tem_fragmentacao = any(
            bloco.prox_bloco is not None and bloco.prox_bloco.id != bloco.id + 1
            for bloco in self.memoria
        )

        return "Com Fragmentação" if tem_fragmentacao else "Sem Fragmentação"

    def cria_diretorio(self, nome_diretorio: str) -> str:
        if nome_diretorio not in self.diretorios:
            self.diretorios[nome_diretorio] = Diretorio(nome_diretorio)
            return f"'/{nome_diretorio}' criado.\n"
        else:
            return f"'/{nome_diretorio}' já existe.\n"

    def remove_diretorio(self, nome_diretorio: str) -> str:
        if nome_diretorio != "root":
            if nome_diretorio in self.diretorios:
                diretorio = self.diretorios.pop(nome_diretorio)

                for arquivo in diretorio.arquivos:
                    for bloco in arquivo.blocos:
                        self.memoria.append(bloco)

                return f"'/{nome_diretorio}' foi removido.\n"
            else:
                return f"'/{nome_diretorio}' não encontrado.\n"
        else:
            return "Não é possível remover o diretório raiz.\n"

    def lista_diretorios(self) -> list[str]:
        return list(self.diretorios.keys())
