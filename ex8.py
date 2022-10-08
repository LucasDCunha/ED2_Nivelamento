caixa = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
caixaArrumada = []

while len(caixa) != 0:
    caixaArrumada.append(min(caixa))
    caixa.remove(min(caixa))
    print(caixaArrumada)
    