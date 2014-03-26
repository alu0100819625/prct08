#!/usr/bin/python
import modulo
def error(intervalo,test, umbral):
  errores=0.0
  for i in range(test):
   apr1=modulo.aprox(intervalo)
   apr2=modulo.aprox(test)
   resultado=(apr1-apr2)
   if (abs(resultado)>= umbral):
     errores+=1
  return (errores/test)* 100 
  
if __name__=="__main__":
  import sys   
  if((len(sys.argv)==1) or (len(sys.argv)==2) or (len(sys.argv)==3)):
      print ("No se han introducido los parametros necesarios, se utilizaran los valores por defecto")
      intervalo=10
      test=10
      umbral=0,00000001
  else:
      intervalo =int(sys.argv[1])
      test =int(sys.argv[2])
      umbral=float(sys.argv[3])
  print error(intervalo,test,umbral)
  
  
