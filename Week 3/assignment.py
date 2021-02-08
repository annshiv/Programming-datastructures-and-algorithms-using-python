def remdup(arr):
  a = arr[::-1]
  temp1 = []
  for i in a:
    if i not in temp1:
      temp1.append(i)
  return temp1[::-1]
  
def splitsum(arr):
  pos = 0
  neg = 0
  for i in arr:
    if i >= 0:
      pos += i ** 2
    else:
      neg += i ** 3
  result = [pos,neg]
  return result

def matrixflip(arr,a):
  b = arr.copy()
  if a =='h':
    for i in range(0,len(b),1):
      b[i].reverse()
  elif a =='v':
    b.reverse()
  return b
