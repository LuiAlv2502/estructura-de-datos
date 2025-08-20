import json 


with open('tarea2/ejercicio4/dron.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

import queue

st = queue.LifoQueue()
i = 0
while datos[i].get("cmd") != "RETURN":
    st.put(datos[i])
    i += 1
    
while not st.empty():
    value = st.get()
    if value.get("cmd") == "MOVE":
        print(f"MOVE_BACK {value.get('x')}")
    elif value.get("cmd") == "TURN_LEFT":
        print("TURN_RIGHT")
    elif value.get("cmd") == "TURN_RIGHT":
        print("TURN_LEFT")  