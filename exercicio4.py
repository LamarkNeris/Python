from random import seed
from random import randint
numero = randint(100, 400)

dados1 = {}
for i in range(5):
    print("************MENU************")
    one = print("1 - Nova inscrição")
    two = print("2 - Visualizar inscrição")
    zero = print("0 - Encerrar")

    choice = int(input("Opção escolhida: "))

    if(choice == 1 ):

        dados1 = { "voucher" : numero ,
        "nome" :  input("Digite o seu nome:"),
        "email" : input("Digite o seu email:"),
        "telefone" :  input("Digite o seu telefone:"),
        "curso" :  input("Digite o seu curso:")}
        dados = [dados1]


    elif(choice == 2):
        print("------------Lista inscritos---------------")
        print("Voucher: {}".format(numero))
        print("Nome: " + dados1["nome"])
        print("E-mail: " + dados1["email"])
        print("Telefone: " + dados1["telefone"])
        print("Curso: " + dados1["curso"])
        print("------------------------")
    elif(choice == 0):
        break
    else:
        print("Erro! Digite uma opção válida")
        break












