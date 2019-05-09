import numpy as np;
class Cube:
    BLANCO = 0;
    VERDE = 1;
    NARANJA = 2;
    AZUL = 3;
    ROJO = 4;
    AMARILLO = 5;
    
    colores = ['b', 'v', 'n', 'a', 'r', 'A'];
    
    cubo = np.zeros((6,3,3), int);
    
    def __init__(self):
        self.caras = 6;
        self.piezas = 3;
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
        
    def __rotarCaraReloj(self, cara):
        cuboAux = np.copy(self.cubo);
        for x in range(self.piezas):
            print()
            cuboAux[cara, :, (self.piezas - 1)- x] = self.cubo[cara, x]
        self.cubo = np.copy(cuboAux);
    def __rotarCaraContrarioReloj(self, cara):
        self.cubo[cara] = np.rot90(self.cubo[cara]);
        
    def __R(self):
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
            for columna in range(self.piezas):
                cuboAux[self.VERDE, fila, 2] = self.cubo[self.AMARILLO, fila, 2]
                cuboAux[self.BLANCO, fila, 2] = self.cubo[self.VERDE, fila, 2]
                
        cuboAux[self.AZUL, 0, 0] = self.cubo[self.BLANCO, 2, 2]
        cuboAux[self.AZUL, 1, 0] = self.cubo[self.BLANCO, 1, 2]
        cuboAux[self.AZUL, 2, 0] = self.cubo[self.BLANCO, 0, 2]
        
        cuboAux[self.AMARILLO, 0, 2] = self.cubo[self.AZUL, 2, 0]
        cuboAux[self.AMARILLO, 1, 2] = self.cubo[self.AZUL, 1, 0]
        cuboAux[self.AMARILLO, 2, 2] = self.cubo[self.AZUL, 0, 0]

        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.ROJO)
    def __Rp(self):
        self.__R();
        self.__R();
        self.__R();
        
    def __L(self):
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
            for columna in range(self.piezas):
                cuboAux[self.VERDE, fila, 0] = self.cubo[self.BLANCO, fila, 0]
                cuboAux[self.AMARILLO, fila, 0] = self.cubo[self.VERDE, fila, 0]
        cuboAux[self.BLANCO, 0, 0] = self.cubo[self.AZUL, 2, 2]
        cuboAux[self.BLANCO, 1, 0] = self.cubo[self.AZUL, 1, 2]
        cuboAux[self.BLANCO, 2, 0] = self.cubo[self.AZUL, 0, 2]
        
        cuboAux[self.AZUL, 0, 2] = self.cubo[self.AMARILLO, 2, 0]
        cuboAux[self.AZUL, 1, 2] = self.cubo[self.AMARILLO, 1, 0]
        cuboAux[self.AZUL, 2, 2] = self.cubo[self.AMARILLO, 0, 0]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.NARANJA)
    def __Lp(self):
        self.__L();
        self.__L();
        self.__L();
        
    def __U(self):
        cuboAux = np.copy(self.cubo);
        for fila in range(self.piezas):
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
        for fila in range(self.piezas):
            for columna in range(self.piezas):
                cuboAux[self.VERDE, 2, columna] = self.cubo[self.NARANJA, 2, columna]
                cuboAux[self.NARANJA, 2, columna] = self.cubo[self.AZUL, 2, columna]
                cuboAux[self.AZUL, 2, columna] = self.cubo[self.ROJO, 2, columna]
                cuboAux[self.ROJO, 2, columna] = self.cubo[self.VERDE, 2, columna]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.AMARILLO)
    def __Dp(self):
        self.__D();
        self.__D();
        self.__D();
        
    def __F(self):
        cuboAux = np.copy(self.cubo);
        cuboAux[self.BLANCO, 2, 0] = self.cubo[self.NARANJA, 2, 2]
        cuboAux[self.BLANCO, 2, 1] = self.cubo[self.NARANJA, 1, 2]
        cuboAux[self.BLANCO, 2, 2] = self.cubo[self.NARANJA, 0, 2]
        
        cuboAux[self.AMARILLO, 0, 0] = self.cubo[self.ROJO, 2, 0]
        cuboAux[self.AMARILLO, 0, 1] = self.cubo[self.ROJO, 1, 0]
        cuboAux[self.AMARILLO, 0, 2] = self.cubo[self.ROJO, 0, 0]
        
        cuboAux[self.NARANJA, 0, 2] = self.cubo[self.AMARILLO, 0, 0]
        cuboAux[self.NARANJA, 1, 2] = self.cubo[self.AMARILLO, 0, 1]
        cuboAux[self.NARANJA, 2, 2] = self.cubo[self.AMARILLO, 0, 2]
        
        cuboAux[self.ROJO, 0, 0] = self.cubo[self.BLANCO, 2, 0]
        cuboAux[self.ROJO, 1, 0] = self.cubo[self.BLANCO, 2, 1]
        cuboAux[self.ROJO, 2, 0] = self.cubo[self.BLANCO, 2, 2]
        self.cubo = np.copy(cuboAux);
        self.__rotarCaraReloj(self.VERDE)
    def __Fp(self):
        self.__F();
        self.__F();
        self.__F();
        
    def __B(self):
        cuboAux = np.copy(self.cubo);
        cuboAux[self.BLANCO, 0, 0] = self.cubo[self.ROJO, 0, 2]
        cuboAux[self.BLANCO, 0, 1] = self.cubo[self.ROJO, 1, 2]
        cuboAux[self.BLANCO, 0, 2] = self.cubo[self.ROJO, 2, 2]
        
        cuboAux[self.ROJO, 0, 2] = self.cubo[self.AMARILLO, 2, 2]
        cuboAux[self.ROJO, 1, 2] = self.cubo[self.AMARILLO, 2, 1]
        cuboAux[self.ROJO, 2, 2] = self.cubo[self.AMARILLO, 2, 0]
        
        cuboAux[self.AMARILLO, 2, 0] = self.cubo[self.NARANJA, 0, 0]
        cuboAux[self.AMARILLO, 2, 1] = self.cubo[self.NARANJA, 1, 0]
        cuboAux[self.AMARILLO, 2, 2] = self.cubo[self.NARANJA, 2, 0]
        
        cuboAux[self.NARANJA, 0, 0] = self.cubo[self.BLANCO, 0, 2]
        cuboAux[self.NARANJA, 1, 0] = self.cubo[self.BLANCO, 0, 1]
        cuboAux[self.NARANJA, 2, 0] = self.cubo[self.BLANCO, 0, 0];
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
        return self.cubo;
    
    def reset(self):
        self.__inicializar();
        return self.cubo;
    
    def ejecutarAlgoritmo(self, algoritmo):
        algoritmo = algoritmo.replace("'", "p").lower().split();
        for movimiento in algoritmo:
            #print(movimiento);
            self.ejecutarMovimiento(movimiento);
            #self.imprimir();
        return self.cubo;
            
    def ejecutar(self):
        self.imprimir();
        self.__rotarCaraReloj(self.ROJO);
        self.imprimir();
    