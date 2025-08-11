
# Relatório do Projeto - Sistema de Caixa para Mercadinho de Bairro

## Objetivo
O objetivo deste projeto foi desenvolver um sistema simples em Python para simular o funcionamento de um caixa de mercadinho de bairro. 
O sistema deve permitir registrar produtos escolhidos pelo cliente, calcular o total da compra e exibir um resumo final.

## Funcionalidades
- **Lista de produtos pré-cadastrada** com seus respectivos preços.
- **Adição de produtos ao carrinho** por meio da entrada de dados.
- **Cálculo do valor total** conforme os produtos são adicionados.
- **Resumo final** da compra, listando todos os itens e o valor total a pagar.

## Tecnologias Utilizadas
- **Linguagem de programação:** Python 3
- **Recursos usados:** dicionários, listas, laços de repetição (`while`), estrutura condicional (`if/elif/else`) e função `input()`.

## Como Funciona
1. O sistema apresenta ao usuário a lista de produtos disponíveis.
2. O usuário digita o nome do produto que deseja comprar.
3. O produto é adicionado ao carrinho e o total é atualizado.
4. O usuário digita "fim" para encerrar a compra.
5. O sistema exibe um relatório com todos os itens comprados e o valor total.

## Exemplo de Uso
```
=== Bem-vindo ao Mercadinho do Bairro ===
Produtos disponíveis:
Arroz - R$ 20.00
Feijão - R$ 8.50
Macarrão - R$ 5.00
Leite - R$ 4.50
Pão - R$ 7.00

Digite o nome do produto para adicionar ao carrinho (ou 'fim' para encerrar): Arroz
Arroz adicionado ao carrinho. Total parcial: R$ 20.00

Digite o nome do produto para adicionar ao carrinho (ou 'fim' para encerrar): Leite
Leite adicionado ao carrinho. Total parcial: R$ 24.50

Digite o nome do produto para adicionar ao carrinho (ou 'fim' para encerrar): fim

=== Compra finalizada ===
Itens no carrinho:
- Arroz - R$ 20.00
- Leite - R$ 4.50
Total a pagar: R$ 24.50
Obrigado por comprar no Mercadinho do Bairro!
```

## Conclusão
Este sistema cumpre o objetivo de simular um caixa simples para um mercadinho de bairro. 
Embora seja um projeto simples, é funcional e pode ser expandido para incluir recursos como banco de dados, 
controle de estoque e geração de recibos.
