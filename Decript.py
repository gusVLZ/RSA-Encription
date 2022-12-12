p = 11
q = 13
n = p*q

pkey = 103

enc = [78, 118, 44, 45, 4, 59, 80, 98, 100, 62, 98, 35, 62, 80, 39, 80]
def decript(a):
  print(a)
  return str(chr((a**pkey)%n))

    
dec = list(map(decript, enc))
str = ""
print(str.join(dec) )