from time import time
from builtins import str
import random

class AlgoritmosDeBusqueda:
    
    def mostrarVector(self, datos):
        cont=1
        for i in range(0, len(datos)):
            if(int(cont)==15):
                print("  "+str(datos[i])+",    ")
                cont=1
            else:
                print("  "+str(datos[i])+",    ", end="")
                cont+=1
    
    def mostrarDatosDeEficiencia(self, contadorComparaciones, contadorRecorridos, tiempoTotal):
        print("       DATOS DE EFICIENCIA DEL ALGORITMO")
        print()
        print("    - Cantidad  de  recorridos  realizados:    "+str(contadorRecorridos))
        print("    - Cantidad de comparaciones realizadas:    "+str(contadorComparaciones))
        #print("    - Cantidad  de intercambios realizados:    "+str(contadorIntercambios))
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal)+" segundos")
        print("    - Tiempo     total     de    ejecucion:    "+str(tiempoTotal*1000)+" milisegundos")
    
    '''=======METODO DE BUSQUEDA SECUENCIAL======='''
    def busquedaSecuencial(self, datos, datoBuscar):
        contadorComparaciones=0
        contadorRecorridos=0
                
        pos=0
        encontrado=False
        
        contadorRecorridos+=1
        inicio=time()
        while(pos<len(datos) and not encontrado):
            contadorComparaciones+=1
            if(datos[pos]==datoBuscar):
                encontrado=True
            else:
                pos+=1
        tiempoTotal=time()-inicio
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorRecorridos, tiempoTotal)
        return encontrado
    
    
    

algoritmos=AlgoritmosDeBusqueda()
repetirMenuPrincipal=True
opcion=0
datos=[]

while(repetirMenuPrincipal):
    print("1 = Algoritmo de busqueda Secuencial.")
    print("2 = (Sin funcion... Por Ahora)")
    print("3 = (Sin funcion... Por Ahora)")
    print("4 = Llenar vector a utilizar.")
    print("5 = Salir")
    print("-----------------------------------------")
    opcion=int(input('Elija una opcion...'))
    print()
    print()
    
    if(opcion>=1 and opcion <=5):
        if(opcion==1):
            if(len(datos)>0):
                print("  ======================================================VECTOR ORIGINAL======================================================\n");
                algoritmos.mostrarVector(datos);
                print("\n\n");
                print("  =================================================BUSQUEDA SECUENCIAL================================================\n");
                if(algoritmos.busquedaSecuencial(datos.copy(), int(input('Ingrese el numero a buscar...')))):
                    print()
                    print()
                    print("   El numero si existe");
                else:
                    print()
                    print()
                    print("   *El numero no existe")
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==2):
            if(len(datos)>0):
                print()
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==3):
            if(len(datos)>0):
                print()
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==4):
            datos=[]
            print("  Creando vector...")
            for i in range(0,100):
                datos.insert(i, random.randint(1,100))
            print()
            print("  El vector ha sido creado y llenado.")
            print()
            print("  *NOTA: El vector a utilizar en los metodos sera el mismo mientras que no se escoja un tamanio diferente.")
            print()
            print()
        if(opcion==5):
            repetirMenuPrincipal=False
    else:
        print("  *"+str(opcion)+" no es una opcion valida, intenta otra vez.")
        print()
        print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print()
print("Usted ha salido.")