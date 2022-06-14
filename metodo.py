from tabulate import tabulate
import pandas as pd
from colorama import Fore, init, Back
from clearscreen import clearscreen
import numpy as np
import matplotlib.pyplot as plt
import math
init(autoreset=True) 

class Metodo:

    def __init__(self):
        self.x = []
        self.fx = []
        self.fn = []
        self.cant = 0
        self.matA = []
        self.matB = []
        self.matX = []
        self.valoresx = []
        self.valoresy = []
        self.intervalo = 0.01

    def carga_val(self):
        clearscreen()
        print("\nA continuación se le solicitará ingresar los valores de x y f(x). ")
        print("\nPara finalizar la carga cuando se desee, presionar enter cuando se solicite el valor de x, sin ingresar ningún valor")
        while True:
            self.cant += 1
            lectura = input(Fore.LIGHTYELLOW_EX + "\nIngrese x%d: " % self.cant)
            if lectura == '':
                print("Lectura vacia")
                self.cant -= 1
                break
            while self.validate_input(lectura):
                lectura = input(Fore.LIGHTYELLOW_EX + "\nIngrese x%d: " % self.cant)
            self.x.append(float(lectura))
            lectura = input(Fore.LIGHTYELLOW_EX + "\nIngrese el valor de f(x)%d: " % self.cant)
            while self.validate_input(lectura):
                lectura = input(Fore.LIGHTYELLOW_EX + "\nIngrese el valor de f(x)%d: " % self.cant)
            self.fx.append(float(lectura))
            clearscreen()
        clearscreen()

    def validate_input(self, inp):
        try:
            float(inp)
            return False
        except ValueError:
            print((Fore.RED + 'Por favor, solo ingrese números, intente nuevamente' + Fore.GREEN))
            return True

    def show_values(self):
        print(Fore.BLUE + "\nTabla de valores ingresados\n" + Fore.GREEN)
        myData={"x": self.x, "f(x)": self.fx}
        myDataFrame=pd.DataFrame(myData)
        print(Fore.GREEN + tabulate(myDataFrame, headers='keys', tablefmt='psql', stralign='center'))

    def print_info(self):
        clearscreen()
        print(Fore.GREEN + "\tProyecto Informático Análisis Numérico 2022")
        print(Fore.BLUE + "\nAutor:" + Fore.CYAN + "\tRicciardi, Marcos")
        print(Fore.BLUE + "\nTema:\t" + Fore.CYAN + "Aproximación discreta por mínimos cuadrados")
        input(Fore.YELLOW + "\n\n\t\tPresione enter para continuar" + Fore.BLUE)
        clearscreen()

    def show_cloud(self):
        plt.figure(figsize=(10,7))
        plt.plot(self.x,self.fx,'o',color='orange',markersize=10)
        plt.show()
        plt.close()

    def calc_poli(self):
        #Voy a tener un polinomio de un grado menor a la cantidad de puntos
        #Tabla de valores para cada funcion
        for exp in range(self.cant):
            faux = []
            for i in range(self.cant):
                faux.append(float(math.pow(self.x[i], exp)))
            self.fn.append(faux)

        #Matriz A
        for i in range(self.cant):
            faux = []
            for j in range(self.cant):
                aux = 0
                for k in range(self.cant):
                    aux = aux + self.fn[i][k]*self.fn[j][k]
                faux.append(aux)
            self.matA.append(faux)

        #Matriz B
        for i in range(self.cant):
            aux = 0
            for j in range(self.cant):
                aux = aux + self.fx[j]*self.fn[i][j]
            self.matB.append(aux)

        A = np.array(self.matA)
        B = np.array(self.matB)
        #Vector de soluciones
        self.matX = np.linalg.solve(A, B)


    def show_func(self):
        xmin = min(self.x)
        xmax = max(self.x)
        while xmin <= xmax:
            aux = 0
            for i in range(self.cant):
                aux = aux + (math.pow(xmin, i) * self.matX[i])
            self.valoresx.append(xmin)
            self.valoresy.append(aux)
            xmin += self.intervalo
        plt.figure(figsize=(10,7))
        plt.plot(self.valoresx, self.valoresy,color='orange',markersize=5)
        plt.show()
        plt.close()

    def show_both(self):
        xmin = min(self.x)
        xmax = max(self.x)
        while xmin <= xmax:
            aux = 0
            for i in range(self.cant):
                aux = aux + (math.pow(xmin, i) * self.matX[i])
            self.valoresx.append(xmin)
            self.valoresy.append(aux)
            xmin += self.intervalo
        plt.figure(figsize=(10,7))
        plt.plot(self.x,self.fx,'o',color='blue',markersize=7)
        plt.plot(self.valoresx, self.valoresy,color='orange',markersize=5)
        plt.show()
        plt.close()

    def show_matrix(self):
        print("\n")
        for i in range(self.cant):
            print(Fore.CYAN + "f(x)%d:" % i , end = Fore.YELLOW + '\t|' )
            for j in range(self.cant):
                print(Fore.YELLOW + "%f|" % self.fn[i][j], end='')
            print("\n")

        print(Fore.CYAN + "\n\nMatriz A:\n")

        for i in range(self.cant):
            print("", end = Fore.LIGHTCYAN_EX + '\t|' )
            for j in range(self.cant):
                print(Fore.LIGHTCYAN_EX + "%f|" % self.matA[i][j], end='')
            print("\n")

        print(Fore.MAGENTA + "\n\nMatriz B:\n")

        for i in range(self.cant):
            print(Fore.LIGHTMAGENTA_EX + "\t|%f|" % self.matB[i])

        print(Fore.GREEN + "\n\nMatriz X:\n")        
        for i in range(self.cant):
            print(Fore.LIGHTGREEN_EX + "\tx%d: |%f|" % (i, self.matX[i]))

        print(Fore.BLUE + "\nFUNCION QUE APROXIMA AL CONJUNTO DE PUNTOS INGRESADOS: \n")
        print(Fore.LIGHTRED_EX + "\t\tf(x) = ", end='')
        for i in range(self.cant):
            if abs(self.matX[i]) > 0.000001:
                if i>0:
                    print(Fore.YELLOW + "%+f*x^%d" % (self.matX[i], i), end='')
                else:
                    print(Fore.YELLOW + "%+f" % self.matX[i], end='')
        print("\n")