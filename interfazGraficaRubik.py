from tkinter import *;
from tkinter import ttk;
import threading;
import numpy as np;
import rubik;
import posicion;
from functools import partial

class InterfazGrafica():

    colores = ['white', 'green', 'orange', 'blue', 'red', 'yellow'];
    movimientos = ['R', 'Rp', 'R2', 'L', 'Lp', 'L2', 'U', 'Up', 'U2', 'B', 'Bp', 'B2', 'F', 'Fp', 'F2', 'B', 'Bp', 'B2'];
    posiciones = np.zeros((6,3,3), posicion.Posicion);
    
    for x in range(3):
        for y in range(3):
            posiciones[0, x, y] = posicion.Posicion(x + 3, y + 3);
    for x in range(3):
        for y in range(3):
            posiciones[1, x, y] = posicion.Posicion(x + (2*3), y + 3);
    for x in range(3):
        for y in range(3):
            posiciones[4, x, y] = posicion.Posicion(x + (2*3), y + (2*3));
    for x in range(3):
        for y in range(3):
            posiciones[3, x, y] = posicion.Posicion(x + (2*3), y + (3*3));
    for x in range(3):
        for y in range(3):
            posiciones[5, x, y] = posicion.Posicion(x + (3*3), y + 3);
    for x in range(3):
        for y in range(3):
            posiciones[2, x, y] = posicion.Posicion(x + (2*3), y);
    
    def __init__(self):
        self.ins = rubik.Cube();
        self.cuboGraficos = np.zeros((6,3,3), Label);
        self.raiz = Tk();

        self.raiz.geometry('1050x500');
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Rubik');
        
        self.inicializar();
        self.textAlgoritmo = Entry(self.raiz, width = 70);
        self.textAlgoritmo.grid(row = 15, column = 15);
        
        resetButton = Button(self.raiz, text="Reset", command=self.reset);
        resetButton.grid(row = 20,column = 0);
        
        algoritmoButton = Button(self.raiz, text="Ejecutar", command=self.algoritmo);
        algoritmoButton.grid(row = 15,column = 17);
        
        fila = 22;
        columna = 0;
        for movimiento in self.movimientos:
            action_movimiento = partial(self.botonMovimiento, movimiento)
            movimientoButton = Button(self.raiz, text=movimiento, 
                                      command = action_movimiento, width = 2);
            movimientoButton.grid(row = fila, column = columna);
            columna += 1;
            print(str(columna));
            if columna % 6 == 0:
                fila += 1;
                columna = 0;
        
        self.reset();
        self.raiz.mainloop();
    
    def inicializar(self):
        fila = 0;
        for cara in range(6):
            for x in range(3):
                for y in range(3):
                    self.cuboGraficos[cara, x, y] = Label(self.raiz, width=5, height=2, relief="solid");

                    if (y + 1) % 3 == 0:
                        self.cuboGraficos[cara, x, y].grid(
                            row = self.posiciones[cara, x, y].x, 
                            column = self.posiciones[cara, x, y].y, padx = (0, 10));
                    if (x + 1) % 3 == 0:
                        self.cuboGraficos[cara, x, y].grid(
                            row = self.posiciones[cara, x, y].x, 
                            column = self.posiciones[cara, x, y].y, pady = (0, 10));
                    else:
                        self.cuboGraficos[cara, x, y].grid(
                            row = self.posiciones[cara, x, y].x, 
                            column = self.posiciones[cara, x, y].y);
                fila += 1;
                
    def algoritmo(self):
        algoritmo = self.textAlgoritmo.get();
        cubo = self.ins.ejecutarAlgoritmo(algoritmo);
        self.actualizar(cubo);
        
    def botonMovimiento(self, movimiento):
        cubo = self.ins.ejecutarMovimiento(movimiento);
        self.actualizar(cubo);
                    
    def reset(self):
        cubo = self.ins.reset();
        self.actualizar(cubo);
        
    def actualizar(self, cubo):
        for cara in range(6):
            for x in range(3):
                for y in range(3):
                    self.cuboGraficos[cara, x, y].configure(background = self.colores[cubo[cara, x, y]]);