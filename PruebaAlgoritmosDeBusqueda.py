from time import time
from builtins import str, sorted
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
            if(encontrado==True):
                tiempoTotal=time()-inicio
                print()
                print()
                self.mostrarDatosDeEficiencia(contadorComparaciones, contadorRecorridos, tiempoTotal)
                return pos
        tiempoTotal=time()-inicio
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorRecorridos, tiempoTotal)
        return -1

    def busquedaBianria(self, datos, elemento):
        contadorComparaciones=0
        contadorRecorridos=0
        
        primero=0
        ultimo=len(datos)
        
        contadorRecorridos+=1
        inicio=time()
        while(primero<=ultimo):
            contadorComparaciones+=1
            centro=int((primero+ultimo)/2)
            valorCentro=datos[centro]
            print("Comparando "+str(elemento)+" con "+str(datos[centro]))
            
            if(elemento==valorCentro):
                tiempoTotal=time()-inicio
                print()
                print()
                self.mostrarDatosDeEficiencia(contadorComparaciones, contadorRecorridos, tiempoTotal)
                return centro
            elif(elemento<valorCentro):
                ultimo=centro-1
            else:
                ultimo=centro+1
        tiempoTotal=time()-inicio
        print()
        print()
        self.mostrarDatosDeEficiencia(contadorComparaciones, contadorRecorridos, tiempoTotal)
        return -1
        
class Hash_table:
    def __init__(self):
        self.table=[None]*127
    
    def mostrarVector(self, datos):
        cont=1
        for i in range(0, len(datos)):
            if(int(cont)==15):
                print("  "+str(datos[i])+",    ")
                cont=1
            else:
                print("  "+str(datos[i])+",    ", end="")
                cont+=1
    
    def Hash_fun(self, value):
        key=0
        for i in range(0,len(value)):
            key+=ord(value[i])
        return key%127
    
    def Insert(self, value):
        hash=self.Hash_fun(value)
        if(self.table[hash]is None):
            self.table[hash]=value
            
    def Search(self, value):
        hash=self.Hash_fun(value)
        if(self.table[hash] is None):
            return None
        else:
            return id(self.table[hash])

algoritmos=AlgoritmosDeBusqueda()
repetirMenuPrincipal=True
opcion=0
datos=[]

while(repetirMenuPrincipal):
    print("1 = Algoritmo de busqueda Secuencial.")
    print("2 = Algoritmo de busqueda Binaria.")
    print("3 = Algoritmo de busqueda por Funciones Hash.")
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
                valor=algoritmos.busquedaSecuencial(datos.copy(), int(input('Ingrese el numero a buscar...')))
                if(valor!=-1):
                    print()
                    print()
                    print("   El numero se encuntra en la posicion "+str(valor+1));
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
                copiaDatos=sorted(datos.copy())
                print("  ======================================================VECTOR ORIGINAL======================================================\n");
                algoritmos.mostrarVector(copiaDatos);
                print("\n\n");
                print("  =================================================BUSQUEDA BINARIA================================================\n");
                valor=algoritmos.busquedaBianria(copiaDatos, int(input("Ingrese el numero a buscar...")))
                if(valor!=-1):
                    print()
                    print()
                    print("   El numero se encuntra en la posicion "+str(valor+1));
                else:
                    print()
                    print()
                    print("   *El numero no existe")
            else:
                print("  *No se ha elegido un tamanio para el vector.")
            print()
            print()
        if(opcion==3):
            if(len(datos)>0):
                h=Hash_table()
                ''''h.Insert("Alo")
                h.Insert("Bou")
                h.Insert("Col")
                h.Insert("arroz")
                h.Insert("animal")
                '''
                
                
                for i in range(0,len(datos)):
                    h.Insert(str(datos[i]))
                        
                print("  ======================================================DATOS======================================================\n");
                h.mostrarVector(datos)
                print("\n\n");
                respuesta=h.Search(input("Ingrese el dato a buscar..."))
                print("\n");
                
                if(respuesta!=None):
                    print("  Se encontro el elemento en la direccion de memoria: "+str(respuesta))
                else:
                    print("  *No se encontro el elemento buscado")
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