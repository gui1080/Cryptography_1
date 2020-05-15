import urllib2
import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter
from xor import triple_str_xor
from update import update_status

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

#--------------------------------------------------------------

if __name__ == "__main__":
    
        po = PaddingOracle()
    
#--------------------------------------------------------------s

for i in range(1, 4):
    
    if i == 1:
        ct = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd"
    
    if i == 2:
        ct = "58b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0"
        
    if i == 3:
        ct = "4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    
    pad = hex(1)[2:]
    #pad = pad_aux.decode('hex')
    zero = hex(0)[2:]

    resultados_bloco = [[] for _ in range(16)]

    l = 30
    m = 32
        
    current_test = ct[l:m]
    ct_15 = ct[l:m]

    #c[15]    
    for i in range(256):
            
        # print("GUESS:")
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
                    
        #parte_1 = hex(int(pad, 16) ^ int(guess, 16))
        # print(parte_1)
        #final_guess = hex(int(parte_1, 16) ^ int(current_test, 16))
        # print(final_guess)
        
        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:4] + ct[m:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + ct[m:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[15].append(guess)
            c_15_guess = guess
            break

    #------------------------------------------------------------------------           

    l = 28
    m = 30

    pad = hex(2)[2:]

    current_test = ct[l:m]
    ct_14 = ct[l:m]

    #c0_15_p1 = hex(int(pad, 16) ^ int(c_15_guess, 16))   
    #c0_15_novo = hex(int(ct_15, 16) ^ int(c0_15_p1, 16))

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)

    #f20bdba6ff29eed7b046d1df9fb70 22200 58b1ffb4210a580f748b4ac714c001bd
    #f20bdba6ff29eed7b046d1df9fb70 021   58b1ffb4210a580f748b4ac714c001bd

    #c[14]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
        
            
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[14].append(guess)
            c_14_guess = guess
            break        
            
    #------------------------------------------------------------------------           

    l = 26
    m = 28

    pad = hex(3)[2:]

    current_test = ct[l:m]
    ct_13 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)

    #c[13]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                
        
        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[13].append(guess)
            c_13_guess = guess
            break
            
    #------------------------------------------------------------------------           

    l = 24
    m = 26

    pad = hex(4)[2:]

    current_test = ct[l:m]
    ct_12 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    
            
    #c[12]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                
        
        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[12].append(guess)
            c_12_guess = guess
            break
    
    #------------------------------------------------------------------------           

    l = 22
    m = 24

    pad = hex(5)[2:]

    current_test = ct[l:m]
    ct_11 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
            
    #c[11]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                
        
        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[11].append(guess)
            c_11_guess = guess
            break
            
    #------------------------------------------------------------------------           

    l = 20
    m = 22

    pad = hex(6)[2:]

    current_test = ct[l:m]
    ct_10 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
        
    #c[10]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                
        
        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[10].append(guess)
            c_10_guess = guess
            break
            
    #------------------------------------------------------------------------           

    l = 18
    m = 20

    pad = hex(7)[2:]

    current_test = ct[l:m]
    ct_9 = ct[l:m]


    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
            
    #c[9]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] 
            + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] 
            + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[9].append(guess)
            c_9_guess = guess
            break
                    
    #------------------------------------------------------------------------           

    l = 16
    m = 18

    pad = hex(8)[2:]

    current_test = ct[l:m]
    ct_8 = ct[l:m]


    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)

    #c[8]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] 
            + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] 
            + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[8].append(guess)
            c_8_guess = guess
            break
                
    #------------------------------------------------------------------------           

    l = 14
    m = 16

    pad = hex(9)[2:]

    current_test = ct[l:m]
    ct_7 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)


    #c[7]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] 
            + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] 
            + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[7].append(guess)
            c_7_guess = guess
            break
        
    #------------------------------------------------------------------------           

    l = 12
    m = 14

    pad = hex(10)[2:]

    current_test = ct[l:m]
    ct_6 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)


    #c[6]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] 
            + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] 
            + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[6].append(guess)
            c_6_guess = guess
            break
        
    #------------------------------------------------------------------------           

    l = 10
    m = 12

    pad = hex(11)[2:]

    current_test = ct[l:m]
    ct_5 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)

    #c[5]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] 
            + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] 
            + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[5].append(guess)
            c_5_guess = guess
            break
        
    #------------------------------------------------------------------------           

    l = 8
    m = 10

    pad = hex(12)[2:]

    current_test = ct[l:m]
    ct_4 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)
    c0_5_novo = triple_str_xor(pad, ct_5, c_5_guess)

    #c[4]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] 
            + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] + c0_9_novo[2:4] 
            + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[4].append(guess)
            c_4_guess = guess
            break
        
    #------------------------------------------------------------------------           

    l = 6
    m = 8

    pad = hex(13)[2:]

    current_test = ct[l:m]
    ct_3 = ct[l:m]


    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)
    c0_5_novo = triple_str_xor(pad, ct_5, c_5_guess)
    c0_4_novo = triple_str_xor(pad, ct_4, c_4_guess)

    #c[3]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] 
            + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] + c0_8_novo[2:4] 
            + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[3].append(guess)
            c_3_guess = guess
            break   
        
    #------------------------------------------------------------------------           

    l = 4
    m = 6

    pad = hex(14)[2:]

    current_test = ct[l:m]
    ct_2 = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)
    c0_5_novo = triple_str_xor(pad, ct_5, c_5_guess)
    c0_4_novo = triple_str_xor(pad, ct_4, c_4_guess)
    c0_3_novo = triple_str_xor(pad, ct_3, c_3_guess)
        
    #c[2]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
                
        
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[2].append(guess)
            c_2_guess = guess
            break
        
    #------------------------------------------------------------------------           

    l = 2
    m = 4

    pad = hex(15)[2:]

    current_test = ct[l:m]
    ct_1 = ct[l:m]


    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)
    c0_5_novo = triple_str_xor(pad, ct_5, c_5_guess)
    c0_4_novo = triple_str_xor(pad, ct_4, c_4_guess)
    c0_3_novo = triple_str_xor(pad, ct_3, c_3_guess)
    c0_2_novo = triple_str_xor(pad, ct_2, c_2_guess)

    #c[1]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        if len(str(final_guess)) == 3:
            ct_teste =  ct[:l] + zero + final_guess[2:3] + c0_2_novo[2:4] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  ct[:l] + final_guess[2:4] + c0_2_novo[2:4] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[1].append(guess)
            c_1_guess = guess
            break
            
    #------------------------------------------------------------------------           

    l = 0
    m = 2

    pad = hex(16)[2:]

    current_test = ct[l:m]

    c0_15_novo = triple_str_xor(pad, ct_15, c_15_guess)
    c0_14_novo = triple_str_xor(pad, ct_14, c_14_guess)
    c0_13_novo = triple_str_xor(pad, ct_13, c_13_guess)
    c0_12_novo = triple_str_xor(pad, ct_12, c_12_guess)
    c0_11_novo = triple_str_xor(pad, ct_11, c_11_guess)
    c0_10_novo = triple_str_xor(pad, ct_10, c_10_guess)
    c0_9_novo = triple_str_xor(pad, ct_9, c_9_guess)
    c0_8_novo = triple_str_xor(pad, ct_8, c_8_guess)
    c0_7_novo = triple_str_xor(pad, ct_7, c_7_guess)
    c0_6_novo = triple_str_xor(pad, ct_6, c_6_guess)
    c0_5_novo = triple_str_xor(pad, ct_5, c_5_guess)
    c0_4_novo = triple_str_xor(pad, ct_4, c_4_guess)
    c0_3_novo = triple_str_xor(pad, ct_3, c_3_guess)
    c0_2_novo = triple_str_xor(pad, ct_2, c_2_guess)
    c0_1_novo = triple_str_xor(pad, ct_1, c_1_guess)

    #c[0]    
    for i in range(256):
            
        guess = hex(i)[2:]  
        #guess = guess_aux.decode('hex')
        #print(guess)
                

        final_guess = triple_str_xor(pad, guess, current_test)
        
        update_status(pad, guess, current_test, final_guess)
            
        if len(str(final_guess)) == 3:
            ct_teste =  zero + final_guess[2:3] + c0_1_novo[2:4] + c0_2_novo[2:4] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4]  + c0_15_novo[2:4] + ct[32:]
            
        if len(str(final_guess)) == 4:         
            ct_teste =  final_guess[2:4] + c0_1_novo[2:4] + c0_2_novo[2:4] + c0_3_novo[2:4] + c0_4_novo[2:4] + c0_5_novo[2:4] + c0_6_novo[2:4] + c0_7_novo[2:4] 
            + c0_8_novo[2:4] + c0_9_novo[2:4] + c0_10_novo[2:4] + c0_11_novo[2:4] + c0_12_novo[2:4] + c0_13_novo[2:4] + c0_14_novo[2:4] + c0_15_novo[2:4] + ct[32:]
                
        print(ct_teste)
            
        print("TESTE:")
            
        if(po.query(ct_teste)):
            resultados_bloco[0].append(guess)
            c_0_guess = guess
            break
        
    print("------------------------------------------------------------")    
    print("------------------------------------------------------------")
    print(resultados_bloco)
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")

    #i = i + 1
    
    #  sdroW digaM eh
    #  he Magid Words
    #  ?he Magic Words
        
    # ct[:2] = str(logical_xor_result)

    # key = k.decode('hex')
    # ct_aux = ct.decode('hex')

    # IV = ct_aux[:16]
    # ct = ct_aux[16:]

    # aes = AES.new(key, mode, IV = IV)
    # enc = aes.decrypt(ct_aux)

