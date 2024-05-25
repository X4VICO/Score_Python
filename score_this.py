# SCRIPT QUE SE EJECUTA
# invocación del script = $ python score_this.py 18700 “AGC” “willoom.txt”

from scorelib import Score # libreria principal donde se encuentran las funciones
import sys # importamos esta libreria para poder leer los parametros introducidos a la hora de ejecutar el script

# ------verificación de argumentos------
# en el caso de que no se introduzca la invocación del script correctamente, mostramos un ejemplo de uso
if len(sys.argv) < 3:
    print("Uso: $ python score_this.py <puntuación> <iniciales> [archivo]")
    sys.exit(1) # cerramos el programa e indicamos con argumento 1 que ha sido a causa de un error en la ejecución

# ------verificación de puntos------
# como solo queremos que los puntos contengan números, hacemos uso de try
try:
    points = int(sys.argv[1])
except ValueError: # en el caso de que el valor introducido no sean números, mostramos el error
    print("Error al registrar puntos. Deben ser números enteros.")
    sys.exit(1) # cerramos el programa e indicamos con argumento 1 que ha sido a causa de un error en la ejecución

# ------verificación de nombre------
# en el caso de que el nombre tenga una longitud diferente a 3 caracteres, mostramos el error
name = sys.argv[2]
if len(name) != 3:
    print("Error al registrar créditos. Deben ser 3 caracteres.")
    sys.exit(1) # cerramos el programa e indicamos con argumento 1 que ha sido a causa de un error en la ejecución

# ------verificación de archivo------
# en el caso de que no se introduzca un tercer argumento indicando el nombre del archivo, se usará por defecto "score.txt"
scorefile = sys.argv[3] if len(sys.argv) > 3 else "score.txt"

score = Score(scorefile) # creamos un objeto "Score" con el nombre del archivo de puntuaciones
score.add_score(points, name, scorefile) # llamamos a la función add_score que hay en el objeto "Score" con los valores de points y name