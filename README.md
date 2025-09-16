# 🐾 Sistema de Cadastro de Pets 

Este projeto é um **sistema de cadastro de animais** desenvolvido em Python, utilizando programação orientada a objetos.  
Ele permite **cadastrar, listar e atualizar** informações de pets (cachorros, gatos e coelhos) atendidos na clínica.

---

## 📂 Estrutura do Projeto

- `appy.py` → Arquivo principal que executa o sistema em loop, exibindo o menu de opções.
- `classes.py` → Define as classes do sistema:
  - **Clinica** → Gerencia os animais cadastrados.
  - **Animal** → Classe base para todos os pets (atributos: nome, raça, cor, peso).
  - **Cachorro, Gato e Coelho** → Classes filhas com métodos específicos (latir, miar, chiar).
- `funcoes.py` → Contém as funções principais que interagem com o usuário:
  - `cadastro()` → Cadastro de novos animais (cachorro, gato ou coelho).
  - `listar()` → Lista todos os pets cadastrados.
  - `atualizar()` → Permite alterar características de um pet já cadastrado.

---

## 🛠️ Funcionalidades

✅ **Cadastro de Pets**  
- Permite cadastrar cachorros, gatos e coelhos.  
- Solicita informações como: nome, raça, cor e peso.  

✅ **Listagem de Pets**  
- Exibe todos os animais cadastrados com suas características.  

✅ **Atualização de Dados**  
- Permite alterar **nome, raça, cor ou peso** de um pet.  

✅ **Menu Interativo**  
- Interface simples no terminal para navegar entre as opções.  
