import os
from classes import Cachorro,Gato,Coelho
def cadastro(pets):
    while True:
        os.system("cls")
        input(" ______________________\n |                    |\n |                    |\n |      Cadastro      |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir:")
        especie=int(input("Digite a espécie do seu pet\n1º Cachorro\n2º Gato\n3º Coelho\n0º Sair\n-->"))
        os.system('cls')
        if especie==4:
            print("Saindo...")
            os.system("pause")
            break
        if especie in [1, 2, 3]:
            nome=input("Digite o nome do seu pet:")
            os.system('cls')
            raca=input("Digite a raça do seu pet:")
            os.system('cls')
            cor=input("Digite a cor do seu pet:")
            os.system('cls')
            peso=float(input("Digite o peso do seu pet:"))
            os.system('cls')
            if especie==1:
                novopet=Cachorro(nome,peso,raca,cor)
                especienome="Cachorro"
            elif especie==2:
                novopet=Gato(nome,peso,raca,cor)
                especienome="Gato"
            else:
                novopet=Coelho(nome,peso,raca,cor)
                especienome="Coelho"
            pets[len(pets)+1]=novopet
            print(f"\n{especienome} adicionado com sucesso!")
            os.system('cls')
            opcao=int(input("1º Adicionar outro pet\n4º Sair\n-->"))
            os.system('cls')
            if opcao==4:
                break
        else:
            print("Informação Inválida")
            tentativa=int(input("1º Tentar novamente\n4º Sair\n-->"))
            if tentativa==0:
                break
def listar(pets):
    os.system("cls")
    print("Lista de todos os pets a seguir\n")
    for chave, pet in pets.items():
        print(f"{chave}°-\tNome:{pet.get_nome()}\n\tRaça:{pet.get_raca()}\n\tCor:{pet.get_cor()}\n\tPeso:{pet.get_peso()}")
    os.system("pause")
def atualizar(pets):
    listar(pets)
    alterar = int(input("Digite o número do pet que você deseja alterar\n--> "))
    if alterar not in pets:
        print("Ops... Esse pet não foi encontrado! Veja se suas informações estão corretas.")
        os.system("pause")
        return
    caracteristicas=int(input("Qual característica você deseja alterar?\n1º Nome\n2º Raça\n3º Cor\n4º Peso\n-->"))
    if caracteristicas==1:
        pets[alterar].set_nome(input("Nome novo:"))
    elif caracteristicas==2:
        pets[alterar].set_raca(input("Raça nova:"))
    elif caracteristicas==3:
        pets[alterar].set_cor(input("Cor nova:"))
    elif caracteristicas==4:
        pets[alterar].set_peso(float(input("Novo peso:")))
    print("\nSeu pet foi atualizado com sucesso!")
    listar(pets)
