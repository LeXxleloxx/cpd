import csv

class Country:

     def __init__(self,a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32):
       self.a1 = a1
       self.a2 = a2
       self.a3 = a3
       self.a4 = a4
       self.a5 = a5
       self.a6 = a6
       self.a7 = a7
       self.a8 = a8
       self.a9 = a9
       self.a10 = a10
       self.a11 = a11
       self.a12 = a12
       self.a13 = a13
       self.a14 = a14
       self.a15 = a15
       self.a16 = a16
       self.a17 = a17
       self.a18 = a18
       self.a19 = a19
       self.a20 = a20
       self.a21 = a21
       self.a22 = a22
       self.a23 = a23
       self.a24 = a24
       self.a25 = a25
       self.a26 = a26
       self.a27 = a27
       self.a28 = a28
       self.a29 = a29
       self.a30 = a30
       self.a31 = a31
       self.a32 = a32


# abre arquivo
# pula primeira linha
# se b = "
#    self.ax = b+1 até pos_prox(")-1
# repete até self.a32
# repete para todas as linhas


with open('new2018_data.bin', 'rb') as f:
  Countries = []
  x = f.readline()
num_lines = sum(1 for line in f)
i=1
while i <= num_lines:
  x = f.read(1)
  if x == '"':
      Country1 = pass
      x = f.read(1)
      if x != '"':
        Country.a1+= x



  print(x)

x = f.read(1)
print(x)

x = f.read(1)
print(x)
##   y = ""
##   if( x == '('):
##       y += f.read(1)
##       x = f.read(1)
##       while x != ')':
##           y += x
##           x = f.read(1)
##           print(y)
##   for i in Country:
##       i=y
##   print(Country.a1)

#    print(xx, end='')

##    for line in f:
##         print(line, end='')