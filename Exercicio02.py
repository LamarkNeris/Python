print("----CODIFICADOR DE NOMES----")
nome = input("Digite um nome: ").upper()
def converteNome(nome):

   if(nome == 'A'):

       return '@'

   if(nome == 'E'):

       return '&'

   if(nome == 'I'):

       return '!'

   if(nome == 'O'):

       return '#'

   if(nome == 'U'):

       return '*'

print(nome)

def main():


   new_name = ''

   for i in nome:

       if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'):

           new_name += converteNome(i.upper())

       else:
           new_name += i.upper()

   print(new_name)

if __name__ == '__main__':

   main()












