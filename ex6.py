List = [
  'item 1',
  'item 2',
  'item 3',
  'item 4',
  'item 5',
  'item 6',  
]
def getMiddle():
  if(int(len(List) % 2) != 0):
    print(List[int(len(List) / 2)])
  else:
    print(List[int(len(List) / 2) - 1])

getMiddle()
List.append('item 7')
getMiddle()