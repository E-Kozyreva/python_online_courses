# Дана последовательность чисел длиной N (N > 1). Найти максимальное число в последовательности и второе по величине число 
# (такое, которое будет максимальным, если вычеркнуть из последовательности одно максимальное число).

def findmax2(seq):
  max1 = max(seq[0], seq[1])
  max2 = min(seq[0],seq[1])
  
  for i in range(len(seq)):
    if seq[i] > max1:
      max2 = max1
      max1 = seq[i]
    elif seq[i] > max2:
      max2 = seq[i]
      
  return (max1, max2)
