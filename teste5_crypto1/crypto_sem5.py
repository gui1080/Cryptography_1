import time
from gmpy2 import divm, powmod, mpz, t_mod

# para rodar: python3 crypto_sem5.py

# queremos achar h = (g ^ x) em modulo p
# (h/(g ^ x1)) = ((g ^b) ^ x0) satisfaz a equacao acima (onde x = x0 * b + x1 pois x < b*b)
# iteramos entre todos os x0 e x1 possiveis ate achar o que bate

ini = time.time()

# b = 2 ^ 20

b = mpz(2**20)

p1= mpz('134078079299425970995740249982058461274793658205\
923933777235614437217640300735469768018742981669034276\
90031858186486050853753882811946569946433649006084171')
g1= mpz('117178298803662070095161175963353670885580849999\
989522055999794590639294997365837466705721764714603129\
28594829675428279466566527115212748467589894601965568')
h1= mpz('323947510405045044356526437872806578864909752095\
244952783479245297198197614329255807385693795855318053\
2878928001494706097394108577585732452307673444020333')

set1_esquerda = {}

aux = mpz(powmod(g1, b, p1))

print("lado esquerdo da eq")
print("------------------------------------------------------------------------")
# criando o dicionario de possibilidades para o lado esquerdo da equacao
for i in range(1, b):
    
    # (g ^ x1)
    aux1 = mpz(powmod(g1, i , p1))
    
    # (h/(g ^ x1)) (taca no dicionario logo depois)
    teste = mpz(divm(h1, aux1, p1))

    set1_esquerda[teste] = i
    print(teste)

print("lado direito da eq")
print("------------------------------------------------------------------------")
# fazendo tentativas para ver se o lado direito e o esquerdo eventualmente batem
for i in range(1, b):
    
    # (g^b)^i para i entre 0 e 2^20
    teste_2 = mpz(powmod(aux, i, p1))
    
    print(teste_2)

    if teste_2 in set1_esquerda:
        # achamos x0 e x1 que satisfazem:
        # (h/g ^ x1) = ((g ^ b) ^ x0)
        
        x1 = set1_esquerda[teste_2]
        x0 = i
        
        # derivamos disso que (x0 ^ b + x1) = X
        # onde h = (g ^ x)
        
        x = mpz((x0 * b) + x1)
        
        print("-------------------------------------------------------------------------------------------------------------------")
        print("Resultado final X:")
        print(x)
        print("-------------------------------------------------------------------------------------------------------------------")
        break
     
#for i in range(1, b):

 #   teste_2 = mpz(powmod(aux, i, p1))


  #  if teste_2 in set1_esquerda:
   #     x1 = set1_esquerda[teste_2]
    #    x0 = i
        
     #   x = (x0 * b) + x1
      #  print("X:")
       # print(x)
       # break

#f.close() 
    
fim = time.time()
print ("Tempo de execucao:")
print (fim-ini)
  
        