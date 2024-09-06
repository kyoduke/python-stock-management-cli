import platform
import os
from classes import Product, ProductStockManagement

platform = platform.system()

clear = 'cls' if 'Windows' in platform else 'clear'

manager = ProductStockManagement()
menu_start = """
[1] - LISTAR PRODUTOS
[2] - ADICIONAR PRODUTO
[3] - ATUALIZAR ESTOQUE
[4] - REMOVER PRODUTO
[5] - SAIR
"""

menu_stock = """
[1] - ADICIONAR QUANTIDADE AO ESTOQUE
[2] - REMOVER QUANTIDADE DO ESTOQUE
[3] - VOLTAR AO MENU INICIAL DO CREG
"""
print("BEM VINDO AO SISTEMA DE GERENCIAMENTO DE ESTOQUE CREG")
exit = False
while not exit:
    print(menu_start)
    command = int(input("O que deseja fazer? "))
    if command in [5, '5'] :
        os.system(clear)
        print("OBRIGADO POR USAR O CREG!")
        exit = True

    elif command in [1, '1']:
        os.system(clear)
        print('PRODUTO | PREÇO | QUANTIDADE')
        for product in manager.get_all_products():
            print(product)

    elif command in [2, '2']:
        os.system(clear)
        name = input('Digite o nome do produto: ')
        price = float(input('Digite o preço do produto: '))
        quantity = int(input('Digite a quantidade em estoque do produto: '))
        product = Product(name, price, quantity)
        manager.add_product(product)
    
    elif command in [3, '3']:
        os.system(clear)
        print(menu_stock)
        option = int(input('O que você deseja fazer?'))
        if option == 3:
            pass

        elif option in [2, '2']:
            os.system(clear)
            for product in manager.get_all_products():
                print(product)
            product_name = input('Digite o nome do produto que deseja atualizar no estoque: ')
            quantity = int(input('Digite a quantidade: '))
            manager.find_and_remove_quantity(product_name, quantity)
        
        else: 
            os.system(clear)
            for product in manager.get_all_products():
                print(product)
            product_name = input('Digite o nome do produto que deseja atualizar no estoque: ')
            quantity = int(input('Digite a quantidade: '))
            manager.find_and_add_quantity(product_name, quantity)

    elif command in [4, '4']:
        os.system(clear)
        for product in manager.get_all_products():
            print(product)
        product_name = input('Digite o nome do produto a ser excluido do estoque: ')
        manager.remove_product(product_name)

    else: 
        os.system(clear)
        print('Comando não reconhecido, tente novamente.')