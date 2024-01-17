# Exercícios de Fixação
# Crie um objeto conta corrente, onde existem alguns métodos:

# Sacar 
# Depositar
# Transferir

# class Conta:
#     def __init__(self, banco):
#         self.banco = banco
#         self.saldo = 500

#     def sacar(self):
#         saque = float(input("Digite o valor que deseja sacar: "))
#         if self.saldo >= saque:
#             self.saldo = self.saldo - saque
#             print(f'saque efetuado com sucesso, seu saldo é {self.saldo}')
#         else:
#             print("vc não tem esse valor amorzinho")

#     def depositar(self):
#         deposito = float(input("Digite o valor que deseja depositar: "))
#         self.saldo = self.saldo + deposito
    
#     def transferir(self):
#         transferencia = float(input("Digite o valor que deseja transferir baby: "))
#         pessoa = input("Digite pra quem deseja transferir: ")
#         if transferencia>self.saldo:
#             print(f"amore, vc nao tem saldo p trasnferir para {pessoa}")
#         else:
#             self.saldo = self.saldo -transferencia
#             print(f"transferencia realizada com sucesso para {pessoa}")

# conta_de_nathalia= Conta("picpay")
# conta_de_nathalia.transferir()
# print(conta_de_nathalia.saldo)
# conta_de_nathalia.depositar()
# print(conta_de_nathalia.saldo)

# Crie um objeto gato, onde existem alguns métodos:
# Miar
# Comer
# Dormir
# Brincar # Ronronar # pertubar o dono

# class Gato:
#     def __init__(self,cor, tamanho,idade,sexo):
#         self.cor = cor
#         self.tamanho= tamanho
#         self.idade = idade
#         self.sexo = sexo
#         self.dormir = False
#         self.comer = False
        
#     def durmir(self):
#         if self.dormir == False:
#             self.dormir = True
#             print("O gato estava acordado, agora está dormindo")
#         else:
#             print("O gato já ta dormindo baby ")

#     def miar(self):
#         if self.dormir == False: 
#             print("miauuuu ")
#         else: 
#             print("o gato está dormindo :x")

#     def comida(self):
#         if self.dormir == True:
#             print("Não pode comer pq ta mimindo ")
#         else:
#             print("o gato está comendo hehe")

#     def brincar(self):
#         if self.dormir == True:
#             print("O gato está dormindo ")
#         else:
#             print("o gato está brincanu ")

#     def roronar(self):
#             print("prrrrrre ")

#     def pertubar(self):
#         if self.dormir== True: 
#             print("pertubando o dono")
#         else:
#             print("O gato ta miminu ")

# gato_de_nathalia = Gato("Laranja", "Médio", 6, "femea")
# gato_de_nathalia.durmir()
# gato_de_nathalia.comida()


'''Crie um objeto funcionário, onde existem alguns métodos:
trabalhar
surtar
Ir embora
chorar'''

# class Funcionario:
#     def __init__(self, nome, idade, sexo):
#         self.nome = nome
#         self.idade= idade
#         self.sexo = sexo
#         self.trabalhar = True
#         self.chorar = False
#         self.irembora = False
#         self.surtar= False

#     def irEmbora(self):
#         if self.trabalhar == True: 
#             self.trabalhar = False
#             self.irembora= True
#             print("A pessoa estava trabalhando e agr foi embora ")
#         else: 
#             print("a pessoa não estava trabalhando ")

#     def Trabalhar(self):
#         if self.chorar == True or self.irembora== True or self.surtar == True:
#             self.trabalhar = False
#             print("a pessoa não consegue trabalhar assim ")
#         else:
#             print("a pessoa tá trabalhando ")
    
#     def Chorar(self):
#         if self.surtar == True and self.trabalhar == True or self.irembora == True:
#             self.chorar = True 
#             print("A pessoa surtou e tá chorando ")
#         else: 
#             print("A pessoa ainda não tá chorando, nem surtando")
    
#     def Surtar(self):
#         if self.trabalhar == True:
#             self.surtar = True
#             print("A pessoa tava trabalhando e começou a surtar")
#         elif self.irembora == True:
#             print("A pessoa surtou depois do trabalho")
#         else:
#             print("A pessoa surtou ")

# joao_funcionario = Funcionario("João", 23,"Macho")
# joao_funcionario.irEmbora()
# joao_funcionario.Trabalhar()
# joao_funcionario.Surtar()
# joao_funcionario.Chorar()

# Crie um objeto batedeira, onde existem alguns métodos:
# Ligar
# Bater
# dar problema
# Parar de bater
# Desligar


class Batedeira:
    def __init__(self, tamanho, potencia, marca):
        self.tamanho = tamanho
        self.potencia = potencia
        self.marca = marca
        self.ligar = False
        self.desligado = True
        self.problema = False
        self.bater = False 
        self.parardebater = True

    def Desligado(self):
        if self.ligar == True:
            self.ligar = False
            self.desligado = False 
            self.problema = False
            self.bater = False
            self.parardebater = True
            print("acabei de desligar ")
        else:
            self.ligar = False
            print("já esta desligado, nao dá p desligar pq ja ta desligado ")

    def Ligado(self):
        if self.desligado == True:
            self.ligar= True
            self.desligado = False
            print("bom dia, vc acabou de ligar o bendito batedeira")
        elif self.problema== True :
            self.desligado = True
            print("maquina deu problema n pode ligar ")      
        else:
            print("Já estava ligada baby")
    
    def Problema(self):
        if self.desligado == True:
            print("não tem como dar problema vei q ta desligada")
        elif self.ligar == True:
            self.ligar = False 
            self.problema = True
            print("deu problema ")

    def Bater(self):
        if self.desligado == True:
            print("não tem como bater pq tá desligadaa")
        elif self.desligado == False and self.ligar == True and self.problema ==False:
            self.bater = True
            print("A batedeira está batendo ")
    
    def Parardebater(self):
        if self.bater == True and self.ligar == True and self.desligado == False and self.problema == False: 
            self.parardebater = False
            print("Parou de bater a bagaça ")
        elif self.problema == True:
            self.parardebater = True
            print("parou de bater, deu problema")
        else:
            print("nao pode parar de bater pq n bateu ")

'''nao bate se estiver desligada 
nao liga se tiver problema 
se n ta batendo , nao dá p parar de bater 
nao consegue desligar se nao tiver ligada 
n consegue fazer nada se tiver desligada 
p dar problema tem q tá ligada 
'''

# batedeira_da_infinty = Batedeira("pequena", 34,"osterrrr")
# batedeira_da_infinty.Desligado( )
# uhuuuuuuuuuuuuuu

# Crie uma classe "Livro" com atributos como título, autor, ano de publicação e número de páginas. Adicione métodos para obter informações do livro e para definir um novo autor.

class Livro:
    def __init__(self, autor, npaginas, ano, edição):
        self.autor = autor
        self.npaginas= npaginas
        self.ano = ano
        self.edição = edição

        
