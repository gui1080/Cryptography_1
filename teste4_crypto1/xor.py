def triple_str_xor(pad, original_c,  guess_c):

    c0_p1 = 0 # var auxiliar apenas para acumular o XOR
    c0_p1 = hex(int(pad, 16) ^ int(guess_c, 16))   
    c0_novo = hex(int(original_c, 16) ^ int(c0_p1, 16))

    return c0_novo