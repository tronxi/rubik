from tkinter import *;
from tkinter import ttk;
import threading;
import numpy as np;
import rubik;
import posicion;
from functools import partial

class InterfazGrafica():

    colores = ['white', 'green', 'orange', 'blue', 'red', 'yellow'];
    movimientos = ['R', 'Rp', 'R2', 'L', 'Lp', 'L2', 'U', 'Up', 'U2', 'D', 'Dp', 'D2', 'F', 'Fp', 'F2', 'B', 'Bp', 'B2'];
    
    
    def __init__(self):
        self.ins = rubik.Cube();
        
        self.cuboGraficos = np.zeros((self.ins.caras, self.ins.piezas, self.ins.piezas), Label);
        self.posiciones = np.zeros((self.ins.caras, self.ins.piezas, self.ins.piezas), posicion.Posicion);
    
        self.crearPosiciones();
        
        self.raiz = Tk();
        self.raiz.geometry('1050x500');
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Rubik');
        
        self.inicializar();
        self.textAlgoritmo = Entry(self.raiz, width = 70);
        self.textAlgoritmo.grid(row = 15, column = 15);
        
        self.resetButton = Button(self.raiz, text="Reset", command=self.reset);
        self.resetButton.grid(row = 20,column = 0);
        
        self.algoritmoButton = Button(self.raiz, text="Ejecutar", command=self.algoritmo);
        self.algoritmoButton.grid(row = 15,column = 17);
        
        self.crearBotonesMovimiento();
        
        self.reset();
        self.raiz.mainloop();
        
        
    def crearPosiciones(self):
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[0, x, y] = posicion.Posicion(x + self.ins.piezas, y + self.ins.piezas);
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[1, x, y] = posicion.Posicion(x + (2*self.ins.piezas), y + self.ins.piezas);
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[4, x, y] = posicion.Posicion(x + (2*self.ins.piezas), y + (2*self.ins.piezas));
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[3, x, y] = posicion.Posicion(x + (2*self.ins.piezas), y + (3*self.ins.piezas));
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[5, x, y] = posicion.Posicion(x + (3*self.ins.piezas), y + self.ins.piezas);
        for x in range(self.ins.piezas):
            for y in range(self.ins.piezas):
                self.posiciones[2, x, y] = posicion.Posicion(x + (2*self.ins.piezas), y);
                
    def crearBotonesMovimiento(self):
        fila = 22;
        columna = 0;
        for movimiento in self.movimientos:
            action_movimiento = partial(self.botonMovimiento, movimiento)
            movimientoButton = Button(self.raiz, text=movimiento, 
                                      command = action_movimiento, width = 2);
            movimientoButton.grid(row = fila, column = columna);
            columna += 1;
            if columna % 6 == 0:
                fila += 1;
                columna = 0;
                
    def inicializar(self):
        fila = 0;
        for cara in range(self.ins.caras):
            for x in range(self.ins.piezas):
                for y in range(self.ins.piezas):
                    self.cuboGraficos[cara, x, y] = Label(self.raiz, width=5, height=2, relief="solid");

                    if (y + 1) % self.ins.piezas == 0:
                        self.cuboGraficos[cara, x, y].grid(
                            row = self.posiciones[cara, x, y].x, 
                            column = self.posiciones[cara, x, y].y, padx = (0, 10));
                    if (x + 1) % self.ins.piezas == 0:
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
        for cara in range(cubo.caras):
            for x in range(cubo.piezas):
                for y in range(cubo.piezas):
                    self.cuboGraficos[cara, x, y].configure(background = self.colores[cubo.cubo[cara, x, y]]);