if __name__ == '__main__':
    def main():
        from posit8bit import posit_number_func
        from old_posit8bit import pola_posit_number_func
        while True:
            n = float(input('輸入數字(小數可): '))
            quantized_float = posit_number_func(n)
            pola_quantized_float = pola_posit_number_func(n)
            print(f'  新 Posit 結果 ->: {quantized_float}')
            print(f'              誤差: {abs(n-quantized_float)}')
            print(f'  舊 Posit 結果 ->: {pola_quantized_float}')
            print(f'              誤差: {abs(n-pola_quantized_float)}')
            print()
    main()