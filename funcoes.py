import os
from classes import *

CliSenai = Clinica("Clinica_Senai", "Jundiai")

def cadastro():
    while True:
        os.system("cls")
        print("--TELA DE CADASTRO---")
        print("")
        especie = int(input("Informe a especie do seu pet\n1 - Cachorro\n2 - Gato\n3 - Coelho\n0 - SAIR\n--> "))
        if especie > 0 and especie < 4:
            nome = input("Informe o nome do pet: ")
            raca = input("Informe a raça do pet: ")
            cor = input("Informe a cor do pet: ")
            peso = float(input("Informe o peso do pet: "))
            
            if especie == 1:
                CliSenai.cadastroCachorro(nome=nome, raca=raca, cor=cor, peso=peso)
                print("\nCachorro adicionado com sucesso")
                while True:
                    opcao = int(input("1 - Adicionar outro pet\n0 - Sair\n--> "))
                    if opcao == 1 or opcao == 0:
                        break
                if opcao == 0:
                    break

            elif especie == 2:
                CliSenai.cadastroGato(nome=nome, raca=raca, cor=cor, peso=peso)
                print("\nGato adicionado com sucesso")
                while True:
                    opcao = int(input("1 - Adicionar outro pet\n0 - Sair\n--> "))
                    if opcao == 1 or opcao == 0:
                        break
                if opcao == 0:
                    break

            elif especie == 3:
                CliSenai.cadastroCoelho(nome=nome, raca=raca, cor=cor, peso=peso)
                print("\nCoelho adicionado com sucesso")
                while True:
                    opcao = int(input("1 - Adicionar outro pet\n0 - Sair\n--> "))
                    if opcao == 1 or opcao == 0:
                        break
                if opcao == 0:
                    break

        elif especie == 0:
            print("SAINDO... ")
            os.system("pause")
            break
        else:
            print("Especie Invalida")
            while True:
                tentativa = int(input("1 - Tentar novamente\n0 - SAIR\n--> "))
                if tentativa == 0 or tentativa == 1:                    
                    break
            if tentativa == 0:
                break
                
def listar():
    os.system("cls")
    print("--LISTAR TODOS OS PETS---")
    print("")
    
    for chave, valor in CliSenai.listar().items():
        print(f"{chave}° - \t{valor.getNome()}\n\t{valor.getRaca()}\n\t{valor.getCor()}\n\t{valor.getPeso()}")
    
    os.system("pause")

def atualizar():
    listar()

    alterar = int(input("Informe o pet que deseja alterar\n-->"))
    caracteristica = int(input("Qual caracteristica quer alterar\n1 - Nome\n2 - Raca\n3 - Cor\n4 - Peso\n-->"))

    if caracteristica == 1:
        nome = input("Informe o nome do PET\n-->")
        CliSenai.alterarNome(id=alterar, nome=nome)
    elif caracteristica == 2:
        raca = input("Informe o raça do PET\n-->")
        CliSenai.alterarRaca(id=alterar, raca=raca)
    elif caracteristica == 3:
        cor = input("Informe o cor do PET\n-->")
        CliSenai.alterarCor(id=alterar, cor=cor)
    elif caracteristica == 4:
        peso = input("Informe o peso do PET\n-->")
        CliSenai.alterarPeso(id=alterar, peso=peso)

    listar()