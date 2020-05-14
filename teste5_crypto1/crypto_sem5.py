import time
from gmpy2 import divm, powmod, mpz, t_mod

# para rodar: python3 crypto_sem5.py

ini = time.time()

b = mpz(2**20)

#p1= mpz('134078079299425970995740249982058461274793658205923933')
#p2= mpz('77723561443721764030073546976801874298166903427690031')
#p3= mpz('858186486050853753882811946569946433649006084171')

#g1= mpz('11717829880366207009516117596335367088558084999998952205')
#g2= mpz('59997945906392949973658374667057217647146031292859482967')
#g3= mpz('5428279466566527115212748467589894601965568')

#h1= mpz('323947510405045044356526437872806578864909752095244')
#h2= mpz('952783479245297198197614329255807385693795855318053')
#h3= mpz('2878928001494706097394108577585732452307673444020333')

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


for i in range(1, b):
    
    #print("--------------------------------")
#    f.write("--------------------------------")

    aux1 = mpz(powmod(g1, i , p1))
    
    teste = mpz(divm(h1, aux1, p1))

    set1_esquerda[teste] = i
    
   # print("i")
    #print(i)
#    f.write(str(i))
  #  print("lado esquerdo da igualdade")
    print(teste)
#    f.write(str(teste))

for i in range(1, b):
    
    teste_2 = mpz(powmod(aux, i, p1))
    
    print(teste_2)

    if teste_2 in set1_esquerda:
        x1 = set1_esquerda[teste_2]
        x0 = i
        
        x = mpz((x0 * b) + x1)
        
        print("-------------------------------------------------------------------------------------------------------------------")
        print("X:")
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
  
        