import tensorflow as tf
import numpy as np

def tf_limit_num_fraction_bits(fr,exp,num_fraction_bits):
    '''
    float_abs: The absolute value of the original number
    num_fraction_bits: Number of fraction bits
    
    - Jahhow 2022.12.10
    '''
    num_fraction_bits+=1
    # fr,exp = frexp(float_abs)
    fr = tf.floor(fr*2**num_fraction_bits + .5)
    return fr * 2**(exp-num_fraction_bits)

posit_bit = 8
ebit = float(1) # es, number of exp bits.  KEEP IT FLOAT !
useed = 2**2**ebit
minFloat = useed**-4
maxFloat = useed** 4
halfMinFloat = minFloat/2

useedP_2 = useed**-2
useedP_1 = useed**-1
useedP1  = useed** 1
useedP2  = useed** 2
@tf.function
def tf_posit_number_func(float_number,fr,exp):
    '''
    Originally written by Jahhow on 2022/12/12
    '''

    float_abs = abs(float_number)
    num_fraction_bits = tf.where((useedP_2 <= float_abs) & (float_abs < useedP2), posit_bit - 1 - 3 - ebit, posit_bit - 1 - 4 - ebit)
    num_fraction_bits = tf.where((useedP_1 <= float_abs) & (float_abs < useedP1), posit_bit - 1 - 2 - ebit, num_fraction_bits)
    posit_float = tf_limit_num_fraction_bits(fr,exp,num_fraction_bits)
    posit_float = tf.where(float_abs >= maxFloat, maxFloat, posit_float)
    posit_float = tf.where(float_abs <= minFloat, minFloat, posit_float)
    posit_float = tf.where(float_abs <= halfMinFloat, 0., posit_float)
    posit_float = tf.where(float_number < 0, -posit_float, posit_float)

    return posit_float

# @tf.function
def tf_posit(a):
    fr,exp = np.frexp(a)
    exp=exp.astype(np.float32)
    a=tf_posit_number_func(a,fr,exp)
    return a

if __name__ == '__main__':
    def verify():
        a=tf.random.uniform([7])
        b=tf_posit(a)
        from posit8bit import posit_number_func
        c=tf.map_fn(posit_number_func, a)
        print(a)
        print(b)
        print(c)
        print(tf.reduce_all(c==b))
    def main():
        from time import time
        # from float_posit16bit_1 import pola_posit_number_func
        a=tf.random.uniform([100000000])
        # a=tf.random.uniform([2,2])
        start_time=time()
        while True:
            b=tf_posit(a)
            end_time = time()
            duration = end_time - start_time
            start_time = end_time
            print(f'{duration:10.3f}')
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
