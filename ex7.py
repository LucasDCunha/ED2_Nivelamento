#A melhor estrutura para o caso seria a Fila pois ela possui a funcionalidade first in first out.
Queue = []

def addToQueue(music):
  Queue.append(music)

def playQueue():
  Queue.pop(0)

addToQueue('Musica 1')
addToQueue('Musica 2')
addToQueue('Musica 3')
print(Queue)

playQueue()
playQueue()
print(Queue)
