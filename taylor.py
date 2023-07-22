import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = sp.Symbol('x')
entrada = input("\nDigite a função: ")
f = sp.sympify(entrada)
a = int(input("Digite o ponto: "))
n = int(input("Digite até qual quantidade de termos você deseja no gráfico: "))

for k in range(2,n+1):
    serie = sp.series(f, x, a, k, "+").removeO()
    func_serie_taylor = sp.lambdify(x, serie, modules=['numpy'])
    valores_x = np.linspace(-10, 10, 1000)
    valores_y_taylor = func_serie_taylor(valores_x)
    sns.lineplot(x=valores_x, y=valores_y_taylor, label="Série de Taylor de grau "+str(k-1)+" de f(x)")

func = sp.lambdify(x, f, modules=['numpy'])
valores_x = np.linspace(-10, 10, 1000)
valores_y = func(valores_x)
sns.lineplot(x=valores_x, y=valores_y, label="f(x)")

print("")
plt.ylim(-100,100)
plt.show()