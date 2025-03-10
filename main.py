from modulo import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, registro):
        super().__init__(nome, idade)
        self.registro = registro

class Aluno(Pessoa):
    def __init__(self, nome, idade, registro):
        super().__init__(nome, idade)
        self.registro = registro