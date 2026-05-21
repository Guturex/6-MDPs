"""
Para desarrollar el problema del inventario.

"""
import math
from MDPs import MDP, iteracion_valor

class Inventario(MDP):
    """
    MDP para el problema de inventario

    Estado s: inventario neto al final del dia
    s > 0 -> unidades en almacen
    s = 0 -> sin stock
    s < 0 -> backlog

    Accion a: cuantas unidades pedir esa tarde
    """    
    
    def __init__(self, gama,lambda_, capacidad=20, backlog_max=10,
                 precio=150, costo_var=80, costo_fijo=40, costo_hold=5,
                 costo_back=15, margen_perd=70): 
        #Espacio de estados
        estados = list(range(-backlog_max, capacidad + 1))
        super().__init__(estados, gama)

        self.lambda = lambda_
        self.capacidad = capacidad
        self.backlog_max = backlog_max
        self.precio = precio
        self.costo_var = costo_var
        self.costo_fijo = costo_fijo
        self.costo_hold = costo_hold
        self.costo_back = costo_back
        self.margen_perd = margen_perd
        
        self.s_min = -backlog_max
        self.s_max = capacidad

        #Truncar la demanda donde la probalbilidad acumulada es -1
        self.D_max = 0
        while poisson_pmf(self.D_max, lambda_) > 1e-9:
            self.D_max += 1
    
    def acciones_legales(self, s):
        """
        A(s) = {0, 1, ..., capacidad - s}

        No puede pedir negativo y el almacen no puede recibir mas
        de lo que cabe
        """
        return list(range(0, self.capacidad - s + 1))
    
    def recompensa(self, s, a, s_):
        #TODO: Completar este método
        pass
        
    def prob_transicion(self, s, a, s_):
        #TODO: Completar este método
        pass
                
    def es_terminal(self, s):
        #TODO: Completar este método
        pass


if __name__ == "__main__":

    inventario = Inventario(0.9, 0.5, ...)  #TODO: Agregar lo que se requiera

    pi_star, V = iteracion_valor(inventario, ...) #TODO: Agregar lo que se requiera

    print("-" * 60)
    print("Estado".center(20) + "Acción".center(20) + "Valor".center(20))
    print("-" * 60 )
    for s in pi_star:
        print(f"{s:^20}{pi_star[s]:^20}{V[s]:^20.2f}")
    print("-" * 60)


"""
Contesta las preguntas aquí mismo (has espacio entre las preguntas):

1. ¿Cómo se comporta las transiciones y las ganancias para casos específicos de $s$ y $a$? 
2. ¿Qué psa si hay mucho almacen? 
3. ¿Que pasa si hay muy poco o estamos sin almacen? 
4. ¿Existe un punto donde la ganancia sea máxima?  
---
5. ¿Cómo se ve la política óptima? ¿Tiene sentido?
6. ¿Como se comporta la función de valor de estado V(s)?
7. ¿Cómo cambiaría la política si la variabilidad de la demanda (lambda) aumenta de 4 a 8?

"""