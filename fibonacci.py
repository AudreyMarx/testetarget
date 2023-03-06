n = int(input("Informe um número de 0 a 100 para pesquisar na Fibonacci: "))

ultimo = 0
penultimo = 0
fibonacci = [] #lista que vai incluir os numeros da fibo
print("\n") #quebra de linha
while (ultimo < 100):
    fibonacci.append(ultimo) #acrescenta à lista o ultimo numero a cada repetição
    termoAtual = ultimo + penultimo #soma dos 2 numeros anteriores
    penultimo = ultimo
    ultimo = termoAtual
    if (ultimo == 0):
        ultimo = ultimo + 1 #incremento da variável que foi inicializada em 0
if (n in fibonacci): #verifica se o numero informado está na lista da fibo
    print("Esse número faz parte da Fibonacci")
else:
    print("Este número não está na Fibonacci")
print("\n")
print("Números até 100 pertencentes à Fibonacci :")
print(fibonacci) #lista da fibo com todos os elementos incluidos
