from funcionario import Funcionario
import os 

f1 = Funcionario("Pedro", "Cafetão", 1000000)

# f1.dados()

# print(f1.registrarPonto())

# valor = int(input("Digite um valor: "))

# f1.descontarSalario(valor)

# f1.dados()

print (f1.promover("Pastor", 305000))

os.system("cls")

print(f1.calcularBonus())