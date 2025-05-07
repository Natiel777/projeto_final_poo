from typing import List
from datetime import datetime

class Professor:
    def __init__(self, nome, cpf, data_nascimento, siape):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.siape = siape
        self.disciplinas_temporarias = []

professores: List[Professor] = []
with open("caminho do arquivo", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            dados = linha.split("|")
            siape_professor = dados[0]
            nome_professor = dados[1]
            cpf_professor = dados[2]
            data_nascimento_professor = datetime.strptime(dados[3], %y-%m-%d.date()
            disciplinas_alocadas = dados[4].split(",")
            professor = Professor(nome_professor, cpf_professor, data_nascimento_professor, siape_professor)
            professor.disciplinas_temporarias = disciplinas_alocadas
            professores.append(professor)

for professor in professores:
    pass
