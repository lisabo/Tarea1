import random

print "Cuantos numeros aleatorios desea?"

try:
   N = int(raw_input())
except ValueError:
   print "No es un numero!"
   exit()

numeros = random.sample(range(101), N)

linea = ""

archivo = open('final.py', 'a')

for n in numeros:
    linea += ",%s" % (n)
    if n % 10 == 0 and n != 0:
        archivo.write(linea[1:])
        archivo.write('\n')
        linea = ""
