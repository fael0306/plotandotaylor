import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def taylor(f, a, n):
    x = sp.Symbol('x')
    serie = sp.series(f, x, a, n, "+").removeO()
    func = sp.lambdify(x, f, modules=['numpy'])
    func_serie_taylor = sp.lambdify(x, serie, modules=['numpy'])

    valores_x = np.linspace(-10, 10, 1000)
    valores_y = func(valores_x)
    valores_y_taylor = func_serie_taylor(valores_x)

    sns.lineplot(x=valores_x, y=valores_y_taylor, label="Série de Taylor de f(x)")
    sns.lineplot(x=valores_x, y=valores_y, label="f(x)")
    plt.ylim(-10,10)
    plt.show()

    return serie

def aproximacao_taylor():
    entrada = input("\nDigite a função: ")
    f = sp.sympify(entrada)
    a = int(input("Digite o ponto: "))
    n = int(input("Digite a quantidade de termos que deseja na série: "))
    print("\nA função aproximada é:", taylor(f, a, n))
    print("")

if __name__ == "__main__":
    aproximacao_taylor()
