# Questão 4
caboDesejado = 34

cabos = [4, 7, 15, 20, 5, 9, 12, 17, 13, 2]
resultados = []


for x in cabos:
    for y in cabos:
        if (x != y):
            resultados.append({'cabo1': x, 'cabo2': y, 'total': x+y})

resultados.sort(key=lambda x: x['total'])
for x in resultados:
    if(x['total'] >= caboDesejado):
        print(x)
        break

    
