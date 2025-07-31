import requests

# Crear una URL para obtener los datos
# Datos de una vivienda
url_ref_cat = "https://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/Consulta_DNPRC?RefCat="
ref_cat = input("Introduce la referencia catastral: ")
url = f"{url_ref_cat}{ref_cat}"


# Intentar realizar la petición a la API
try:
    response = requests.get(url)
    response.raise_for_status()
    # Imprimir la respuesta en formato JSON.
    # Aquí podriamos manejar los datos obtenidos a nuestra conveniencia.
    datos = response.json()
    print(datos)
except Exception as e:
    print(f"Error al acceder a la API: {e}")
