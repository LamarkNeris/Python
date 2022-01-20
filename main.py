print("----SISTEMA DE MATRÍCULAS---- ")

nome = input("Nome da criança: ")
idade = int(input("Idade: "))
if 1 <= idade <= 5:
    print("O aluno (a) {} tem {} anos e está no ensino infantil.".format(nome, idade))
elif 6 <= idade <= 10:
    print("O aluno (a) {} tem {} anos e está no ensino fundamental I.".format(nome, idade))
elif 11 <= idade <= 14:
    print("O aluno (a) {} tem {} anos e está no ensino fundamental II.".format(nome, idade))
elif idade >= 15:
    print("O aluno (a) {} tem {} anos e está no ensino médio.".format(nome, idade))
else:
    print("Insira um nome ou idade válidos")

print("Deseja continuar?")
print("0 - Não       1 - Sim ")
