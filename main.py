import rubik;
import numpy as np;

ins = rubik.Cube();
algoritmo = "R' D U B2 F' R2 U R2 B' F' D' B F2 R' F' L2 D2 L2 B L2 R D' L R2 F2 R B2 D' F L2";
ins.ejecutarAlgoritmo(algoritmo);
ins.imprimir();