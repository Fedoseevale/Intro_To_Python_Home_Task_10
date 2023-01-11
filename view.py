def input_coefficients() -> list:
    while True:
        try:
            coefficient_a = int(input('Введите значение коэффициента a - целое число: '))
            coefficient_b = int(input('Введите значение коэффициента b - целое число: '))
            coefficients = [coefficient_a, coefficient_b]
            return coefficients
        except:
            print('Ошибка')