import json
import queue

with open('tarea2/ejercicio3/comedor.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

q_vip = queue.Queue()
q_bulk = queue.Queue()
q_norm = queue.Queue()

for cliente in datos:
    if cliente['tipo'] == 'VIP':
        q_vip.put(cliente)
    elif cliente['tipo'] == 'BULK':
        q_bulk.put(cliente)
    else:
        q_norm.put(cliente)

q_fusionada = queue.Queue()
while not q_vip.empty():
    q_fusionada.put(q_vip.get())

while not q_bulk.empty():
    q_fusionada.put(q_bulk.get())

while not q_norm.empty():
    q_fusionada.put(q_norm.get())
print(q_fusionada.queue)