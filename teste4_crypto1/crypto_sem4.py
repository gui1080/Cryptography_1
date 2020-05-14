import urllib2
import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter


TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print ("We got: %d" % e.code)       # Print response code
            if e.code == 404:
                print("GOOD PADDING")
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    
        po = PaddingOracle()
    
ct = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd"

#first_test = ct[126:128]
#first_test = hex(first_test_aux)[2:]
#print(first_test)
#print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

pad = hex(1)[2:]
#pad = pad_aux.decode('hex')
zero = hex(0)[2:]

resultados_bloco1 = [[] for _ in range(16)]

l = 30
m = 32
    
current_test = ct[l:m]
ct_15 = ct[l:m]

#c0[15]    
for i in range(256):
        
    # print("GUESS:")
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
                
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    # print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    # print(parte_2)
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
    
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:4] + ct[m:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + ct[m:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[15].append(guess)
        c0_15_aux = guess
        break

print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
     

#------------------------------------------------------------------------           

l = 28
m = 30

pad = hex(2)[2:]

current_test = ct[l:m]
ct_14 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))


#f20bdba6ff29eed7b046d1df9fb70 22200 58b1ffb4210a580f748b4ac714c001bd
#f20bdba6ff29eed7b046d1df9fb70 021   58b1ffb4210a580f748b4ac714c001bd

#c0[14]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[14].append(guess)
        c0_14_aux = guess
        break        

print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
     
        
#------------------------------------------------------------------------           

l = 26
m = 28

pad = hex(3)[2:]

current_test = ct[l:m]
ct_13 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))

#c0[13]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[13].append(guess)
        c0_13_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
     

        
#------------------------------------------------------------------------           

l = 24
m = 26

pad = hex(4)[2:]

current_test = ct[l:m]
ct_12 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
   
        
#c0[12]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[12].append(guess)
        c0_12_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
     
  
#------------------------------------------------------------------------           

l = 22
m = 24

pad = hex(5)[2:]

current_test = ct[l:m]
ct_11 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
        
#c0[11]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[11].append(guess)
        c0_11_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
      
        
#------------------------------------------------------------------------           

l = 20
m = 22

pad = hex(6)[2:]

current_test = ct[l:m]
ct_10 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
       
c0_11_p1 = hex(int(pad, 16) ^ int(c0_11_aux, 16))   
c0_11_novo = hex(int(ct_11, 16) ^ int(c0_11_p1, 16))   
        
#c0[10]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[10].append(guess)
        c0_10_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
      
        
#------------------------------------------------------------------------           

l = 18
m = 20

pad = hex(7)[2:]

current_test = ct[l:m]
ct_9 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
       
c0_11_p1 = hex(int(pad, 16) ^ int(c0_11_aux, 16))   
c0_11_novo = hex(int(ct_11, 16) ^ int(c0_11_p1, 16))   

c0_10_p1 = hex(int(pad, 16) ^ int(c0_10_aux, 16))   
c0_10_novo = hex(int(ct_10, 16) ^ int(c0_10_p1, 16))   
        
#c0[9]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[9].append(guess)
        c0_9_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
      
        
#------------------------------------------------------------------------           

l = 16
m = 18

pad = hex(8)[2:]

current_test = ct[l:m]
ct_8 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
       
c0_11_p1 = hex(int(pad, 16) ^ int(c0_11_aux, 16))   
c0_11_novo = hex(int(ct_11, 16) ^ int(c0_11_p1, 16))   

c0_10_p1 = hex(int(pad, 16) ^ int(c0_10_aux, 16))   
c0_10_novo = hex(int(ct_10, 16) ^ int(c0_10_p1, 16))   

c0_9_p1 = hex(int(pad, 16) ^ int(c0_9_aux, 16))   
c0_9_novo = hex(int(ct_9, 16) ^ int(c0_9_p1, 16))   
         
#c0[8]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[8].append(guess)
        c0_8_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
      
#------------------------------------------------------------------------           

l = 14
m = 16

pad = hex(9)[2:]

current_test = ct[l:m]
ct_7 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
       
c0_11_p1 = hex(int(pad, 16) ^ int(c0_11_aux, 16))   
c0_11_novo = hex(int(ct_11, 16) ^ int(c0_11_p1, 16))   

c0_10_p1 = hex(int(pad, 16) ^ int(c0_10_aux, 16))   
c0_10_novo = hex(int(ct_10, 16) ^ int(c0_10_p1, 16))   

c0_9_p1 = hex(int(pad, 16) ^ int(c0_9_aux, 16))   
c0_9_novo = hex(int(ct_9, 16) ^ int(c0_9_p1, 16))   

c0_8_p1 = hex(int(pad, 16) ^ int(c0_8_aux, 16))   
c0_8_novo = hex(int(ct_8, 16) ^ int(c0_8_p1, 16))   
         
#c0[7]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[7].append(guess)
        c0_7_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
       

#------------------------------------------------------------------------           

l = 12
m = 14

pad = hex(10)[2:]

current_test = ct[l:m]
ct_6 = ct[l:m]

c0_15_p1 = hex(int(pad, 16) ^ int(c0_15_aux, 16))   
c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

c0_14_p1 = hex(int(pad, 16) ^ int(c0_14_aux, 16))   
c0_14_novo = hex(int(ct_14, 16) ^ int(c0_14_p1, 16))
       
c0_13_p1 = hex(int(pad, 16) ^ int(c0_13_aux, 16))   
c0_13_novo = hex(int(ct_13, 16) ^ int(c0_13_p1, 16))
       
c0_12_p1 = hex(int(pad, 16) ^ int(c0_12_aux, 16))   
c0_12_novo = hex(int(ct_12, 16) ^ int(c0_12_p1, 16))   
       
c0_11_p1 = hex(int(pad, 16) ^ int(c0_11_aux, 16))   
c0_11_novo = hex(int(ct_11, 16) ^ int(c0_11_p1, 16))   

c0_10_p1 = hex(int(pad, 16) ^ int(c0_10_aux, 16))   
c0_10_novo = hex(int(ct_10, 16) ^ int(c0_10_p1, 16))   

c0_9_p1 = hex(int(pad, 16) ^ int(c0_9_aux, 16))   
c0_9_novo = hex(int(ct_9, 16) ^ int(c0_9_p1, 16))   

c0_8_p1 = hex(int(pad, 16) ^ int(c0_8_aux, 16))   
c0_8_novo = hex(int(ct_8, 16) ^ int(c0_8_p1, 16))   

c0_7_p1 = hex(int(pad, 16) ^ int(c0_7_aux, 16))   
c0_7_novo = hex(int(ct_7, 16) ^ int(c0_7_p1, 16))   
         
#c0[6]    
for i in range(256):
        
    guess = hex(i)[2:]  
    #guess = guess_aux.decode('hex')
    #print(guess)
             
    parte_1 = hex(int(pad, 16) ^ int(guess, 16))
    #print(parte_1)
    parte_2 = hex(int(parte_1, 16) ^ int(current_test, 16))
    #print(parte_2)
    
    
    print(pad)
    print("xor")
    print(guess)
    print("xor")
    print(current_test)
    print("equals")
    print(parte_2)
           
    
    if len(str(parte_2)) == 3:
        ct_teste =  ct[:l] + zero + parte_2[2:3] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
        
    if len(str(parte_2)) == 4:         
        ct_teste =  ct[:l] + parte_2[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
            
    print(ct_teste)
        
    print("TESTE:")
        
    if(po.query(ct_teste)):
        resultados_bloco1[6].append(guess)
        c0_6_aux = guess
        break
    
print("------------------------------------------------------------")    
print("------------------------------------------------------------")
print(resultados_bloco1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
       
       
       
        
# ct[:2] = str(logical_xor_result)

# key = k.decode('hex')
# ct_aux = ct.decode('hex')

# IV = ct_aux[:16]
# ct = ct_aux[16:]

# aes = AES.new(key, mode, IV = IV)
# enc = aes.decrypt(ct_aux)

