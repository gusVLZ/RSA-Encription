p = 11
q = 13
n = p*q

pub = 7

def encript(a):
  a = (ord(a))
  print(a)
  return (a**pub)%n

message = "Nicolas de Jesus"
enc = list(map(encript, list(message)))

print(enc)
