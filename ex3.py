# Sim, é possível. 
# Para inverter uma String utilizando pilha, inicialmente cada caracter da String seria inserido na pilha através da função push() a partir da posição 0 da String.
# Após todos os caracteres serem inseridos, uma nova String receberia um a um os caracteres armazenados na pilha através da utilização da função pop().
# Dessa forma, teríamos a palavra original invertida.

string = 'teste'
stringFinal = []
pilha = []
i = 0

while i < len(string):
    pilha.append(string[i])
    i += 1

for j in string:
    stringFinal += pilha.pop()

print(stringFinal)