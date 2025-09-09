import os

from funcoes import *

while True:
    try:
        os.system("cls")
        print("BEM VINDO AO SISTEMA DE CADASTRO")
        print("SELECIONE A OPÇÃO QUE DESEJA")
        print("1 - CADASTRO")
        print("2 - LISTAR")
        print("3 - ATUALIZAR CADASTRO")
        print("0 - SAIR")
        escolha = int(input("--> "))

        match escolha:
            case 1:
                cadastro()
            case 2:
                listar()
            case 3:
                atualizar()
            case 0:
                print("SAINDO...")
                os.system("pause")
                break
            case _:
                print("ESCOLHA INVALIDA")
                os.system("pause")

    except Exception as e:
        print(f"Ocorreu um erro Inesperado: {e}")
        os.system("pause")