from Crypto.Cipher import AES
from Crypto.Util import Counter

# rodar em python 2
# literalmente apenas python main.py no terminal

#-----------------------------------------------------------------------------------------------------
# Dados da questao

k1 = "140b41b22a29beb4061bda66b6747e14"
ct1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"

k2 = "140b41b22a29beb4061bda66b6747e14"
ct2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"

mode_q1_q2 = AES.MODE_CBC



mode_q3_q4 = AES.MODE_CTR

k3 = "36f18357be4dbd77f050515c73fcf9f2"
ct3 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"


k4 = "36f18357be4dbd77f050515c73fcf9f2"
ct4 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
#-----------------------------------------------------------------------------------------------------
# Resolve Q1

key = k1.decode('hex')
ct_aux = ct1.decode('hex')

IV = ct_aux[:16]
ct = ct_aux[16:]

aes = AES.new(key, mode_q1_q2, IV = IV)
decd = aes.decrypt(ct) 

paddingAmount = ord(decd[len(decd)-1:])
# ord pega um valor em unicode/string e retorna esse valor em inteiro
final = decd[: -paddingAmount]
# a string final seria o que foi decodificado menos o padding, o final da string

print("Q1")
print(final)


#-----------------------------------------------------------------------------------------------------
# Resolve Q2


key = k2.decode('hex')
ct_aux = ct2.decode('hex')

IV = ct_aux[:16]
ct = ct_aux[16:]

aes = AES.new(key, mode_q1_q2, IV = IV)
decd = aes.decrypt(ct) 

paddingAmount = ord(decd[len(decd)-1:])
# ord pega um valor em unicode/string e retorna esse valor em inteiro

final = decd[: -paddingAmount]
# a string final seria o que foi decodificado menos o padding, o final da string

print("Q2")
print(final)

#-----------------------------------------------------------------------------------------------------
# Resolve Q3

key = k3.decode('hex')
ct_aux = ct3.decode('hex')


ct = ct_aux[16:]
IV = ct_aux[:16]
contador =  Counter.new(16 * 8, initial_value=long(IV.encode('hex'), 16) ) 
# o param contador fica pedindo long
# ai ficou reclamando da base 10, converti pra base 16 com IV convertido dnv
# long(str, base)

aes = AES.new(key, mode_q3_q4, counter = contador)
decd = aes.decrypt(ct) 

# n aplicar padding aqui!

final = decd

print("Q3")
print(final)

#-----------------------------------------------------------------------------------------------------
# Resolve Q4

key = k4.decode('hex')
ct_aux = ct4.decode('hex')


ct = ct_aux[16:]
IV = ct_aux[:16]
contador =  Counter.new(16 * 8, initial_value=long(IV.encode('hex'), 16) ) 
# o param contador fica pedindo long
# ai ficou reclamando da base 10, converti pra base 16 com IV convertido dnv
# long(str, base)

aes = AES.new(key, mode_q3_q4, counter = contador)
decd = aes.decrypt(ct) 

# n aplicar padding aqui!

final = decd

print("Q4")
print(final)

#-----------------------------------------------------------------------------------------------------


