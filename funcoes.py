import re
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    print(" ______________________\n |                    |\n |                    |\n |      Cadastro      |\n |                    |\n |____________________|\n\nRealize seu Cadastro a seguir.")

    # Nome
    while True:
        nome = input("Digite seu nome (apenas letras)\n--> ")
        if nome.replace(" ", "").isalpha():
            nome = nome.title()
            break
        else:
            print("Erro! Digite apenas letras.")
    limpar()

    # Idade
    while True:
        idade = input("Digite sua idade (apenas números)\n--> ")
        if idade.isdigit() and 0 < int(idade) <= 120:
            break
        else:
            print("Erro! Idade inválida.")
    limpar()

    # CPF
    while True:
        cpf = input("Digite seu CPF (11 dígitos)\n--> ")
        if cpf.isdigit() and len(cpf) == 11:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            break
        else:
            print("Erro! CPF inválido.")
    limpar()

    # Email
    while True:
        email = input("Digite seu e-mail\n--> ").strip()
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            break
        else:
            print("Erro! E-mail inválido.")
    limpar()

    # Senha
    while True:
        senha = input("Digite sua senha (até 8 caracteres)\n--> ")
        if len(senha) <= 8:
            break
        else:
            print("Erro! Máximo 8 caracteres.")
    limpar()

    # Pergunta secreta
    print("Configuração da pergunta secreta:")
    pergunta = input("Digite sua pergunta:\n--> ")
    resposta = input("Digite sua resposta:\n--> ").strip().lower()
    limpar()

    # Confirmação
    print("Confirme seus dados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"CPF: {cpf_formatado}")
    print(f"E-mail: {email}")
    print(f"Senha: {senha}")
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta}")

    confirma = input("\nSeus dados estão corretos? (s/n) ").lower()
    if confirma not in ["s", "sim"]:
        print("Cadastro cancelado.")
        return None

    print("\nCadastro concluído com sucesso!")

    return {
        "nome": nome,
        "idade": idade,
        "cpf": cpf_formatado,
        "email": email,
        "senha": senha,
        "pergunta": pergunta,
        "resposta": resposta
    }
