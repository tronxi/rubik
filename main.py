import rubik;
import numpy as np;

ins = rubik.Cube();
algoritmo = "B F D R B F U2 L2 U' B R2 B U' F' U' L' B' L2 D' F U' B2 D B' L2 U' B D R2 U2";
ins.ejecutarAlgoritmo(algoritmo);
ins.imprimir();

