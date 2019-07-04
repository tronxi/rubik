import numpy as np;
import time;
class Cube:
    BLANCO = 0;
    VERDE = 1;
    NARANJA = 2;
    AZUL = 3;
    ROJO = 4;
    AMARILLO = 5;
    
    colores = ['b', 'v', 'n', 'a', 'r', 'A'];
    movimientos = ['R', 'Rp', 'R2', 'L', 'Lp', 'L2', 'U', 'Up', 'U2', 'D', 'Dp', 'D2', 'F', 'Fp', 'F2', 'B', 'Bp', 'B2'];
    #movimientos = ['R', 'L', 'U', 'D', 'F', 'B'];

    def __init__(self):
        self.caras = 6;
        self.piezas = 3;
        self.cubo = np.zeros((self.caras, self.piezas, self.piezas), int);
        self.__inicializar();
        
    def __imprimirNumeros(self):
        print('IMPRIMIR');
        print(self.cubo);
        print('FIN');
        
    def imprimir(self):
        print('IMPRIMIR');
        for cara in range(self.caras):
            for x in range(self.piezas):
                for y in range(self.piezas):
                    print(' ' + self.colores[self.cubo[cara, x, y]] + ' ', end = '');
                print('\n');
            print('\n');
        print('FIN');
    
    
    def __inicializar(self):
        for cara in range(self.caras):
            for x in range(self.piezas):
                for y in range(self.piezas):
                    self.cubo[cara, x, y] = cara;
    def resuelto(self):
        for cara in range(self.caras):
            for x in range(self.piezas):
                for y in range(self.piezas):
                    if self.cubo[cara, x, y] != cara:
                        return False;
        return True;
        
    def __rotarCaraReloj(self, cara):
        cuboAux = np.copy(self.cubo);
        for x in range(self.piezas):
            cuboAux[cara, :, (self.piezas - 1)- x] = self.cubo[cara, x]
        self.cubo = np.copy(cuboAux);
        
    def __R(self):
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
            filaIn = (self.piezas - 1) - fila;
            cuboAux[self.AZUL, fila, 0] = self.cubo[self.BLANCO, filaIn, self.piezas-1]
            cuboAux[self.AMARILLO, fila, self.piezas - 1] = self.cubo[self.AZUL, filaIn, 0]
            cuboAux[self.VERDE, fila, self.piezas - 1] = self.cubo[self.AMARILLO, fila, self.piezas - 1]
            cuboAux[self.BLANCO, fila, self.piezas - 1] = self.cubo[self.VERDE, fila, self.piezas - 1]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.ROJO)
    def __Rp(self):
        self.__R();
        self.__R();
        self.__R();
        
    def __L(self):
        cuboAux = np.copy(self.cubo); 
        for fila in range(self.piezas):
            filaIn = (self.piezas - 1) - fila;
            cuboAux[self.VERDE, fila, 0] = self.cubo[self.BLANCO, fila, 0];
            cuboAux[self.AMARILLO, fila, 0] = self.cubo[self.VERDE, fila, 0];
            cuboAux[self.BLANCO, fila, 0] = self.cubo[self.AZUL, filaIn, self.piezas - 1];
            cuboAux[self.AZUL, fila, self.piezas - 1] = self.cubo[self.AMARILLO, filaIn, 0];
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.NARANJA)
    def __Lp(self):
        self.__L();
        self.__L();
        self.__L();
        
    def __U(self):
        cuboAux = np.copy(self.cubo);
        for columna in range(self.piezas):
            cuboAux[self.VERDE, 0, columna] = self.cubo[self.ROJO, 0, columna]
            cuboAux[self.ROJO, 0, columna] = self.cubo[self.AZUL, 0, columna]
            cuboAux[self.AZUL, 0, columna] = self.cubo[self.NARANJA, 0, columna]
            cuboAux[self.NARANJA, 0, columna] = self.cubo[self.VERDE, 0, columna]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.BLANCO)
    def __Up(self):
        self.__U();
        self.__U();
        self.__U();
        
    def __D(self):
        cuboAux = np.copy(self.cubo);
        for columna in range(self.piezas):
            cuboAux[self.VERDE, self.piezas - 1, columna] = self.cubo[self.NARANJA, self.piezas - 1, columna]
            cuboAux[self.NARANJA, self.piezas - 1, columna] = self.cubo[self.AZUL, self.piezas - 1, columna]
            cuboAux[self.AZUL, self.piezas - 1, columna] = self.cubo[self.ROJO, self.piezas - 1, columna]
            cuboAux[self.ROJO, self.piezas - 1, columna] = self.cubo[self.VERDE, self.piezas - 1, columna]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.AMARILLO)
    def __Dp(self):
        self.__D();
        self.__D();
        self.__D();
        
    def __F(self):
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
            filaIn = (self.piezas - 1) - fila;
            cuboAux[self.BLANCO, self.piezas - 1, fila] = self.cubo[self.NARANJA, filaIn, self.piezas - 1]
            cuboAux[self.AMARILLO, 0, fila] = self.cubo[self.ROJO, filaIn, 0]
            cuboAux[self.NARANJA, fila, self.piezas - 1] = self.cubo[self.AMARILLO, 0, fila]
            cuboAux[self.ROJO, fila, 0] = self.cubo[self.BLANCO, self.piezas - 1, fila]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.VERDE)
    def __Fp(self):
        self.__F();
        self.__F();
        self.__F();
        
    def __B(self):
        cuboAux = np.copy(self.cubo);
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
            filaIn = (self.piezas - 1) - fila;
            cuboAux[self.BLANCO, 0, fila] = self.cubo[self.ROJO, fila, self.piezas - 1]
            cuboAux[self.ROJO, fila, self.piezas - 1] = self.cubo[self.AMARILLO, self.piezas - 1, filaIn]
            cuboAux[self.AMARILLO, self.piezas - 1, fila] = self.cubo[self.NARANJA, fila, 0]
            cuboAux[self.NARANJA, fila, 0] = self.cubo[self.BLANCO, 0, filaIn]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.AZUL)
    def __Bp(self):
        self.__B();
        self.__B();
        self.__B();
    
    def ejecutarMovimiento(self, movimiento):
        movimiento = movimiento.lower();
        if movimiento == 'r':
            self.__R();
        elif movimiento == 'rp':
            self.__Rp();
        elif movimiento == 'r2':
            self.__R();
            self.__R();
        elif movimiento == 'l':
            self.__L();
        elif movimiento == 'lp':
            self.__Lp();
        elif movimiento == 'l2':
            self.__L();
            self.__L();
        elif movimiento == 'u':
            self.__U();
        elif movimiento == 'up':
            self.__Up();
        elif movimiento == 'u2':
            self.__U();
            self.__U();
        elif movimiento == 'd':
            self.__D();
        elif movimiento == 'dp':
            self.__Dp();
        elif movimiento == 'd2':
            self.__D();
            self.__D();
        elif movimiento == 'f':
            self.__F();
        elif movimiento == 'fp':
            self.__Fp();
        elif movimiento == 'f2':
            self.__F();
            self.__F();
        elif movimiento == 'b':
            self.__B();
        elif movimiento == 'bp':
            self.__Bp();
        elif movimiento == 'b2':
            self.__B();
            self.__B();
        return self;
    
    def reset(self):
        self.__inicializar();
        return self;
    
    def ejecutarAlgoritmo(self, algoritmo):
        algoritmo = algoritmo.replace("'", "p").lower().split();
        for movimiento in algoritmo:
            self.ejecutarMovimiento(movimiento);
        return self;
    