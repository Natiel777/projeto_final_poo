from pessoa import Professor, Aluno, Disciplina
from datetime import datetime

professores = []
alunos = []
disciplinas = []

professores_dict = {}
alunos_dict = {}

try:
    with open("professores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                linha = linha.strip()
                if linha:
                    siape, nome, cpf, data_str, disci_str = linha.split("|")
                    data_nasc = datetime.strptime(data_str, "%Y-%m-%d").date()
                    professor = Professor(nome, cpf, data_nasc, siape)
                    professor.disciplinas_temporarias = disci_str.split(",") if disci_str else []
                    professores.append(professor)
                    professores_dict[nome] = professor
            except Exception as e:
                print(f"Erro ao processar linha de professor: {e}")
except FileNotFoundError:
    print("Arquivo 'professores.txt' não encontrado.")

try:
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                linha = linha.strip()
                if linha:
                    partes = linha.split("|")
                    nome, cpf, data_str, matricula = partes[:4]
                    data_nasc = datetime.strptime(data_str, "%Y-%m-%d").date()
                    aluno = Aluno(nome, cpf, data_nasc, matricula)
                    aluno.disciplinas_temporarias = []  
                    for info in partes[4:]:
                        campos = info.split(",")
                        disc_nome = campos[0]
                        notas = list(map(float, campos[1:]))
                        aluno.disciplinas_temporarias.append((disc_nome, notas))
                    alunos.append(aluno)
                    alunos_dict[nome] = aluno
            except Exception as e:
                print(f"Erro ao processar linha de aluno: {e}")
except FileNotFoundError:
    print("Arquivo 'alunos.txt' não encontrado.")

try:
    with open("disciplinas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                linha = linha.strip()
                if linha:
                    codigo, nome_disc, prof_nome, alunos_str = linha.split("|")
                    if prof_nome in professores_dict:
                        prof = professores_dict[prof_nome]
                        disc = Disciplina(codigo, nome_disc, prof)
                        disc.alunos_temporarios = alunos_str.split(",") if alunos_str else []
                        disciplinas.append(disc)
                    else:
                        raise ValueError(f"Professor '{prof_nome}' não encontrado.")
            except Exception as e:
                print(f"Erro ao processar linha de disciplina: {e}")
except FileNotFoundError:
    print("Arquivo 'disciplinas.txt' não encontrado.")

for aluno in alunos:
    for nome_disc, notas in aluno.disciplinas_temporarias:
        for disc in disciplinas:
            if disc.nome == nome_disc:
                disc.matricular_aluno(aluno)
                for n in notas:
                    aluno.adicionar_nota(n)
                break

for disc in disciplinas:
    for nome_al in disc.alunos_temporarios:
        for aluno in alunos:
            if aluno.nome == nome_al:
                disc.matricular_aluno(aluno)
                break

print("\n- PROFESSORES -")
for professor in professores:
    professor.exibir_dados()

print("\n- ALUNOS -")
for aluno in alunos:
    aluno.exibir_dados()

print("\n- DISCIPLINAS -")
for disc in disciplinas:
    disc.exibir_informacoes()
