class Cadastro:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)
        self.salvar_aluno_em_arquivo(aluno)
        print(f"Aluno {aluno.nome} cadastrado!")

    def cadastrar_professor(self, professor):
        self.professores.append(professor)
        self.salvar_professor_em_arquivo(professor)
        print(f"Professor {professor.nome} cadastrado!")

    def cadastrar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        self.salvar_disciplina_em_arquivo(disciplina)
        print(f"Disciplina {disciplina.nome} cadastrada!")

    def listar_todos(self, lista_entidades):
        for entidade in lista_entidades:
            entidade.exibir_dados()
            print("------")

    def buscar_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        print("Aluno não encontrado.")
        return None

    def buscar_por_siape(self, siape):
        for professor in self.professores:
            if professor.siape == siape:
                return professor
        print("Professor não encontrado.")
        return None

    def buscar_por_codigo_disciplina(self, codigo):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo:
                return disciplina
        print("Disciplina não encontrada.")
        return None

    def salvar_aluno_em_arquivo(self, aluno, caminho="alunos.txt"):
        with open(caminho, "a", encoding="utf-8") as f:
            f.write(f"{aluno.nome};{aluno.cpf};{aluno.data_nascimento};{aluno.matricula}\n")

    def salvar_professor_em_arquivo(self, professor, caminho="professores.txt"):
        with open(caminho, "a", encoding="utf-8") as f:
            f.write(f"{professor.nome};{professor.cpf};{professor.data_nascimento};{professor.siape}\n")

    def salvar_disciplina_em_arquivo(self, disciplina, caminho="disciplinas.txt"):
        with open(caminho, "a", encoding="utf-8") as f:
            f.write(f"{disciplina.codigo};{disciplina.nome};{disciplina.professor_responsavel.nome}\n")
