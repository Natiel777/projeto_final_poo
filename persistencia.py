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
with open("professores.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            dados = linha.split("|")
            siape_professor = dados[0]
            nome_professor = dados[1]
            cpf_professor = dados[2]
            data_nascimento_professor = datetime.strptime(dados[3], "%Y-%m-%d")
            disciplinas_alocadas = dados[4].split(",")
            professor = Professor(nome_professor, cpf_professor, data_nascimento_professor, siape_professor)
            professor.disciplinas_temporarias = disciplinas_alocadas
            professores.append(professor)

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    for aluno in []:
        arquivo.write(f"{aluno.nome}|{aluno.cpf}|{aluno.data_nascimento.strftime('%Y-%m-%d')}|{aluno.matricula}\n")

with open("disciplinas.txt", "w", encoding="utf-8") as arquivo:
    for disciplina in []:
        arquivo.write(f"{disciplina.codigo}|{disciplina.nome}|{disciplina.professor_responsavel.nome}\n")
