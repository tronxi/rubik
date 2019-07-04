from itertools import *;
import rubik;
import numpy as np;
from datetime import datetime, date, time, timedelta


class Solve:
    movimientos = ['R', 'Rp', 'R2', 'L', 'Lp', 'L2', 'U', 'Up', 'U2', 'D', 'Dp', 'D2', 'F', 'Fp', 'F2', 'B', 'Bp', 'B2'];
    
    def __init__(self, c):
        self.cubo = c;
        
    def resolver(self):
        for numeroMovimientos in range(21):
            lista = self.getLista(numeroMovimientos);
            print('tengo la lista ' + str(numeroMovimientos)+ ' lista con ' + str(len(lista)));
            for algoritmo in lista:
                cuboAux = np.copy(self.cubo.cubo);
                nuevoAlgoritmo = ' '.join(algoritmo);
                self.cubo.ejecutarAlgoritmo(nuevoAlgoritmo);
                if self.cubo.resuelto():
                    self.cubo.cubo = np.copy(cuboAux);
                    return True, nuevoAlgoritmo;
                else:
                    self.cubo.cubo = np.copy(cuboAux);
        return False, 'error';

    
    def getLista(self, repeat):
        print('pido lista con' + str(repeat));
        return np.asarray(list(product(self.movimientos,repeat = repeat)));
    def ejecutar(self):
        for i in range(21):
            timeAntes = datetime.now();
            lista = self.getLista(i);
            timeDespues = datetime.now();
            timeTotal = timeDespues - timeAntes;
            print('lista '+ str(i) + ' tarda '+  str(timeTotal));
            print('lista con ' + str(len(lista)));