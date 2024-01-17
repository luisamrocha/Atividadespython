#listas possuem indice
# o indice da lista começa sempre pelo zero!!!
# minha_lista = ["fernando",True,"NATHALIA",3.15,"Mirela"]
# print(minha_lista[1])
#O metodo append add no final da lista 
# lista = []
# lista.append("Luisa")
# print(lista)
'''
lista = ["água","chocolate", "celular", "dente"]

lista.insert(4,"batata")
print(lista)
'''

# lista = ["água", "chocolate", "celular", "dente"]

# print(lista.index("chocolate"))

# lista.pop()
# print(lista)

# lista.extend(["brasil", "argentina", "uruguai"] )
# print(lista)

# lista = ["Sophia", "Adriano", "Claudia", "Angela", "Luísa", "Fernando"]

# # lista.sort()
# # print(lista)

# lista[2]="Nathalia"
# print(lista)'''

# #Escreva um programa que recebe uma lista de números e retorna uma nova lista apenas com os números pares.

# # criei uma lista 
# lista= []
# #eu falei quantos itens eu queria que tivesse na lista 
# for i in range(3):
# #solicite ao usuário
#     numeros=int(input("Digite um número "))
# #verifiquei se são pares 
#     if numeros%2==0: 
# # pedi para criar a lista apenas com os pares adicionando sempre no final
#         lista.append(numeros)
# #pintei a lista 
# print(lista)

# #[LP-A04] Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

# lista = []

# while True:
#     numero_pedido = int(input("Digite um número "))
#     if numero_pedido ==0:
#         print(len(lista))
#         print(sum(lista))
#         print(sum(lista)/len(lista))
#         break
#     else:
#         lista.append(numero_pedido) 


#Escreva uma função que recebe uma lista de palavras e retorna uma nova lista contendo apenas as palavras que possuem mais de 5 caracteres.

# lista=[]
# listacerta= []
# for i in range(4):
#     palavra_pedida= str(input("digite uma palavra "))
#     lista.append(palavra_pedida)
# for i in lista:
#     if len(i)>5:
#         listacerta.append(i)
# print(listacerta)

#Escreva uma função que recebe duas listas e retorna uma nova lista contendo #apenas os elementos comuns entre as duas listas.

# lista=["palavra", "play", "água", "celular"]
# lista2=["palavra", "amor", "paz", "legal"]
# lista3= []

# for i in lista:
#     if i in lista2:
#         lista3.append(i)
# print(lista3)        

# Escreva um programa que recebe uma lista de números e retorna a soma dos elementos em posições ímpares.
   