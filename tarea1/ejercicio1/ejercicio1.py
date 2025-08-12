import time

def generar_archivo():
    with open("large_text.txt", "w") as f:
        for _ in range(1500000):
            f.write("The quick brown fox jumps over the lazy dog.\n")
            
#generar_archivo()


def lectura_caracter():
    inicio = time.time()
    with open("large_text.txt", "r") as file:
        while True:
            char = file.read(1)
            if not char:
                break
    fin = time.time()
    print(fin-inicio)
    
def lectura_linea():
    inicio = time.time()
    with open("large_text.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
    fin = time.time()
    print(fin-inicio)

def lectura_4bytes():
    inicio = time.time()
    with open("large_text.txt", "r") as file:
        while True:
            bloque = file.read(4096)
            if not bloque:
                break
    fin = time.time()
    print(fin-inicio)

lectura_caracter()      
lectura_linea()
lectura_4bytes()
