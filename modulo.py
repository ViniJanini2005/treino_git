class Erro(Exception):
    ...

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.validar_idade(idade)

    def validar_idade(self, idade):
        if idade < 18:
            raise Erro('Idade menor que 18')
        self.idade = idade

    def saudacao(self):
        return f'Olá, meu nome é {self.nome}'