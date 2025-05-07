class Disciplina:
    def __init__(self, codigo, nome, professor_responsavel):
        self.codigo = codigo
        self.nome = nome
        self.professor_responsavel = professor_responsavel
        self.alunos_matriculados = []

    def exibir_dados(self):
        print(f"Disciplina: {self.nome} ({self.codigo})")
        print(f"Professor Responsável: {self.professor_responsavel.nome}")
        print("Alunos Matriculados:")
        for aluno in self.alunos_matriculados:
            print(f"  - {aluno.nome}")

    def adicionar_aluno(self, aluno):
    if aluno not in self.alunos_matriculados:
        self.alunos_matriculados.append(aluno)
    if self not in aluno.disciplinas:
        aluno.disciplinas.append(self)

    def atribuir_ao_professor(self):
    if self not in self.professor_responsavel.disciplinas:
        self.professor_responsavel.disciplinas.append(self)
