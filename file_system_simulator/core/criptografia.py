# UFRPE - Universidade Federal Rural de Pernambuco
# Sistemas Operacionais - 2023.1
#
# 2VA - Segurança
# Aluno(s): Aildson Ferreira e Arthur Macedo


def codifica(senha: str) -> str:
    # Função para codificar uma senha, utilizando substituição
    senha_codificada = []
    cripto = "substituicao_xor"

    for i, char in enumerate(senha):
        character = cripto[i % len(cripto)]
        senha_codificada.append(chr((ord(char) + ord(character)) % 256))

    return "".join(senha_codificada)


def descodifica(senha_codificada: str) -> str:
    senha_descodificada = []
    cripto = "substituicao_xor"

    for i, char in enumerate(senha_codificada):
        character = cripto[i % len(cripto)]
        senha_descodificada.append(chr((ord(char) - ord(character)) % 256))

    return "".join(senha_descodificada)
