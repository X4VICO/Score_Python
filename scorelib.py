# LIBRERÍA PRINCIPAL

class Score:
    # ----- función inicial de la clase "Score" -----
    def __init__(self, scorefile='score.txt'): # aseguramos de nuevo que el valor por defecto de "scorefile" sea "score.txt"
        self.scorefile = scorefile # guardamos el valor obtenido en la variable de la instancia
        # creamos una lista de las 20 posiciones posibles que tendrá el archivo de puntuaciones
        self.posiciones = [" 1ST", " 2ND", " 3RD", " 4TH", " 5TH", " 6TH", " 7TH", " 8TH", " 9TH", "10TH", "11TH", "12TH", "13TH", "14TH", "15TH", "16TH", "17TH", "18TH", "19TH", "20TH"]
    
    # ----- función añadir resultados -----
    def add_score(self, points, name, scorefile=None): # aplicamos "scorefile=None" por si no hemos obtenido ningún argumento de archivo, se use el valor por defecto "score.txt"
        if not (0 <= points <= 99999): # si el valor de "points" no está dentro del rango especifico...
            print("Error al registrar puntos.") # ... informamos del error...
            return # ... seguidamente salimos de la función finalizando el script
        if len(name) != 3: # si no se introduce un nombre con una longitud de 3 caracteres alfanuméricos...
            print("Error al registrar créditos.") # ... informamos del error...
            return # ... seguidamente salimos de la función finalizando el script
                
        name = name.upper() # pasamos los caracteres introducidos en el nombre a mayúsculas
        new_score = (points, name) # guardamos los valores nuevos en una variable llamada "new_score"

        # como tuvimos problemas con "scorefile", en el caso de no obtener ningún argumento... 
        if scorefile is None: # ... decidimos, de nuevo, asegurarnos de que la variable use el valor por defecto "score.txt"
            scorefile = self.scorefile
        
        scores = self.get_scores(scorefile) # llamamos a la función "get_scores", donde "scores" será una lista donde almacenar las puntuaciones
        
        # ----- verificación resultados mostrados -----
        # comprobamos que las puntuaciones nuevas estén dentro del limite del top 20. Si lo están, comprobamos que los puntos de estas nuevas puntuaciónes... 
        if len(scores) >= 20 and points <= scores[-1][0]: # ... séan mayores a los de la ultima puntuación ([1] = ultimo del top 20) ([0] = argumento points) 
            print("Vuelve a jugar para mejorar tu puntuación.") # en el caso de no estar dentro del top o tener menos puntos que el top 20, informamos de ello...
            return # ... seguidamente salimos de la función finalizando el script

        scores.append(new_score) # añadimos la nueva puntuación a la lista "scores"
        scores = sorted(scores, key=lambda x: -x[0])[:20] # ordenamos los puntos ([0] = argumento points) de forma descendente (-x) y nos quedamos con los 20 primeros ([:20]) 

        with open(scorefile, 'w') as fichero: # hacemos uso del "with open...as fichero" para que se cierre "scorefile" al salir del with
            for i, (score_points, score_name) in enumerate(scores): # enumeramos y damos variables a los valores de cada puntuación que hay dentro de "scores"
                position = self.posiciones[i] # asignamos a una variable nueva la posición correspondiente 
                fichero.write(f"{position}     {str(score_points).zfill(5)}   {score_name}\n") # escribimos en el fichero la puntuacion con su formato correspondiente

    # ----- función coger resultados -----
    def get_scores(self, scorefile=None): 
        if scorefile is None: # aseguramos de que si no se ha escogido archivo, se use el valor por defecto "score.txt"
            scorefile = self.scorefile 
        
        scores = [] # creamos una lista vacía
        
        try: # usamos "try" por si nos da un error al abrir el archivo
            with open(scorefile, 'r') as fichero:
                for linea in fichero:
                    partes = linea.strip().split() # quitamos los espacios en blanco y dividimos la línea en partes
                    points = int(partes[1]) # ([1] = puntuación) guardamos la primera partición en "points"  
                    name = partes[2] # ([2] = nombre) guardamos la segunda partición en "name"  
                    scores.append((points, name)) # lo añadimos a la lista "scores"
        except FileNotFoundError:
            pass
        return scores # devolvemos el resultado de la lista obtenida en esta función
