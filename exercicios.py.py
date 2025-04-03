# EXERCÍCIO 01 
# usuário vai digitar um valor e terá a resposta do valor digitado + 100% 

valor_digitado = int(input('Digite o valor: '))                             # estava na formas str e foi p int
taxa_aumento = 1.0                                                          # 100% em python 
print(f'''
=======================================      



Valor digitado:{valor_digitado}
Taxa com Aumento:R${valor_digitado * taxa_aumento + valor_digitado}            

          
      
      
=======================================      
      
''')
# soma entre float e int sempre dá um float 

# EXERCÍCIO 02 - Usuário digita um numero e terá um acrescimo de 50% 

# valor_produto = float(input('Digite o valor do produto: R$'))
# taxa_revenda = 0.5 
# valor_revenda = valor_produto * taxa_revenda + valor_produto
# print(f'''
# =========================================
# Valor Original: {valor_produto}
# Valor Revenda:  {valor_revenda}
    
    
# ========================================
          
#       ''')

 
# EXERCÍCIO 03 - usuário digita um valor de um investimento e o programa vai retornar 30% do valor que é o seu retorno 

# valor_investimento = float(input('Digite o valor do investimento: R$'))
# TAXA = 0.3                                                                                              # CONSTANTE 
# valor_retorno = valor_investimento * TAXA

# print(f'''
# ==============================================
# Valor investido: R$ {valor_investimento}
# O seu retorno do investimento é: R$ {valor_retorno}
      
# ==============================================      
#       ''')


# EXERCÍCIO 04 - Usuário digita o valor do seu salário e o programa vai aumentar 15% 

# valor_salario = float(input('Digite o valor do seu salário:  R$'))
# aumento = 0.15 
# novo_salario = valor_salario * aumento + valor_salario

# print(f'''
# ======================================================
# Valor do seu salário atual: R$ {valor_salario}
# Valor do seu novo salário:  R${novo_salario}

# ====================================================== 
      
#       ''')

# EXERCÍCIO 05 - usuário digita o valor de um produto e o programa vaiu descontar 7% do valor do produto 

# valor_produto = float(input('Digite o valor do produto: R$'))
# DESCONTO = 0.07 
# novo_valor =  valor_produto - valor_produto * DESCONTO                      # mudou o local do - valor_produto do final apra o inicio 

# print(f'''
# =============================================== 
#       Valor antigo: R${valor_produto}
#       Valor Atual:  R${novo_valor}
# ===============================================     
      
      
      
#       ''')