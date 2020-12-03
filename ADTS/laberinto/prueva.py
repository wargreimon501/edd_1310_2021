from bcktraking import laberintoADT
pasillo_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lap=laberintoADT(6,6,pasillo_inicial,(5,2),(2,5))
lap.to_string()
lap.es_salida(2,5)
