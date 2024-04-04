import os

class CarrinhoHotweels:
    def __init__(self, nome, cor, modelo, ano):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

def cadastrar_carrinho():
    nome = input('Informe o nome do carrinho: ')
    cor = input('Informe a cor do carrinho: ')
    modelo = input('Informe o modelo do carrinho: ')
    while True:
        try:
            ano = int(input('Informe o ano: '))
            print('Cadastro realizado com sucesso!')
            break
        except ValueError:
            print("Por favor, insira um ano válido.")
            
    return CarrinhoHotweels(nome, cor, modelo, ano)

def salvar_carrinhos(carrinhos):
    try:
        with open("carrinhos.txt", "w") as file:
            for carrinho in carrinhos:
                file.write(f"{carrinho.nome},{carrinho.cor},{carrinho.modelo},{carrinho.ano}\n")
        print("Cadastro dos Carrinhos realizado com sucesso!")
    except IOError:
        print("Erro ao salvar os carrinhos.")

def listar_carrinhos(carrinhos):
    print('Lista de carrinhos cadastrados:')
    for i, carrinho in enumerate(carrinhos, start=1):
        print(f'{i}. Nome: {carrinho.nome}, Cor: {carrinho.cor}, Modelo: {carrinho.modelo}, Ano: {carrinho.ano}')

def main():
    carrinhos = []

    while True:
        print('\n***MENU***')
        print('1. Cadastrar novo carrinho')
        print('2. Listar carrinhos cadastrados')
        print('3. Salvar carrinhos')
        print('4. Sair')

        opcao = input('Por favor, escolha a opção desejada: ')

        if opcao == "1":
            carrinhos.append(cadastrar_carrinho())
        elif opcao == "2":
            if carrinhos:
                listar_carrinhos(carrinhos)
            else:
                print('Ops! Você ainda não tem carrinhos cadastrados.')
        elif opcao == "3":
            if carrinhos:
                salvar_carrinhos(carrinhos)
            else:
                print('Não há carrinhos para salvar.')
        elif opcao == "4":
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Por favor, escolha novamente!')

if __name__ == '__main__':
    main()
