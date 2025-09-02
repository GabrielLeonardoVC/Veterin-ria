from classes import Cachorro, Gato, Passaro
from funcoes import login
dados = login()
input(" ________________________________\n |                              |\n |                              |\n |     Cadastro concluido       |\n |                              |\n |______________________________|")
zen = Gato(nome="Zen", peso=4, raca="Siames", cor="Cinza", idade=4)
pitica = Cachorro(nome="Pitica", peso=6, raca="Pinscher", cor="Preto e Marrom", idade=8)
estrelinha = Passaro(nome="Estrelinha", peso=1, raca="Canário", cor="Amarelo", idade=2)
print("\nDados do Gato:")
print(f"Nome: {zen.getNome()}")
print(f"Cor: {zen.getCor()}")
print(f"Raça: {zen.getRaca()}")
zen.setNome("Toddy")
print(f"Novo nome: {zen.getNome()}")
