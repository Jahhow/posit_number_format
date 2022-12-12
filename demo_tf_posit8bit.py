if __name__ == '__main__':
    def main():
        from time import time
        import tensorflow as tf
        from tf_posit8bit import tf_posit_8bit
        from posit8bit import posit_number_func
        def posit_number_func_tensor(tensor):
            shape = tensor.shape
            tensor = tf.reshape(tensor, [-1])
            tensor = tf.map_fn(posit_number_func, tensor)
            return tf.reshape(tensor, shape)
            
        # nTestCase=100000000
        nTestCase=2000
        a=tf.random.uniform([nTestCase])
        # a=tf.random.uniform([2,2])
        # while True:
        for _ in range(10):
            start_time = time()
            b=tf_posit_8bit(a)
            end_time = time()
            duration1 = end_time - start_time

            start_time = end_time
            c=posit_number_func_tensor(a)
            end_time = time()
            duration2 = end_time - start_time

            allCorrect = tf.reduce_all(c==b).numpy()
            if not allCorrect:
                print('ERROR!!!')
                return
            # Tested on dip3: All correct. 5.3425s -> 0.0015s
            print(f'\rAll correct. {duration2:6.4f}s -> {duration1:6.4f}s', end='', flush=True)
        print()
    main()