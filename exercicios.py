
# EXERCICIO 01 - Calculadora com fim (while)

'''
sair = False
while sair == False:
    print('Calculadora')
    num1 = int(input('Digite o primeiro número: '))
    operador = input('Digite o operador: ')
    num2 = int(input('Digite o segundo número: '))

    if operador == '+':
            operação = num1 + num2
    if operador == '-':
            operação = num1 - num2
    if operador == '*':
            operação = num1 * num2
    elif operador == '/': 
            operação = num1 / num2
        
    print('Resultado: ')
    print(operação)
    teste = input('Deseja sair? (s ou n ): ')
    print(teste)
    if teste == 's': 
        sair = True 

'''

# EXERCÍCIO 02 - O usuario vai digitar um numero e tera como resposta o seu quadrado 

'''
numero = int(input('Digite o número: '))
quadrado = (numero * numero)
print(quadrado)

'''

# EXERCÍCIO 03 O usário vai digitar seu nome e vai receber como resposta "Bem vindo, seu nome"
'''
nome = input('Digite seu nome aqui: ')
print('Bem vindo,' , nome)
'''
# EXERCÍCIO 04 - O usuário irá digitar dois numeros e terá como resposta os 4 tipos de operações matematicas com eles 
'''
num1 = int(input('Digite o primeiro número'))
num2 = int(input('Digite o segundo número'))
soma = num1 + num2 
subtração = num1 - num2
multiplicação = num1 * num2  
divisão = num1 // num2
print(f'Adição = {soma} , Subtração = {subtração} , Multiplicação = {multiplicação} , Divisão = {divisão}')
'''
# EXERCÍCIO 05 o usuario vai digitar seu ano de nascimento e terá a resposta de quantos anos ele vai ter em 2030

'''
idade = int(input('Digite seu ano de nascimento'))
anos =  2030 - idade
print(f'Em 2030 voce terá {anos} anos')
'''


