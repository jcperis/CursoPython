import json
import pickle


# ---------- Exportar texto ----------

def exportar_lista_txt(nombre_fichero, datos):
    try:
        with open(nombre_fichero, 'w', encoding='utf-8') as f:
            for item in datos:
                f.write(f"{item}\n")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def exportar_json(nombre_fichero, datos):
    try:
        with open(nombre_fichero, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")


# ---------- Importar texto ----------

def importar_lista_txt(nombre_fichero):
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_fichero}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado al abrir el archivo: {e}")
        return None

def importar_json(nombre_fichero: str):
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_fichero}' no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_fichero}' contiene JSON inválido.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado al abrir el archivo: {e}")
        return None


# ---------- Exportar / Importar binario (pickle) ----------

def exportar_pickle(nombre_fichero, datos):
    try:
        with open(nombre_fichero, 'wb') as f:
            pickle.dump(datos, f)
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def importar_pickle(nombre_fichero):
    try:
        with open(nombre_fichero, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")
