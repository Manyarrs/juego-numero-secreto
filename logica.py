import random 
def generar_numero_secreto():
    return random.randint(1,10)
def evaluar_intento(intento,numero_secreto):

    if intento == numero_secreto:
        return "Acierto"
    elif intento < numero_secreto:
        return "Bajo"
    else:
        return "Alto"