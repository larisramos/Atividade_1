'''1)Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c. Se o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário, se i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4. '''
i = int(input('Digite um valor: '))
if i<=0:
  print ('Valor inválido! Digite um valor inteiro maior que zero!!!')
else:
  a = float(input('Digite o valor de A: '))
  b = float(input('Digite o valor de B: '))
  c = float(input('Digite o valor de C: '))
  if i%2==0:
    media1 = (a+b+c)/3
    print(f'A média aritmética de A({a}), B({b}) e C({c}) é {media1}')
  elif i>10:
    media1 = (a+b+c)/3
    media2 = ((a*2)+(b*3)+(c*4))/2+3+4
    print(f'As  médias de A({a}), B({b}) e C({c}) respectivamente são a aritmética igual à {media1} e a ponderada igual a {media2}')