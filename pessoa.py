from abc import ABC, abstractmethod
from datetime import datetime as date
from disciplina import Disciplina

class Pessoa(ABC):
    def __init__(self, nome, cpf, data_nascimento=date(1900, 1, 1)):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @abstractmethod
    def exibir_dados(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Notas: {self.__notas}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome}") 


class Professor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []

    @property
    def siape(self):
        return self.__siape

    @siape.setter
    def siape(self, siape):
        self.__siape = siape

    def exibir_dados(self):  
        print(f"Nome do Professor: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"SIAPE: {self.__siape}")
        print("Disciplinas lecionadas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")


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
