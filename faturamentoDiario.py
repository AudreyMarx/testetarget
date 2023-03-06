import json

j = open('dados.json',) #abre o arquivo json
lista = json.load(j) #transforma o arquivo em uma lista em que os elementos são dicionarios
valores = [] #lista que guarda os valores da chave "valor"

for k, v in enumerate(lista): # k é o indice de elementos e v é o conteudo dos dicionarios dentro da lista
    for d, f in v.items(): #dentro do dicionario, d equivale a chave e f equivale a valor
        if f <= 30:
            del f #exlui valores zerados e valores respectivos à chave "dia"
        else:
            valores.append(f) #adiciona à lista apenas os valores do faturamento

maximo = max(valores) #valor maximo da lista
minimo = min(valores) #valor minimo
media = sum(valores) / len(valores) #soma todos os valores da lista e divide pela quantidade de itens
cont = 0 #inicia contador

for num in valores:
    if num > media: #conta quantas vezes um numero da lista de valores foi maior que a media
        cont = cont + 1 # incrementa contador

print(f"Maior valor de faturamento: R$ {maximo:,.2f}")
print(f"Menor valor de faturamento: R$ {minimo:,.2f}")
print(f"Média do total de faturamento mensal: R$ {media:,.2f}")
print("Quantidade de dias que o faturamento ultrapassou a média:", cont)
