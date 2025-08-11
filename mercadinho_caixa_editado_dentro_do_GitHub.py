
# Sistema simples de caixa para mercadinho de bairro
# Autor: Projeto fictício para treino de Python
# Versão compatível com ambientes interativos e não interativos

import sys

# Lista de produtos e preços
produtos = {
    "Arroz": 20.0,
    "Feijão": 8.5,
    "Macarrão": 5.0,
    "Leite": 4.5,
    "Pão": 7.0,
    "Miojo": 1.5,
    "Ovo": 10.0,
    "Carne": 50.0
}

carrinho = []
total = 0

print("=== Bem-vindo ao Mercadinho do Bairro ===")
print("Produtos disponíveis:")
for item, preco in produtos.items():
    print(f"{item} - R$ {preco:.2f}")

# Função para detectar ambiente interativo
def ambiente_interativo():
    return sys.stdin.isatty()

if ambiente_interativo():
    # Modo interativo (funciona no VS Code)
    while True:
        escolha = input("\nDigite o nome do produto para adicionar ao carrinho (ou 'fim' para encerrar): ").strip().title()
        
        if escolha.lower() == "fim":
            print("\nFinalizando a compra...")
            break
        elif escolha in produtos:
            carrinho.append(escolha)
            total += produtos[escolha]
            print(f"{escolha} adicionado ao carrinho. Total parcial: R$ {total:.2f}")
        else:
            print("Produto não encontrado. Tente novamente.")
else:
    # Simulação automática (para rodar em ambiente sem input)
    compras_simuladas = ["Arroz", "Leite", "Pão", "Fim"]
    for escolha in compras_simuladas:
        if escolha.lower() == "fim":
            print("\nFinalizando a compra...")
            break
        elif escolha in produtos:
            carrinho.append(escolha)
            total += produtos[escolha]
            print(f"{escolha} adicionado ao carrinho. Total parcial: R$ {total:.2f}")

# Resumo da compra
print("\n=== Compra finalizada ===")
print("Itens no carrinho:")
for item in carrinho:
    print(f"- {item} - R$ {produtos[item]:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado por comprar no Mercadinho do Bairro!")
