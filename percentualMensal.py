faturamento = {"SP" : 67836.43, "RJ" : 36678.66, "MG" : 29229.88, "ES" : 27165.48,"Outros" : 19849.53} #dicionario com o faturamento de cada estado
total = sum(faturamento.values()) #soma dos valores do dicionario
print("Porcentagem de cada estado com base no faturamento total: ")

for k, v in faturamento.items(): # K representa o estado (chave), v representa os valores (valor)
    quocient = v / total #divisão de cada valor pelo total
    porcent = quocient * 100 #resultado da divisão multiplicado por 100 retorna a porcentagem
    print(k,"-", f'{porcent:.2f}%') #formata o print exibindo apenas 2 casas decimais na porcentagem

