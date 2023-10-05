from datetime import date
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def dados(self):
        print(f"{self.nome} seu cargo é {self.cargo} e seu salário é {self.salario}")

    def registrarPonto(self):
        return f"Ponto Registrado na data {date.today()}"
    
    def descontarSalario(self, valor):
        if valor < 0:
            print("Operação inválida")
        else:
            resultado = self.salario - valor
            print(f"Esse é seu novo salario R${resultado}")
            self.salario = resultado
        
    def promover(self, novoCargo, novosalario):
        self.cargo = novoCargo
        self.salario = novosalario
        return f"Promovido para {self.cargo} com salário de R${self.salario}"
    
    def calcularBonus(self):
        bonus = self.salario * 0.1 #calculando 10% do salário
        return bonus