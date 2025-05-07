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
        
    @staticmethod
    def validar_cpf(cpf):
        try:
            return len(str(int(cpf))) == 11
        except ValueError:
            return False

    @staticmethod
    def validar_data(data_nascimento):
        return data_nascimento <= date.now().date()


class Aluno(Pessoa):
    total_alunos = 0 
    
    def __init__(self, nome, cpf, data_nascimento, matricula):
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__notas = []
        self.disciplinas = []
        Aluno.total_alunos += 1

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

    def adicionar_nota(self, disciplina, nota):
        if disciplina in self.disciplinas:
            self.__notas.append(nota)
        else:
            print("Aluno não está matriculado nesta disciplina.")

    def calcular_media(self, disciplina):
        if disciplina in self.disciplinas:
            if len(self.__notas) == 0:
                return 0
            return sum(self.__notas) / len(self.__notas)
        else:
            print("Aluno não está matriculado nesta disciplina.")
            return 0

    def matricular_em_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.adicionar_aluno(self)

    def desmatricular_disciplina(self, codigo_disciplina):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo_disciplina:
                self.disciplinas.remove(disciplina)
                disciplina.alunos_matriculados.remove(self)
                break
        else:
            print(f"Disciplina com código {codigo_disciplina} não encontrada.")
            
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
    total_professores = 0
    
    def __init__(self, nome, cpf, data_nascimento, siape):
        super().__init__(nome, cpf, data_nascimento)
        self.__siape = siape
        self.disciplinas = []
        Professor.total_professores += 1

    @property
    def siape(self):
        return self.__siape

    @siape.setter
    def siape(self, siape):
        self.__siape = siape

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.professor_responsavel = self

    def remover_disciplina(self, codigo_disciplina):
        for disciplina in self.disciplinas:
            if disciplina.codigo == codigo_disciplina:
                self.disciplinas.remove(disciplina)
                disciplina.professor_responsavel = None
                break
        else:
            print(f"Disciplina com código {codigo_disciplina} não encontrada.")
    
    def exibir_dados(self):  
        print(f"Nome do Professor: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"SIAPE: {self.__siape}")
        print("Disciplinas lecionadas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} ({disciplina.codigo})")
