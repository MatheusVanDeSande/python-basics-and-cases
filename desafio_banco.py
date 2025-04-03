menu = '''

=============== MENU ================
[d] Depositar 
[s] Sacar
[e] Extrato 
[q] Sair 
============ BEM VINDX ==============
'''
LIMITE_SAQUES = 3
saldo = 0 
limite = 500
extrato = ''
numero_saques = 0 

while 1 == 1: 

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor de depósito: '))
        
        if valor > 0:
            print(f'''
             =============================================
               Depósito de R${valor:.2f} feito com sucesso!
             ============================================= 
              
              ''')
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('''
                ============================================  
                Operação falhou!
                ============================================    
                  ''')
           
        
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print('''
                ==============================================
                Operação falhou! Saldo insuficiente.
                ============================================== 
                  ''')
        elif excedeu_limite:
            print('''
                ==============================================
                Operação falhou! Limite insuficiente.
                ============================================== 
                  ''')
        elif excedeu_saques:
            print('''
                ==============================================
                Operação falhou! Limite de saques excedido!
                ============================================== 
                  ''')

        elif valor > 0:
            saldo -= valor 
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
            print(f'''
             =============================================
               Saque de R${valor:.2f} feito com sucesso!
             ============================================= 
              
              ''')
        
        else: 
            print('''
                ==============================================
                Operação falhou! O valor informado é inválido
                ============================================== 
                  ''')

    elif opcao == 'e':
        print('==================EXTRATO======================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('================== :) =========================')
              
        

    elif opcao == 'q':
        print('''
             ==============================================
              Obrigado e volte sempre!
             ============================================== 
              ''')
        break

    else: 
        print('ERRO! - Operação falhou')




