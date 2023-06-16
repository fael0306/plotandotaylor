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
