from persistencia import Persistencia
class Disciplina:
    def __init__(self, disciplina, nome, professor_responsavel):
        self.disciplina = disciplina
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []

    def exibir_dados(self):
            print(f"Disciplina: {self.nome} ({self.disciplina})")
        if self.professor_responsavel:
            print(f"Professor Responsável: {self.professor_responsavel.nome}")
        else:
            print("Professor Responsável: Não atribuído")
            print("Alunos Matriculados:")
        if self.alunos_matriculados:
            for aluno in self.alunos_matriculados:
            print(f"  - {aluno.nome}")
        else:
            print("Nenhum aluno matriculado.")

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_matriculados:
           self.alunos_matriculados.append(aluno)
        if self not in aluno.disciplinas:
           aluno.disciplinas.append(self)

    def atribuir_ao_professor(self):
        if self not in self.professor_responsavel.disciplinas:
           self.professor_responsavel.disciplinas.append(self)
