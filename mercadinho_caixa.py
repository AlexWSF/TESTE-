
# Sistema simples de caixa para mercadinho de bairro
# Autor: Projeto fictício para treino de Python

# Lista de produtos e preços
produtos = {
    "Arroz": 20.0,
    "Feijão": 8.5,
    "Macarrão": 5.0,
    "Leite": 4.5,
    "Pão": 7.0
}

carrinho = []
total = 0

print("=== Bem-vindo ao Mercadinho do Bairro ===")
print("Produtos disponíveis:")
for item, preco in produtos.items():
    print(f"{item} - R$ {preco:.2f}")

while True:
    escolha = input("\nDigite o nome do produto para adicionar ao carrinho (ou 'fim' para encerrar): ").strip().title()
    
    if escolha == "Fim":
        break
    elif escolha in produtos:
        carrinho.append(escolha)
        total += produtos[escolha]
        print(f"{escolha} adicionado ao carrinho. Total parcial: R$ {total:.2f}")
    else:
        print("Produto não encontrado. Tente novamente.")

print("\n=== Compra finalizada ===")
print("Itens no carrinho:")
for item in carrinho:
    print(f"- {item} - R$ {produtos[item]:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado por comprar no Mercadinho do Bairro!")
