import pickle
import os

def save_data(profiles, filename="archivo.dat"):
    #comandos para hacer que el .dat se guarde en la misma carpeta que el .py
    folder = os.path.dirname(__file__)
    filepath = os.path.join(folder, filename)

    with open(filename, "wb") as f:
        pickle.dump(profiles, f)

def load_data(filename="archivo.dat"):
    folder = os.path.dirname(__file__)
    filepath = os.path.join(folder, filename)
    
    try:
        with open(filename, "rb") as f:
            profiles = pickle.load(f)
            return profiles
    except FileNotFoundError:
        print("No profile file found.")
        return {}
def add_value(pos_diccionario, key, value):
    if key in pos_diccionario:
        pos_diccionario[key] = value 
    else:
        pos_diccionario[key] = value



if __name__ == "__main__":
    lista_diccionarios = [ {"a":"10", "b":"20"}, {"c":"30", "d":"40"}, {"e":"50", "f":"60"} ] 
    add_value(lista_diccionarios[2], "nombre", "Diego")
    save_data(lista_diccionarios)
    loaded_data = load_data()
    print(loaded_data)