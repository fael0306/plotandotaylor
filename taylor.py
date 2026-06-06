import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def taylor_series_plot():
    x = sp.Symbol('x')
    entrada = input("\nDigite a função (em termos de x): ")
    try:
        f = sp.sympify(entrada)
    except sp.SympifyError:
        print("Função inválida. Use, por exemplo: sin(x), exp(x), x**2 + 1")
        return

    a = float(input("Digite o ponto de expansão: "))
    n = int(input("Digite o número máximo de termos (grau máximo exibido = n-1): "))
    if n < 2:
        print("n deve ser pelo menos 2 para mostrar ao menos um polinômio de grau 1.")
        return

    # Ajuste dinâmico da janela x
    x_min, x_max = a - 10, a + 10
    valores_x = np.linspace(x_min, x_max, 1000)

    # Função original
    try:
        func = sp.lambdify(x, f, modules=['numpy'])
        valores_y = func(valores_x)
    except Exception as e:
        print(f"Erro ao avaliar a função original: {e}")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(valores_x, valores_y, label="f(x)", linewidth=2)

    # Cálculo das séries
    y_taylor_list = []
    for k in range(2, n+1):
        serie = sp.series(f, x, a, n=k).removeO()
        func_taylor = sp.lambdify(x, serie, modules=['numpy'])
        try:
            y_vals = func_taylor(valores_x)
            y_taylor_list.append(y_vals)
            plt.plot(valores_x, y_vals, '--', label=f"Taylor grau {k-1}")
        except Exception as e:
            print(f"Erro na série de grau {k-1}: {e}")

    # Ajuste automático do eixo y com folga de 10%
    todos_y = np.concatenate([valores_y] + y_taylor_list) if y_taylor_list else valores_y
    y_min, y_max = np.nanmin(todos_y), np.nanmax(todos_y)
    if np.isfinite(y_min) and np.isfinite(y_max):
        margem = 0.1 * (y_max - y_min)
        plt.ylim(y_min - margem, y_max + margem)
    else:
        plt.ylim(-10, 10)  # fallback

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Série de Taylor de {entrada} em torno de x = {a}')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    taylor_series_plot()
