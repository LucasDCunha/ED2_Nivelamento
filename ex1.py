# Questão 1

sequencia = [1, 7, 2, 9]
i = 3

while i < 100:
    sequencia.append(sequencia[i - 2] + sequencia[i - 3])
    i += 1

print(sequencia)