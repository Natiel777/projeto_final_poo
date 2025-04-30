from abc import ABC, abstractmethod
from datetime import datetime as dt
from disciplina import Disciplina

class Pessoa(ABC):
	def __init__(self, nome: str, cpf: str, data_nascimento: date):
         self.nome = nome
         self.__cpf = cpf
         self.data_nascimento = data_nascimento

    @abstractmethod
    def exibir_dados(self):
        pass

    def get_cpf(self):
        return self.__cpf
        
class Aluno(Pessoa):
	def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def exibir_dados(self):
        print(f"Aluno: {self.nome}, Nascimento: {self.data_nascimento}")
        print("Disciplinas matriculadas:")
        for d in self.disciplinas:
            print(f"  - {d.nome} ({d.codigo})")
            
class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []

    def exibir_dados(self):
        print(f"Professor: {self.nome}, Nascimento: {self.data_nascimento}")
        print("Disciplinas lecionadas:")
        for d in self.disciplinas:
            print(f"  - {d.nome} ({d.codigo})")
            
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