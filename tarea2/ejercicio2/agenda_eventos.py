import json
from datetime import datetime, timedelta

with open('tarea2/ejercicio2/eventos.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

#print(datos)

class Evento:
    def __init__(self, inicio, duracion, sala):
        self.inicio = inicio
        self.duracion = duracion
        self.sala = sala
        
    def calcular_hora(self):
        t = datetime.strptime(self.inicio, "%H:%M")
        t += timedelta(minutes=self.duracion)
        return t.strftime("%H:%M")
    def to_dict(self):
        return {
            "inicio": self.inicio,
            "duracion": self.duracion,
            "sala": self.sala
        }

def fusionar_eventos(evento1, evento2):
    if evento1.sala == evento2.sala and evento1.calcular_hora() == evento2.inicio:
        return Evento(evento1.inicio, evento1.duracion + evento2.duracion, evento1.sala)
    return None

def main():
    eventos = [Evento(evento['inicio'], evento['duracion'], evento['sala']) for evento in datos]

    eventos_fusionados = []
    i = 0
    while i < len(eventos):
        actual = eventos[i]
        j = i + 1
        while j < len(eventos):
            fusion = fusionar_eventos(actual, eventos[j])
            if fusion:
                actual = fusion
            else:
                break
            j += 1
        eventos_fusionados.append(actual)
        i = j

    print(json.dumps([e.to_dict() for e in eventos_fusionados], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()