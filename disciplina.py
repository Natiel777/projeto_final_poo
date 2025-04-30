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
        self.alunos_matriculados.append(aluno)
        aluno.disciplinas.append(self)

    def atribuir_ao_professor(self):
        self.professor_responsavel.disciplinas.append(self)