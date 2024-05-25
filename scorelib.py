# LIBRERIA PRINCIPAL

# creamos un objeto
class Score:
    # iniciamos y escribimos el arrray que usaremos para las posiciones
    def __init__(self, scorefile='score.txt'):
        self.scorefile = scorefile
        self.posiciones = [" 1ST", " 2ND", " 3RD", " 4TH", " 5TH", " 6TH", " 7TH", " 8TH", " 9TH", "10TH", "11TH", "12TH", "13TH", "14TH", "15TH", "16TH", "17TH", "18TH", "19TH", "20TH"]
    
# ------función para añadir puntos------
    def add_score(self, points, name, scorefile=None):
        # verificamos que el numero intrducido esta dentro los parametros correctos
        if not (0 <= points <= 99999):
            print("Error al registrar puntos.")
        # verificamos que el nombre tiene 3 caracteres
        if len(name) != 3:
            print("Error al registrar créditos.")
            return 
                
        name = name.upper() # nombre en mayusculas
        new_score = (points, name) # creamos la variable new_score
        
        # nos aseguramos que usa el archivo de puntuacion correcto
        if scorefile is None:
            scorefile = self.scorefile

        scores = self.get_scores(scorefile)
        
        # si la nueva puntuacion no entra en el top 20 y los puntos introducidos son menores que el 20TH actual... 
        if len(scores) >= 20 and points <= scores[-1][0]:
            print("Vuelve a jugar para mejorar tu puntuación.") # ...muestra esto
            return

        # añadimos la nueva puntuacion y ordenamos la lista de puntuaciones y guarda solo las top 20
        scores.append(new_score)
        scores = sorted(scores, key=lambda x: -x[0])[:20]

        # abrimos fichero en modo ecritura, obtiene los parametros... 
        with open(scorefile, 'w') as fichero:
            for i, (score_points, score_name) in enumerate(scores):
                position = self.posiciones[i] # ...agrega la posicion... 
                fichero.write(f"{position}     {str(score_points).zfill(5)}   {score_name}\n")   

    # ------función para leer puntuaciones actuales------ 
    def get_scores(self, scorefile=None):
        # comprobamos que el fichero de scorefile es el correcto
        if scorefile is None:
            scorefile = self.scorefile # y si no hay ninguno especificado, usamos el score.txt de self
        scores = [] # creamos una array vacia
        
        try: # si no hay archivo sale del bucle para evitar el error
            # abre el archivo de puntuaciones en modo lectura
            with open(scorefile, 'r') as fichero:
                for linea in fichero:
                    partes = linea.strip().split() # separa la linea por columna y por fila
                    points = int(partes[1]) # convierte la puntuación a int
                    name = partes[2] # asigna el 3r elemento de partes a name
                    scores.append((points, name)) # y agrega puntuación, nombre a la lista de puntuaciones
        except FileNotFoundError:
            pass
        return scores
