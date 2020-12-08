from bcktraking import laberintoADT
import time
pasillo_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lap=laberintoADT(6,6,pasillo_inicial,(5,2),(2,5))
lap.buscar_entrada()
lap.to_string()
lap.imprimir_camino()
while not  lap.es_salida(lap.get_pos_actual()[0],lap.get_pos_actual()[1]):
    lap.resolver_labarinto()
    lap.imprimir_camino()
