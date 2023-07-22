import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def taylor_series_plot():
    x = sp.Symbol('x')
    entrada = input("\nDigite a função: ")
    f = sp.sympify(entrada)
    a = int(input("Digite o ponto: "))
    n = int(input("Digite até qual quantidade de termos você deseja no gráfico: "))

    valores_x = np.linspace(-10, 10, 1000)

    func = sp.lambdify(x, f, modules=['numpy'])
    valores_y = func(valores_x)

    plt.figure(figsize=(10, 6))

    sns.lineplot(x=valores_x, y=valores_y, label="f(x)")

    for k in range(2, n+1):
        serie = sp.series(f, x, a, n=k).removeO()
        func_serie_taylor = sp.lambdify(x, serie, modules=['numpy'])
        valores_y_taylor = func_serie_taylor(valores_x)
        sns.lineplot(x=valores_x, y=valores_y_taylor, label=f"Série de Taylor de grau {k-1} de f(x)")

    plt.ylim(-10, 10)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Série de Taylor')
    plt.show()

taylor_series_plot()