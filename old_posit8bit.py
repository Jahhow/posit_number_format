from calendar import month_name
from importlib.util import MAGIC_NUMBER


def devide_number_integer(number):
    shift_number = 0
    while number >= 10:
        number = number / 10
        shift_number = shift_number + 1
    return number, shift_number


def devide_number_float(number):
    # print(number)
    shift_number = 0
    while number < 1:
        number = number * 10
        shift_number = shift_number + 1
    return number, shift_number


def decimal_converter(number, x):  # 0.4972
    if(number >= 2**-(x+1)):
        number = number - 2**-(x+1)
        return '1', number
    else:
        return '0', number


def bin_to_float(org_number, number, m_number, count, If_have_whole_number):
    float_number = 0
    keep_bit = 0
    for bit in range(32):
        if(org_number == 2**-bit):
            keep_bit = 0
            break
        else:
            keep_bit = 1

    for bit in range(m_number+keep_bit):
        if(If_have_whole_number):
            # print("m_number {answer}".format(answer=m_number))
            float_number += float(number[bit]) * 2**(count-bit)
            # print("float_number {answer}".format(answer=float_number))
        else:
            # print("m_number {answer}".format(answer=m_number))
            float_number += float(number[bit]) * 2**-(count+bit)
            # print("float_number {answer}".format(answer=float_number))
    return float_number


def pola_posit_number_func(float_number, places=32):
    float_abs = abs(float_number)
    posit_bit = 8
    ebit = 1
    used = 2 ** ebit
    if(float_abs < 2**(-used*4)):
        return 0
    if(float_abs > 2**(used*4)):
        return 2**(used*4)
    sign = 0
    If_have_whole_number = 0
    res_float = ''
    # print("res_float {answer}".format(answer=res_float))
    # 整數 ， 小數 = 進來的數字切開(1.123456789)
    # 1   ,  123456798
    whole_number, dec_number = str('{:.10f}'.format(float_number)).split('.')
    # 把str -> int
    whole_number = int(whole_number)
    # print("whole_number {answer}".format(answer=whole_number))
    # 把0補上去
    dec_number = float(str('0.') + str(dec_number))
    # print("dec_number {answer}".format(answer=dec_number))
    # 看原本是不是負數或是正數，如果是正數 sign = 0
    if(float_number < 0):
        sign = 1
        res = bin(whole_number).lstrip("-0b")
    else:
        sign = 0
        res = bin(whole_number).lstrip("0b")
    # res=whole 2's
    # print("res {answer}".format(answer=res))

    '''float_abs = abs(float_number)
    posit_bit = 16
    ebit = 1
    used = 2 ** ebit'''
    # print("float_abs {answer}".format(answer=float_abs))
    #float_abs = float_abs * (2**2)
    # print("float_abs {answer}".format(answer=float_abs))
    if(float_abs < 2**(used) and float_abs > 2 ** (-used)):
        m_number = posit_bit - ebit - 3
    elif((float_abs < 2**(used*2) and float_abs >= 2**(used)) or (float_abs <= 2**(-used) and float_abs > 2**(-used*2))):
        m_number = posit_bit - ebit - 4
    else:
        m_number = posit_bit - ebit - 5
    #m_number = 3
    # print(type(m_number))
    # 如果是0.123456789 = ''
    if(res == ''):
        res = ""
        If_have_whole_number = 0
    else:
        #count = 2**次方
        #org_res = 1010101
        #res = 1.010101
        org_res = res
        res, count = devide_number_integer(number=int(res))
        #print("res {answer}".format(answer=res))
        #print("count {answer}".format(answer=count))
        If_have_whole_number = 1
    for x in range(places):
        # 浮點數轉換
        whole_number, dec_number = (decimal_converter(dec_number, x))
        res_float += whole_number

    if(If_have_whole_number == 1):
        if(sign == 0):
            res_bit = str(org_res) + str(res_float) + \
                "0000000000000000000000000000000"
            scientific_answer = bin_to_float(
                org_number=float_number, number=res_bit, m_number=m_number, count=count, If_have_whole_number=If_have_whole_number)
        else:
            res_bit = str(org_res) + str(res_float) + \
                "0000000000000000000000000000000"
            scientific_answer = -1 * bin_to_float(org_number=float_number, number=res_bit,
                                                  m_number=m_number, count=count, If_have_whole_number=If_have_whole_number)
    else:
        res_float = "0." + res_float
        res_float, count_float = devide_number_float(number=float(res_float))
        if(sign == 0):
            res_int, res_float = str(res_float).split('.')
            res_bit = str(res_int) + str(res_float) + \
                "0000000000000000000000000000000"
            # print(res_bit)
            scientific_answer = bin_to_float(org_number=float_number, number=res_bit,
                                             m_number=m_number, count=count_float, If_have_whole_number=If_have_whole_number)
        else:
            res_int, res_float = str(res_float).split('.')
            res_bit = str(res_int) + str(res_float) + \
                "0000000000000000000000000000000"
            scientific_answer = -1 * bin_to_float(org_number=float_number, number=res_bit,
                                                  m_number=m_number, count=count_float, If_have_whole_number=If_have_whole_number)
    return scientific_answer


def main():
    while True:
        n = float(input("Enter your floating point value : \n"))
        float_answer = pola_posit_number_func(n)
        print("there is scientific_answer float {answer}".format(answer=float_answer))


if __name__ == "__main__":
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
