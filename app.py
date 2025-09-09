import os
from funcoes import cadastro, listar, atualizar
pets={}
while True:
    input(" ______________________\n |                    |\n |                    |\n |      Cadastro      |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir:")
    escolha=int(input("1º Cadastro\n2º Listar\n3º Atalizar o Cadastro\n4º Sair\n-->"))
    if escolha==1:
        cadastro(pets)
    elif escolha==2:
        listar(pets)
    elif escolha==3:
        atualizar(pets)
    elif escolha==4:
        print("Saindo...")
        os.system("pause")
        break
    else:
        print("Digite Novamente sua escolha...")
        os.system("pause")
