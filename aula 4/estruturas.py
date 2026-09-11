lista = [10,20,30]
# Vetor(lista): mutável, ordenado e indexável (0...n)

tupla = (10,20,30)
tuplaB = (30,40,50)
tupla[1] = 12

print(tupla)
tupla = tuplaB #Sobrescreveu a primeira tupla
print(tupla)
# Tupla: imutável, ordenada e indexavel (0...n)

dic = {"n1": 10, "n2": 20, "n3": 30}
# Dicionário: mutável, ordenado desde a v3.7.x, acessado pela chave

matriz = [[10,20,30]]
# Matriz

print(type(lista))
print(type(tupla))
print(type(dic))
print(type(matriz))