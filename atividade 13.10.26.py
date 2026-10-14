

class Aluno:
    pass  #num faz nada ele mermo

aluno1 = Aluno()
aluno2 = Aluno()


nome = 'Carlos'
idade = 20
altura = 1.75
aprovado = True

#funçao type indentifica a variavel 
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'> ne ne

print(type(nome))
print(type(idade))
print(type(altura))
print(type(aprovado))


class Produto:
   pass


feijao = Produto()
batata = Produto()


print(type(batata))
print(type(feijao))


#https://olivers.tools/?play&net=on&room=9d7sdruq&start=fresh


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


carro1 = Carro('Toyota', 'Corolla')
carro2 = Carro('Honda', 'Civic')    


print(type(carro1))
print(type(carro2))
print(carro1.modelo)
print(carro1.marca)


def cuscuz():
  print('CUSCUZZZZ')

cuscuz()


def apresentar(nome, idade):
   print('Nome:', nome)
   print('Idade:', idade)

   apresentar('Maria', 20)
   apresentar('Carlos', 25)


   #construtor init


class Aluno:
    def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade

    def apresentar(self):
       print('Ola meu nome e', self.nome)
       print('Minha idade e', self.idade)


       aluno1 = Aluno('Ana', 19)



aluno1 = Aluno('Ana', 19)
aluno2 = Aluno ('Carlos', 22)

aluno1.apresentar()         






class Conta:
   def __init__(self, titular, saldo):
      self.titular = titular
      self.saldo = saldo

   def depositar(self, valor):
      self.saldo += valor


conta1 = Conta('Maria', 100)


conta1.depositar(50)

print('seu saldo é', conta1.saldo)
      



      
