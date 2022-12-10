from math import frexp
def limit_num_fraction_bits(float_abs, num_fraction_bits):
    '''
    float_abs: The absolute value of the original number
    num_fraction_bits: Number of fraction bits
    
    - Jahhow 2022.12.10
    '''
    num_fraction_bits+=1
    fr,exp = frexp(float_abs)
    fr = int(fr*2**num_fraction_bits + .5)
    return fr * 2**(exp-num_fraction_bits)

posit_bit = 8
ebit = 1 # es, number of exp bits
useed = 2**2**ebit
minFloat = useed**-4
maxFloat = useed** 4

useedP_2 = useed**-2
useedP_1 = useed**-1
useedP1  = useed** 1
useedP2  = useed** 2
def posit_number_func(float_number):
    '''
    Originally written by Pola.
    Modified by Jahhow on 2022/12/10
    '''
    
    float_abs = abs(float_number)
    if float_abs <= minFloat:
        return 0
    if float_abs >= maxFloat:
        if float_number < 0:
            return -maxFloat
        return maxFloat

    # Get the number of fraction bits
    if useedP_1 <= float_abs < useedP1:
        num_fraction_bits = posit_bit - 1 - 2 - ebit
    elif useedP_2 <= float_abs < useedP2:
        num_fraction_bits = posit_bit - 1 - 3 - ebit
    else:
        num_fraction_bits = posit_bit - 1 - 4 - ebit

    posit_float = limit_num_fraction_bits(float_abs, num_fraction_bits)

    if float_number < 0:
        posit_float = -posit_float

    return posit_float

if __name__ == '__main__':
    def main():
        # from float_posit16bit_1 import pola_posit_number_func
        while True:
            n = float(input('Enter a float num: '))
            quantized_float = posit_number_func(n)
            # pola_quantized_float = pola_posit_number_func(n)
            print(f'               ->: {quantized_float}')
            # print(f'  Old posit float: {pola_quantized_float}')
    main()
    '''if(float_abs < 2**(-used*4)):
        return 0
    if(float_abs > 2**(used*4)):
        return 2**(used*4)'''
    '''if(float_abs < 2**(-used*4)):
        return 0
    if(float_abs > 2**(used*1)):
        return 2**(used*1)'''
    # float_abs = abs(float_number)
    # posit_bit = 8
    # ebit = 1
    # used = 2 ** ebit

    # bais_origin
    '''if(float_abs < 2 ** (-used) and float_abs >= 2 ** (-used*2)):
        m_number = posit_bit - ebit - 2
    elif(float_abs < 1 and float_abs >= 2 ** (-used)):
        m_number = posit_bit - ebit - 3
    elif(float_abs < 2 ** (used) and float_abs >= 1):
        m_number = posit_bit - ebit - 4
    elif(float_abs < 2 ** (used*2) and float_abs >= 2 ** (used)):
        m_number = posit_bit - ebit - 4
    else:
        m_number = posit_bit - ebit - 4'''
    #########################
    # bais_best

    '''if(float_abs < 2 ** (-used*2) and float_abs >= 2 ** (-used*4)):
        m_number = posit_bit - ebit - 5
    elif(float_abs < 2 ** (-used*1) and float_abs >= 2 ** (-used*2)):
        m_number = posit_bit - ebit - 4
    elif(float_abs < 2 ** (-used*0) and float_abs >= 2 ** (-used*1)):
        m_number = posit_bit - ebit - 3
    elif(float_abs < 2 ** (used*1) and float_abs >= 2 ** (-used*0)):
        m_number = posit_bit - ebit - 2
    else:
        m_number = posit_bit - ebit - 5'''
    ###########################
    '''#bais_full
    if(float_abs < 2 ** (-used*3) and float_abs >= 2 ** (-used*4)):
        m_number = posit_bit - ebit - 2
    elif(float_abs < 2 ** (-used*2) and float_abs >= 2 ** (-used*3)):
        m_number = posit_bit - ebit - 3
    elif(float_abs < 2 ** (-used*1) and float_abs >= 2 ** (-used*2)):
        m_number = posit_bit - ebit - 4
    elif(float_abs < 2 ** (used*1) and float_abs >= 2 ** (-used*1)):
        m_number = posit_bit - ebit - 5
    else:
        m_number = posit_bit - ebit - 5'''
