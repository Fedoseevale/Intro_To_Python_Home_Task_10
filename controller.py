import matplotlib.pyplot as plt
import view

def input_coef():
    coef_a_b = view.input_coefficients()
    coef_a = coef_a_b[0]
    coef_b = coef_a_b[1]
    return coef_a, coef_b

def draw_graph(coef_a, coef_b):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    x_values = list(range(0, 1001))
    y_values = [(coef_a*x + coef_b) for x in x_values]
    ax.scatter(x_values, y_values, c='red', s=10)
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.axis([0, 201, 0, 1001])
    plt.show()

def start():
    print('Имеется функция: у = ах + b. Предлагается построить график '
          'данной функции. Введите коэффициенты a и b.')
    coef_a, coef_b = input_coef()
    draw_graph(coef_a, coef_b)