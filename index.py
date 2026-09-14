#Funções definidas pelo usuario
def calcularDesconto(valor, percentual):
  #Calcula o valor final aplicando um desconto percentual

    if percentual < 0 or percentual > 100:
       return None #Marcação invalida
    desconto = valor * (percentual/100)
    return valor - desconto

#Função resgistrar venda
def regristrarVendas(produto, valorFinal):
  #Registro de uma venda
    print(f"Venda Registrada:{produto} por R${valorFinal:.2f}")

#Função lambda para arredondar
arredondar = lambda valor: round(valor, 2)

#Variaveis principais do pdv
totalVendas = 0
qtdVendas = 0

#Loop principal do caixa. MINHALOJAPDV
while True:
  print('\n----- minha loja - pdv-----')
  print('0 - Encerrar Caixa')
  print('1 - Registrar Venda')  
  print('2 - Relatorio do Dia')
  

  opcao = input('Escolha uma opção: ')
  if opcao == '0':
    print('Encerrando Caixa...')
    break

  elif opcao == '1':
    produto = input('Nome do Produto: ')
    valor = float(input('Valor do Produto: '))
    percentual = float(input('Percentual de Desconto: '))

    valorFinal = calcularDesconto(valor, percentual)

    if valorFinal is None:
       print('Percentual Invalido')
    else:
       valorFinal = arredondar(valorFinal)
       regristrarVendas(produto, valorFinal)
       totalVendas += valorFinal
       qtdVendas += 1

  elif opcao == '2':
    print(f'\Vendas Hoje: {qtdVendas}')
    print(f'Total de Vendas: R$ {arredondar(totalVendas)}')

  else:
    print('Opção invalida. Tente de novo.')